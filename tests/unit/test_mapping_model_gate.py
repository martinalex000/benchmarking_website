from datetime import UTC, datetime, timedelta
from types import SimpleNamespace
from zoneinfo import ZoneInfo

from backend.mapping.batch import MappingGate
from backend.mapping.client import (
    DEEPSEEK_FLASH_MODEL,
    DEFAULT_MODEL,
    GLM_MODEL,
    SECOND_GLM_FLASH_ROUTE,
)


def test_rate_limit_cooldown_is_scoped_to_the_model():
    def now():
        return datetime(2026, 10, 13, 20, tzinfo=ZoneInfo("Europe/Berlin"))

    gate = MappingGate(
        20,
        daytime_streams=20,
        now=now,
        models={DEFAULT_MODEL, DEEPSEEK_FLASH_MODEL, GLM_MODEL},
    )
    gate._enter(DEEPSEEK_FLASH_MODEL)
    error = SimpleNamespace(
        status_code=429,
        response=SimpleNamespace(headers={"retry-after": "120"}),
    )
    gate._exit(DEEPSEEK_FLASH_MODEL, error)

    assert gate.rate_limits_by_model[DEEPSEEK_FLASH_MODEL] == 1
    assert gate.rate_limits_by_model[DEFAULT_MODEL] == 0
    assert gate.cooldowns_by_model[DEEPSEEK_FLASH_MODEL] > 0
    assert gate.cooldowns_by_model[DEFAULT_MODEL] == 0
    assert not gate.can_schedule(DEEPSEEK_FLASH_MODEL)
    assert gate.can_schedule(DEFAULT_MODEL)
    assert gate.can_schedule(GLM_MODEL)


def test_full_glm_daytime_access_is_opt_in():
    hour = 17

    def now():
        return datetime(2026, 10, 13, hour, tzinfo=ZoneInfo("Europe/Berlin"))

    gate = MappingGate(20, 20, now, models={DEFAULT_MODEL, DEEPSEEK_FLASH_MODEL, GLM_MODEL})

    assert not gate.model_enabled(GLM_MODEL)
    hour = 18
    assert gate.model_enabled(GLM_MODEL)
    hour = 7
    assert gate.model_enabled(GLM_MODEL)
    hour = 8
    assert not gate.model_enabled(GLM_MODEL)

    daytime_gate = MappingGate(
        20,
        20,
        now=lambda: datetime(2026, 10, 13, 17, tzinfo=ZoneInfo("Europe/Berlin")),
        models={DEFAULT_MODEL, GLM_MODEL},
        full_glm_daytime=True,
    )
    assert daytime_gate.model_enabled(GLM_MODEL)


def test_key_two_allows_fifty_streams_while_primary_remains_capped_at_twenty(monkeypatch):

    def now():
        return datetime(2026, 10, 13, 20, tzinfo=ZoneInfo("Europe/Berlin"))

    gate = MappingGate(
        20,
        daytime_streams=20,
        now=now,
        models={DEFAULT_MODEL, DEEPSEEK_FLASH_MODEL, GLM_MODEL, SECOND_GLM_FLASH_ROUTE},
    )
    gate._limits.update(dict.fromkeys(gate.models, 20))
    gate._limits[SECOND_GLM_FLASH_ROUTE] = 50
    monkeypatch.setattr(gate, "_request_wait_seconds", lambda *_: 0)

    assert gate.limit == 70

    primary_models = [DEFAULT_MODEL, DEEPSEEK_FLASH_MODEL, GLM_MODEL]
    acquired = []
    for index in range(20):
        model = primary_models[index % len(primary_models)]
        gate._enter(model)
        acquired.append(model)
    for _ in range(50):
        model = SECOND_GLM_FLASH_ROUTE
        gate._enter(model)
        acquired.append(model)
    assert gate.active == 70
    assert not any(gate.can_schedule(model) for model in primary_models)
    assert not gate.can_schedule(SECOND_GLM_FLASH_ROUTE)
    for model in acquired:
        gate._exit(model, None)
    assert gate.active == 0


def test_key_two_fact_tasks_can_queue_ahead_of_key_one_verifier_capacity():
    gate = MappingGate(
        20,
        20,
        models={DEFAULT_MODEL, GLM_MODEL, SECOND_GLM_FLASH_ROUTE},
        second_key_maximum=50,
    )
    gate._limits[GLM_MODEL] = 10

    assert gate.paper_task_limit(GLM_MODEL, SECOND_GLM_FLASH_ROUTE) == 60
    assert gate.paper_task_limit(GLM_MODEL, DEFAULT_MODEL) == 10
    assert gate.model_limit(GLM_MODEL) == 10


def test_paper_worker_capacity_reserves_fact_workers_while_verifiers_are_gated():
    def now():
        return datetime(2026, 10, 13, 20, tzinfo=ZoneInfo("Europe/Berlin"))

    gate = MappingGate(
        20,
        20,
        now=now,
        models={DEFAULT_MODEL, GLM_MODEL, SECOND_GLM_FLASH_ROUTE},
        second_key_maximum=50,
    )
    gate._limits.update({DEFAULT_MODEL: 3, GLM_MODEL: 2, SECOND_GLM_FLASH_ROUTE: 50})

    assert gate.limit == 70
    assert gate.paper_worker_capacity == 105


def test_second_key_verification_is_only_available_after_phase_one_drains():
    gate = MappingGate(
        20,
        20,
        models={DEFAULT_MODEL, SECOND_GLM_FLASH_ROUTE},
        second_key_maximum=50,
    )
    gate.set_phase1_pending(1)

    assert gate.phase1_pending() == 1
    assert gate.phase2_model(DEFAULT_MODEL, DEFAULT_MODEL) == DEFAULT_MODEL

    gate.phase1_finished()
    assert gate.phase1_pending() == 0
    assert gate.phase2_model(DEFAULT_MODEL, DEFAULT_MODEL) == SECOND_GLM_FLASH_ROUTE


def test_key_two_verification_waits_until_phase_one_queue_is_drained():
    gate = MappingGate(
        20,
        20,
        models={DEFAULT_MODEL, SECOND_GLM_FLASH_ROUTE},
    )
    gate.set_phase1_pending(1)

    assert gate.phase2_model(DEFAULT_MODEL, DEFAULT_MODEL) == DEFAULT_MODEL
    assert gate.phase2_model(DEFAULT_MODEL, SECOND_GLM_FLASH_ROUTE) == DEFAULT_MODEL

    gate.phase1_finished()
    assert gate.phase2_model(DEFAULT_MODEL, DEFAULT_MODEL) == SECOND_GLM_FLASH_ROUTE
    assert gate.phase2_model(DEFAULT_MODEL, SECOND_GLM_FLASH_ROUTE) == DEFAULT_MODEL


def test_flash_moves_to_verification_only_above_the_main_glm_buffer():
    gate = MappingGate(
        20,
        20,
        models={DEFAULT_MODEL, GLM_MODEL, SECOND_GLM_FLASH_ROUTE},
    )
    gate.set_phase1_pending(100)
    gate._phase2_pending = 31
    assert gate.phase2_model(GLM_MODEL, DEFAULT_MODEL) == DEFAULT_MODEL

    gate._phase2_pending = 30
    assert gate.phase2_model(GLM_MODEL, DEFAULT_MODEL) == GLM_MODEL


def test_retry_after_state_survives_a_process_restart():
    future = (datetime.now(UTC) + timedelta(seconds=60)).isoformat()
    gate = MappingGate(
        20,
        20,
        now=lambda: datetime(2026, 10, 13, 20, tzinfo=ZoneInfo("Europe/Berlin")),
        models={DEFAULT_MODEL, DEEPSEEK_FLASH_MODEL, GLM_MODEL},
        persisted_state={
            "cooldown_until_utc_by_model": {DEEPSEEK_FLASH_MODEL: future},
            "rate_limits_by_model": {DEEPSEEK_FLASH_MODEL: 3},
            "model_limits": {DEEPSEEK_FLASH_MODEL: 1},
        },
    )

    assert gate.cooldowns_by_model[DEEPSEEK_FLASH_MODEL] > 0
    assert gate.cooldowns_by_model[DEFAULT_MODEL] == 0
    assert gate.rate_limits_by_model[DEEPSEEK_FLASH_MODEL] == 3
    assert gate.model_limit(DEEPSEEK_FLASH_MODEL) == 1
    assert gate.can_schedule(DEFAULT_MODEL)
    assert gate.can_schedule(GLM_MODEL)


def test_minimum_model_concurrency_is_preserved_after_rate_limit():
    gate = MappingGate(
        20,
        20,
        models={DEFAULT_MODEL, GLM_MODEL},
        persisted_state={"model_limits": {DEFAULT_MODEL: 4}},
        minimum_model_limits={DEFAULT_MODEL: 10},
    )

    assert gate.model_limit(DEFAULT_MODEL) == 10
    gate._enter(DEFAULT_MODEL)
    error = SimpleNamespace(
        status_code=429,
        response=SimpleNamespace(headers={"retry-after": "120"}),
    )
    gate._exit(DEFAULT_MODEL, error)

    assert gate.model_limit(DEFAULT_MODEL) == 10
    assert not gate.can_schedule(DEFAULT_MODEL)

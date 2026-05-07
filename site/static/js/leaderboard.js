/**
 * leaderboard.js
 *
 * Handles:
 *  - Chart.js best-over-time STEP chart per dataset variant
 *  - Table column sorting
 *  - Show/hide std columns
 *  - Show/hide baseline rows
 *  - Hover sync between chart dots and table rows (yellow ring / row highlight)
 *  - Dataset variant switching
 */
(function () {
  "use strict";

  /* ── State ─────────────────────────────────────────────────────────── */
  const charts = {};           // variant slug → Chart instance
  let showStd = true;
  let showBaselines = true;
  let activeVariant = null;

  /* ── Init ───────────────────────────────────────────────────────────── */
  function init() {
    const cfg = window.leaderboardConfig || {};
    const variants = cfg.variants || [];

    variants.forEach(function (v) {
      const canvas = document.getElementById("chart-" + v.slug);
      if (canvas) {
        buildChart(canvas, v.slug, cfg.higherIsBetter !== false);
      }
    });

    _initSortableColumns();

    // Set initial active variant (first standard one)
    const standard = variants.find(function (v) { return v.is_standard; }) || variants[0];
    if (standard) {
      activeVariant = standard.slug;
    }
  }

  /* ── Variant switching ──────────────────────────────────────────────── */
  function switchVariant(slug) {
    activeVariant = slug;
    document.querySelectorAll(".variant-section").forEach(function (el) {
      el.style.display = el.dataset.variant === slug ? "" : "none";
    });
  }

  /* ── Std toggle ─────────────────────────────────────────────────────── */
  function toggleStd(enabled) {
    showStd = enabled;
    document.querySelectorAll(".col-std").forEach(function (el) {
      el.style.display = enabled ? "" : "none";
    });
    Object.values(charts).forEach(function (chart) {
      const ds = chart.data.datasets[0];
      if (ds) {
        ds.errorBarWhiskerRatio = enabled ? 0.5 : 0;
        chart.update();
      }
    });
  }

  /* ── Baseline toggle ────────────────────────────────────────────────── */
  function toggleBaselines(enabled) {
    showBaselines = enabled;
    document.querySelectorAll("tr.row-baseline").forEach(function (row) {
      row.style.display = enabled ? "" : "none";
    });
    _rerank();
  }

  /* ── Re-rank visible rows ───────────────────────────────────────────── */
  function _rerank() {
    document.querySelectorAll(".result-table tbody").forEach(function (tbody) {
      let rank = 1;
      tbody.querySelectorAll("tr").forEach(function (row) {
        if (row.style.display !== "none") {
          const rankCell = row.querySelector(".col-rank");
          if (rankCell) rankCell.textContent = rank++;
        }
      });
    });
  }

  /* ── Chart builder ──────────────────────────────────────────────────── */
  function buildChart(canvas, slug, higherIsBetter) {
    let milestones = [];
    try {
      milestones = JSON.parse(canvas.dataset.milestones || "[]");
    } catch (e) { /* ignore */ }

    if (!milestones.length || typeof Chart === "undefined") return;

    const labels = milestones.map(function (m) { return m.date || ""; });
    const values = milestones.map(function (m) { return m.value; });

    // Build step dataset: each milestone is a point; lines are horizontal steps
    const pointData = milestones.map(function (m, i) {
      return { x: m.date, y: m.value, std: m.std, model: m.model, arxiv_id: m.arxiv_id };
    });

    const chart = new Chart(canvas, {
      type: "line",
      data: {
        labels: labels,
        datasets: [{
          label: canvas.dataset.metric || "Score",
          data: values,
          stepped: "before",          // step chart
          borderColor: "#2563eb",
          backgroundColor: "rgba(37,99,235,0.1)",
          pointBackgroundColor: "#2563eb",
          pointRadius: 6,
          pointHoverRadius: 9,
          tension: 0,
          fill: false,
          _pointData: pointData,      // custom field for hover sync
        }],
      },
      options: {
        responsive: true,
        interaction: { mode: "nearest", axis: "x", intersect: false },
        plugins: {
          tooltip: {
            callbacks: {
              title: function (items) {
                const idx = items[0].dataIndex;
                const pd = pointData[idx];
                return pd ? pd.model + " (" + (pd.date || "") + ")" : "";
              },
              label: function (item) {
                const idx = item.dataIndex;
                const pd = pointData[idx];
                const stdStr = (pd && pd.std != null) ? " ± " + pd.std.toFixed(4) : "";
                return item.formattedValue + stdStr;
              },
              afterLabel: function (item) {
                const idx = item.dataIndex;
                const pd = pointData[idx];
                return pd ? "arXiv:" + (pd.arxiv_id || "") : "";
              },
            },
          },
          legend: { display: false },
        },
        scales: {
          x: { title: { display: true, text: "Date" } },
          y: {
            title: { display: true, text: canvas.dataset.metric || "Score" },
            ticks: { precision: 4 },
          },
        },
        onHover: function (event, elements) {
          _onChartHover(slug, elements, pointData);
        },
      },
    });

    charts[slug] = chart;
  }

  /* ── Chart → Table hover sync ───────────────────────────────────────── */
  function _onChartHover(slug, elements, pointData) {
    // Remove all existing highlights
    document.querySelectorAll("tr.chart-hover-highlight").forEach(function (row) {
      row.classList.remove("chart-hover-highlight");
    });

    if (!elements.length) return;
    const idx = elements[0].index;
    const pd = pointData[idx];
    if (!pd || !pd.arxiv_id) return;

    // Find matching row in the table for this variant
    const tbody = document.querySelector(
      ".leaderboard-section[data-variant='" + slug + "'] .result-table tbody"
    );
    if (!tbody) return;

    tbody.querySelectorAll("tr").forEach(function (row) {
      if (row.dataset.arxiv === pd.arxiv_id && row.dataset.model === pd.model) {
        row.classList.add("chart-hover-highlight");
        row.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
    });
  }

  /* ── Table → Chart hover sync ───────────────────────────────────────── */
  function _initTableHover() {
    document.querySelectorAll(".result-table tbody tr").forEach(function (row) {
      row.addEventListener("mouseenter", function () {
        const slug = row.closest(".leaderboard-section")
          ? row.closest(".leaderboard-section").dataset.variant
          : null;
        if (!slug || !charts[slug]) return;
        const arxivId = row.dataset.arxiv;
        const model   = row.dataset.model;
        const chart   = charts[slug];
        const pointData = chart.data.datasets[0]._pointData || [];
        const idx = pointData.findIndex(function (pd) {
          return pd.arxiv_id === arxivId && pd.model === model;
        });
        if (idx < 0) return;

        // Draw a "yellow ring" on the matching point
        const meta = chart.getDatasetMeta(0);
        if (meta && meta.data[idx]) {
          meta.data[idx].options = Object.assign({}, meta.data[idx].options, {
            borderColor: "#fbbf24",
            borderWidth: 3,
          });
          chart.update("none");
        }
      });

      row.addEventListener("mouseleave", function () {
        const slug = row.closest(".leaderboard-section")
          ? row.closest(".leaderboard-section").dataset.variant
          : null;
        if (slug && charts[slug]) {
          charts[slug].update("none");
        }
      });
    });
  }

  /* ── Column sorting ─────────────────────────────────────────────────── */
  function _initSortableColumns() {
    document.querySelectorAll(".result-table thead th.sortable-col").forEach(function (th) {
      th.style.cursor = "pointer";
      th.addEventListener("click", function () {
        const col = th.dataset.col;
        const table = th.closest("table");
        _sortTable(table, col, th);
      });
    });
  }

  function _sortTable(table, col, th) {
    const tbody = table.querySelector("tbody");
    const rows  = Array.from(tbody.querySelectorAll("tr"));

    // Determine sort direction
    const asc = th.dataset.sortDir !== "asc";
    th.dataset.sortDir = asc ? "asc" : "desc";

    // Reset other headers
    table.querySelectorAll("th.sortable-col").forEach(function (h) {
      if (h !== th) delete h.dataset.sortDir;
      h.classList.remove("sort-asc", "sort-desc");
    });
    th.classList.add(asc ? "sort-asc" : "sort-desc");

    rows.sort(function (a, b) {
      const aVal = _cellValue(a, col);
      const bVal = _cellValue(b, col);
      if (typeof aVal === "number" && typeof bVal === "number") {
        return asc ? aVal - bVal : bVal - aVal;
      }
      const cmp = String(aVal).localeCompare(String(bVal));
      return asc ? cmp : -cmp;
    });

    rows.forEach(function (row) { tbody.appendChild(row); });
    _rerank();
  }

  function _cellValue(row, col) {
    const raw = row.dataset[col];
    if (raw === "" || raw === null || raw === undefined) return asc ? Infinity : -Infinity;
    const num = parseFloat(raw);
    return isNaN(num) ? raw : num;
  }

  /* ── Public API ─────────────────────────────────────────────────────── */
  window.leaderboard = {
    init: init,
    switchVariant: switchVariant,
    toggleStd: toggleStd,
    toggleBaselines: toggleBaselines,
  };

  // Auto-init if config is present
  document.addEventListener("DOMContentLoaded", function () {
    if (window.leaderboardConfig) {
      init();
      _initTableHover();
    }
  });
})();

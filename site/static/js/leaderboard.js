/**
 * leaderboard.js
 *
 * Handles:
 *  - Chart.js best-over-time STEP chart per dataset variant
 *  - Table column sorting
 *  - Show/hide std error bars
 *  - Show/hide baseline rows
 *  - Hover sync between chart dots and table rows (yellow ring / row highlight)
 *  - Dataset variant anchor navigation
 */
(function () {
  "use strict";

  /* ── State ─────────────────────────────────────────────────────────── */
  const charts = {};           // variant slug -> Chart instance
  let showStd = true;
  let showBaselines = true;
  let showSecondaryMetrics = false;
  let showExternalData = true;
  let showNoCode = true;
  let activeVariant = null;

  const TRADITIONAL_ARCH_TYPES = {
    svm_kernel: true,
    random_forest: true,
    decision_tree: true,
    boosting: true,
    other_traditional: true,
  };

  const archFilters = {
    gnn: true,
    hybrid: true,
    graph_transformer: true,
    llm: true,
    traditional: true,
  };

  function _chartCssVar(name, fallback) {
    var value = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    return value || fallback;
  }

  function _chartTheme() {
    return {
      tick: _chartCssVar("--chart-tick", "#1f2937"),
      grid: _chartCssVar("--chart-grid", "rgba(31,41,55,0.12)"),
      labelBg: _chartCssVar("--chart-label-bg", "rgba(255,255,255,0.88)"),
      blue: _chartCssVar("--blue", "#2563eb"),
    };
  }

  function _refreshChartsForColorScheme() {
    Object.values(charts).forEach(function (chart) { chart.update("none"); });
  }

  /* ── Init ───────────────────────────────────────────────────────────── */
  function init() {
    const cfg = window.leaderboardConfig || {};
    const variants = cfg.variants || [];
    const showAllVariants = !!cfg.showAllVariants;

    variants.forEach(function (v) {
      const canvas = document.getElementById("chart-" + v.slug);
      if (canvas) {
        buildChart(canvas, v.slug, cfg.higherIsBetter !== false);
      }
    });

    _initSortableColumns();
    _initTableExpanders();
    _initMobileRowDetails();

    _initChartStdToggles();
    _initFilterBar();

    // Set initial active variant (first standard one)
    const standard = variants.find(function (v) { return v.is_standard; }) || variants[0];
    if (standard && !showAllVariants) {
      activeVariant = standard.slug;
      switchVariant(activeVariant);
    } else if (showAllVariants) {
      document.querySelectorAll(".variant-section").forEach(function (el) {
        el.style.display = "";
      });
    }

    _applyModelColumnWidths();
    _applyModelTooltips();
    window.addEventListener("resize", _applyModelColumnWidths);
    window.addEventListener("resize", _applyModelTooltips);
    window.addEventListener("resize", function () {
      Object.values(charts).forEach(_positionChartStdToggle);
    });

    window.addEventListener("sitethemechange", _refreshChartsForColorScheme);
  }

  /* ── Variant switching ──────────────────────────────────────────────── */
  function switchVariant(slug) {
    activeVariant = slug;
    document.querySelectorAll(".variant-section").forEach(function (el) {
      el.style.display = el.dataset.variant === slug ? "" : "none";
    });
    _applyModelColumnWidths();
    _applyModelTooltips();
  }

  /* ── Std toggle ─────────────────────────────────────────────────────── */
  function toggleStd(enabled) {
    showStd = !!enabled;
    _syncChartStdToggle(showStd);
    // Re-render all charts so the error bars plugin shows/hides
    Object.values(charts).forEach(function (chart) { chart.update("none"); });
    _applyModelColumnWidths();
    _applyModelTooltips();
  }

  function _syncChartStdToggle(isOn) {
    document.querySelectorAll(".chart-std-toggle").forEach(function (btn) {
      btn.classList.toggle("is-on", !!isOn);
      btn.setAttribute("aria-pressed", isOn ? "true" : "false");
    });
  }

  function _positionChartStdToggle(chart) {
    if (!chart || !chart.canvas || !chart.chartArea) return;
    var canvas = chart.canvas;
    var wrap = canvas.closest(".chart-plot-wrap");
    var btn = wrap ? wrap.querySelector(".chart-std-toggle") : null;
    if (!btn) return;

    var area = chart.chartArea;
    var scaleX = canvas.offsetWidth / chart.width;
    var scaleY = canvas.offsetHeight / chart.height;
    var inset = 8;
    var lower = wrap.classList.contains("chart-plot-wrap-lower-is-better");

    btn.style.top = area.top * scaleY + inset + "px";
    if (lower) {
      btn.style.left = "auto";
      btn.style.right = (chart.width - area.right) * scaleX + inset + "px";
    } else {
      btn.style.right = "auto";
      btn.style.left = area.left * scaleX + inset + "px";
    }
  }

  function _initChartStdToggles() {
    document.querySelectorAll(".chart-std-toggle").forEach(function (btn) {
      if (btn.dataset.stdToggleBound) return;
      btn.dataset.stdToggleBound = "1";
      btn.addEventListener("click", function () {
        toggleStd(!btn.classList.contains("is-on"));
      });
    });
    _syncChartStdToggle(showStd);
  }

  /* ── Secondary-metrics toggle ─────────────────────────────────────── */
  function toggleSecondaryMetrics(enabled) {
    showSecondaryMetrics = !!enabled;
    _syncFilterButton("secondary-metrics", showSecondaryMetrics);
    document.querySelectorAll(".result-table").forEach(function (table) {
      table.querySelectorAll(".secondary-metrics").forEach(function (block) {
        block.hidden = !showSecondaryMetrics;
        block.classList.toggle("is-visible", showSecondaryMetrics);
      });
    });
    document.querySelectorAll(".chart-hover-preview").forEach(function (preview) {
      preview.querySelectorAll(".secondary-metrics").forEach(function (block) {
        block.hidden = !showSecondaryMetrics;
        block.classList.toggle("is-visible", showSecondaryMetrics);
      });
    });
    _applyModelColumnWidths();
    _applyModelTooltips();
  }

  /* ── Baseline toggle ────────────────────────────────────────────────── */
  function toggleBaselines(enabled) {
    showBaselines = !!enabled;
    _syncFilterButton("baselines", showBaselines);
    _applyRowFilters();
  }

  function _architectureFilterKey(archType) {
    if (!archType) return null;
    if (archType === "gnn" || archType === "hybrid" || archType === "graph_transformer" || archType === "llm") {
      return archType;
    }
    if (TRADITIONAL_ARCH_TYPES[archType]) return "traditional";
    return null;
  }

  function _rowPassesFilters(row) {
    if (!row) return true;
    if (!showBaselines && row.classList.contains("row-baseline") && !_isSotaBaselineRow(row)) {
      return false;
    }
    if (!showExternalData && row.dataset.externalData === "1") {
      return false;
    }
    if (!showNoCode && row.dataset.hasCode === "0") {
      return false;
    }
    var archKey = _architectureFilterKey(row.dataset.architecture || "");
    if (archKey && !archFilters[archKey]) {
      return false;
    }
    return true;
  }

  function _datumPassesFilters(datum) {
    if (!datum) return false;
    if (!showBaselines && datum.is_baseline && !datum._isRecord && !datum._isSotaMatch) {
      return false;
    }
    if (!showExternalData && datum.uses_external_data === true) {
      return false;
    }
    if (!showNoCode && !datum.has_code) {
      return false;
    }
    var archKey = _architectureFilterKey(datum.architecture_type || "");
    if (archKey && !archFilters[archKey]) {
      return false;
    }
    return true;
  }

  function _syncFilterButton(name, isOn) {
    document.querySelectorAll(".filter-bubble[data-filter='" + name + "']").forEach(function (btn) {
      btn.classList.toggle("is-on", !!isOn);
      btn.setAttribute("aria-pressed", isOn ? "true" : "false");
    });
  }

  function _syncArchFilterButton(name, isOn) {
    document.querySelectorAll(".filter-bubble[data-filter-arch='" + name + "']").forEach(function (btn) {
      btn.classList.toggle("is-on", !!isOn);
      btn.setAttribute("aria-pressed", isOn ? "true" : "false");
    });
  }

  function _applyRowFilters() {
    document.querySelectorAll(".result-table").forEach(function (table) {
      _syncTableRows(table);
    });
    Object.values(charts).forEach(function (chart) {
      _applyChartFilters(chart);
      chart.update("none");
    });
  }

  function _initFilterBar() {
    if (!document.querySelector(".leaderboard-filter-bar")) return;

    document.querySelectorAll(".leaderboard-filter-bar .filter-bubble[data-filter]").forEach(function (btn) {
      if (btn.dataset.filterBound) return;
      btn.dataset.filterBound = "1";
      var key = btn.getAttribute("data-filter");
      btn.addEventListener("click", function () {
        var nextOn = !btn.classList.contains("is-on");
        if (key === "baselines") {
          toggleBaselines(nextOn);
        } else if (key === "secondary-metrics") {
          toggleSecondaryMetrics(nextOn);
        } else if (key === "ext-data") {
          showExternalData = nextOn;
          _syncFilterButton("ext-data", showExternalData);
          _applyRowFilters();
        } else if (key === "no-code") {
          showNoCode = nextOn;
          _syncFilterButton("no-code", showNoCode);
          _applyRowFilters();
        }
      });
    });

    document.querySelectorAll(".leaderboard-filter-bar .filter-bubble[data-filter-arch]").forEach(function (btn) {
      if (btn.dataset.archFilterBound) return;
      btn.dataset.archFilterBound = "1";
      var archKey = btn.getAttribute("data-filter-arch");
      btn.addEventListener("click", function () {
        var nextOn = !btn.classList.contains("is-on");
        archFilters[archKey] = nextOn;
        _syncArchFilterButton(archKey, nextOn);
        _applyRowFilters();
      });
    });

    _syncFilterButton("baselines", showBaselines);
    _syncFilterButton("secondary-metrics", showSecondaryMetrics);
    _syncFilterButton("ext-data", showExternalData);
    _syncFilterButton("no-code", showNoCode);
    Object.keys(archFilters).forEach(function (key) {
      _syncArchFilterButton(key, archFilters[key]);
    });
    document.querySelectorAll(".filter-bubble[data-filter-arch][data-arch-count]").forEach(_formatArchFilterLabel);
  }

  function _formatMetricValue(value) {
    return typeof value === "number" && isFinite(value) ? value.toPrecision(2) : String(value);
  }

  function _truncateTitle(title) {
    var text = String(title || "").trim().replace(/\s+/g, " ");
    if (!text) return "";
    return text.length > 72 ? text.slice(0, 69) + "..." : text;
  }

  function _selectionMatches(selection, datum) {
    return !!selection && !!datum && selection.arxiv_id === datum.arxiv_id && selection.model === datum.model;
  }

  function _clearRowHighlights(className) {
    document.querySelectorAll("tr." + className).forEach(function (row) {
      row.classList.remove(className);
    });
  }

  function _findRowForDatum(slug, datum) {
    if (!datum || !datum.arxiv_id) return null;
    var tbody = document.querySelector(
      ".leaderboard-section[data-variant='" + slug + "'] .result-table tbody"
    );
    if (!tbody) return null;
    var rows = Array.from(tbody.querySelectorAll("tr"));
    return rows.find(function (row) {
      return row.dataset.arxiv === datum.arxiv_id && row.dataset.model === datum.model;
    }) || null;
  }

  function _selectionFromDatum(slug, datum, datasetIndex, index) {
    if (!datum) return null;
    return {
      datasetIndex: datasetIndex,
      index: index,
      arxiv_id: datum.arxiv_id || "",
      model: datum.model || "",
      row: _findRowForDatum(slug, datum),
    };
  }

  function _selectionFromElement(slug, chart, element) {
    if (!chart || !element) return null;
    var dataset = chart.data.datasets[element.datasetIndex];
    var data = dataset && dataset.data ? dataset.data : [];
    return _selectionFromDatum(slug, data[element.index], element.datasetIndex, element.index);
  }

  function _syncPinnedHighlight(chart) {
    _clearRowHighlights("chart-pinned-highlight");
    if (chart && chart._pinnedSelection && chart._pinnedSelection.row) {
      chart._pinnedSelection.row.classList.add("chart-pinned-highlight");
    }
  }

  function _formatArchFilterLabel(btn) {
    var key = btn.getAttribute("data-filter-arch");
    var labels = {
      gnn: "GNN",
      hybrid: "Hyb",
      graph_transformer: "GT",
      llm: "LLM",
      traditional: "Trad",
    };
    var count = btn.getAttribute("data-arch-count");
    if (count == null || count === "") return;
    btn.textContent = (labels[key] || key) + " (" + count + ")";
  }

  function _buildPreviewRowHtml(row) {
    if (!row) return "";
    var clone = row.cloneNode(true);
    clone.classList.remove(
      "row-collapsed",
      "chart-hover-highlight",
      "chart-pinned-highlight",
      "chart-scroll-highlight"
    );
    clone.removeAttribute("style");
    clone.querySelectorAll(".mobile-details-toggle").forEach(function (el) {
      el.remove();
    });
    var secondary = clone.querySelector(".secondary-metrics");
    if (secondary) {
      if (showSecondaryMetrics) {
        secondary.hidden = false;
        secondary.classList.add("is-visible");
      } else {
        secondary.hidden = true;
        secondary.classList.remove("is-visible");
      }
    }
    return "<table class=\"result-table chart-preview-table\"><tbody>" + clone.outerHTML + "</tbody></table>";
  }

  function _updatePreview(slug, chart) {
    var preview = document.getElementById("hover-preview-" + slug);
    if (!preview) return;

    var selection = chart && chart._pinnedSelection ? chart._pinnedSelection : (chart ? chart._lastHoverSelection : null);
    if (!selection || !selection.row) {
      preview.style.display = "none";
      preview.classList.remove("is-pinned");
      preview.innerHTML = "";
      return;
    }

    var isPinned = !!(chart && chart._pinnedSelection);
    var rowHtml = _buildPreviewRowHtml(selection.row);
    if (!rowHtml) {
      preview.style.display = "none";
      preview.classList.remove("is-pinned");
      preview.innerHTML = "";
      return;
    }

    var label = isPinned ? "Pinned" : "Hovered";
    var actions = "";
    if (isPinned) {
      actions = "<div class='preview-actions'>" +
        "<button type='button' class='preview-action-btn preview-scroll-btn'>Scroll to row</button>" +
        "<button type='button' class='preview-action-btn preview-unpin-btn'>Unpin</button>" +
        "</div>";
    }

    preview.classList.toggle("is-pinned", isPinned);
    preview.innerHTML = "<div class='preview-top'>" +
      "<span class='preview-label'>" + label + "</span>" +
      actions +
      "</div><div class='chart-preview-row-wrap'>" + rowHtml + "</div>";
    preview.style.display = "block";

    if (isPinned) {
      var scrollBtn = preview.querySelector(".preview-scroll-btn");
      if (scrollBtn) {
        scrollBtn.addEventListener("click", function () {
          _scrollToRow(selection.row);
        });
      }
      var unpinBtn = preview.querySelector(".preview-unpin-btn");
      if (unpinBtn) {
        unpinBtn.addEventListener("click", function () {
          if (!chart) return;
          chart._pinnedSelection = null;
          _syncPinnedHighlight(chart);
          _updatePreview(slug, chart);
        });
      }
    }
  }

  function _scrollToRow(row) {
    if (!row) return;
    if (row.classList.contains("row-collapsed") || row.style.display === "none") {
      var table = row.closest("table");
      var selector = table && table.id ? "#" + table.id : null;
      var moreBtn = selector ? document.querySelector("button[data-table-more='" + selector + "']") : null;
      if (moreBtn && moreBtn.getAttribute("data-expanded") !== "true") {
        moreBtn.click();
      }
    }
    row.scrollIntoView({ behavior: "smooth", block: "center" });
    row.classList.add("chart-scroll-highlight");
    window.setTimeout(function () {
      row.classList.remove("chart-scroll-highlight");
    }, 1600);
  }

  function _normalizeModelFamily(name) {
    var raw = String(name || "").trim().toLowerCase();
    if (raw === "gcn") return "gcn";
    if (raw === "gin") return "gin";
    if (raw === "graphsage") return "graphsage";
    if (raw === "mlp") return "mlp";
    return "";
  }

  function _pickBestReference(rows, higherIsBetter, families) {
    var wanted = Array.isArray(families) ? families : [families];
    var best = null;
    rows.forEach(function (row) {
      var family = _normalizeModelFamily(row.model_plain || row.model);
      var value = row.metric_values && row.metric_values[0];
      if (wanted.indexOf(family) === -1 || value == null) return;
      if (!best || (higherIsBetter ? value > best.value : value < best.value)) {
        best = {
          family: family,
          label: row.model_plain || row.model,
          value: value,
        };
      }
    });
    return best;
  }

  function _quantile(sortedNums, q) {
    if (!sortedNums || !sortedNums.length) return null;
    var qq = Math.max(0, Math.min(1, q));
    var idx = Math.floor(qq * (sortedNums.length - 1));
    return sortedNums[idx];
  }

  function _computeFocusedYBounds(scatterData, recordData, refs, higherIsBetter) {
    var allVals = (scatterData || []).map(function (d) { return d && d.y; }).filter(function (v) {
      return typeof v === "number" && isFinite(v);
    }).sort(function (a, b) { return a - b; });

    var focusVals = [];
    (recordData || []).forEach(function (d) {
      if (d && d._isRecord && typeof d.y === "number" && isFinite(d.y)) focusVals.push(d.y);
    });
    (refs || []).forEach(function (ref) {
      if (ref && typeof ref.value === "number" && isFinite(ref.value)) focusVals.push(ref.value);
    });

    if (!allVals.length && !focusVals.length) return null;
    if (!focusVals.length) focusVals = allVals.slice();

    var focusMin = Math.min.apply(null, focusVals);
    var focusMax = Math.max.apply(null, focusVals);

    var badSide = higherIsBetter
      ? _quantile(allVals, 0.28)
      : _quantile(allVals, 0.72);
    var goodTail = higherIsBetter
      ? _quantile(allVals, 0.97)
      : _quantile(allVals, 0.03);

    var yMin;
    var yMax;
    if (higherIsBetter) {
      yMin = Math.min(focusMin, badSide == null ? focusMin : badSide);
      yMax = Math.max(focusMax, goodTail == null ? focusMax : goodTail);
    } else {
      yMin = Math.min(focusMin, goodTail == null ? focusMin : goodTail);
      yMax = Math.max(focusMax, badSide == null ? focusMax : badSide);
    }

    var span = yMax - yMin;
    var base = Math.max(Math.abs(focusMin), Math.abs(focusMax), 1);
    var pad = span > 1e-9 ? span * 0.09 : base * 0.02;

    var isUnitScale = allVals.length && allVals.every(function (v) { return v >= 0 && v <= 1; });
    if (higherIsBetter && isUnitScale && refs && refs.length) {
      var minRef = Math.min.apply(null, refs.map(function (ref) { return ref.value; }));
      yMin = Math.max(yMin, Math.max(0, minRef - 0.07));
      span = yMax - yMin;
      pad = span > 1e-9 ? span * 0.09 : base * 0.02;
    }

    return {
      min: yMin - pad,
      max: yMax + pad,
    };
  }

  function _isWithinYBounds(value, bounds) {
    return !!bounds && typeof value === "number" && isFinite(value) &&
      value >= bounds.min && value <= bounds.max;
  }

  function _semanticPointColors(datum) {
    if (datum && datum._isRecord) {
      return {
        fill: "#2563eb",
        stroke: "rgba(37,99,235,0.9)",
        error: "rgba(37,99,235,0.95)",
      };
    }
    if (datum && datum._isSotaMatch) {
      return {
        fill: "#d97706",
        stroke: "rgba(180,83,9,0.95)",
        error: "rgba(180,83,9,0.95)",
      };
    }
    if (datum && !datum.is_baseline) {
      return {
        fill: "rgba(107,114,128,0.68)",
        stroke: "rgba(75,85,99,0.9)",
        error: "rgba(75,85,99,0.82)",
      };
    }
    return {
      fill: "rgba(209,213,219,0.78)",
      stroke: "rgba(156,163,175,0.9)",
      error: "rgba(156,163,175,0.78)",
    };
  }

  function _scatterPriority(datum) {
    if (!datum) return 0;
    if (datum._isRecord) return 3;
    if (datum._isSotaMatch) return 2;
    if (!datum.is_baseline) return 1;
    return 0;
  }

  function _sortScatterByPriority(data) {
    return (data || []).slice().sort(function (a, b) {
      var pa = _scatterPriority(a);
      var pb = _scatterPriority(b);
      if (pa !== pb) return pa - pb;
      if (a.x !== b.x) return a.x - b.x;
      return a.y - b.y;
    });
  }

  function _stdIntervalsOverlap(aValue, aStd, bValue, bStd) {
    if (aValue == null || bValue == null || aStd == null || bStd == null) return false;
    var aMin = aValue - aStd;
    var aMax = aValue + aStd;
    var bMin = bValue - bStd;
    var bMax = bValue + bStd;
    return aMin <= bMax && bMin <= aMax;
  }

  function _decorateHistoricalSotaRows(slug, scatterData) {
    var tbody = document.querySelector(".leaderboard-section[data-variant='" + slug + "'] .result-table tbody");
    if (!tbody) return;

    Array.from(tbody.querySelectorAll("tr")).forEach(function (row) {
      row.classList.remove("row-historical-record");
      row.classList.remove("row-historical-sota-match");
    });

    (scatterData || []).forEach(function (datum) {
      if (!datum) return;
      var row = _findRowForDatum(slug, datum);
      if (!row) return;
      if (datum._isRecord) {
        row.classList.add("row-historical-record");
      } else if (datum._isSotaMatch) {
        row.classList.add("row-historical-sota-match");
      }
    });
  }

  function _applyChartFilters(chart) {
    if (!chart || !chart._scatterAll || !chart._recordAll) return;
    var yBounds = chart._yBounds || null;
    var visibleScatter = chart._scatterAll.filter(function (d) {
      if (!_isWithinYBounds(d.y, yBounds)) return false;
      if (d._isStdOutlier && !d._isRecord) return false;
      return _datumPassesFilters(d);
    });
    visibleScatter = _sortScatterByPriority(visibleScatter);
    var visibleRecord = chart._recordAll.filter(function (d) {
      return _isWithinYBounds(d.y, yBounds);
    });

    chart.data.datasets[0].data = visibleScatter;
    chart.data.datasets[1].data = visibleRecord;

    chart.data.datasets[0].pointBackgroundColor = visibleScatter.map(function (d) {
      return _semanticPointColors(d).fill;
    });
    chart.data.datasets[0].borderColor = visibleScatter.map(function (d) {
      return _semanticPointColors(d).stroke;
    });
    chart.data.datasets[0].pointHoverBackgroundColor = visibleScatter.map(function (d) {
      return _semanticPointColors(d).fill;
    });
    chart.data.datasets[0].pointHoverBorderColor = visibleScatter.map(function (d) {
      return _semanticPointColors(d).stroke;
    });

    chart.data.datasets[1].pointBackgroundColor = visibleRecord.map(function (d) {
      return d && d._isRecord ? "#2563eb" : "transparent";
    });
    chart.data.datasets[1].pointRadius = visibleRecord.map(function (d) {
      return d && d._isRecord ? 7 : 0;
    });

    if (chart._highlightedPoint) {
      var h = chart._highlightedPoint;
      var ds = chart.data.datasets[h.datasetIndex];
      var currentLen = ds && ds.data ? ds.data.length : 0;
      if (!ds || h.index < 0 || h.index >= currentLen) {
        chart._highlightedPoint = null;
        if (chart.setActiveElements) chart.setActiveElements([]);
      }
    }

    if (chart._pinnedSelection) {
      var visiblePinned = chart.data.datasets.some(function (dataset) {
        var data = dataset && dataset.data ? dataset.data : [];
        return data.some(function (datum) { return _selectionMatches(chart._pinnedSelection, datum); });
      });
      if (!visiblePinned) {
        chart._pinnedSelection = null;
      }
      _syncPinnedHighlight(chart);
      if (chart._slug) _updatePreview(chart._slug, chart);
    }
  }

  function _isSotaBaselineRow(row) {
    if (!row || !row.classList) return false;
    return row.classList.contains("row-best") || row.classList.contains("row-global-top");
  }

  /* ── Chart builder ──────────────────────────────────────────────────── */
  function buildChart(canvas, slug, higherIsBetter) {
    let milestones = [];
    try {
      milestones = JSON.parse(canvas.dataset.milestones || "[]");
    } catch (e) { /* ignore */ }

    const cfg = window.leaderboardConfig || {};
    const variant = (cfg.variants || []).find(function (v) { return v.slug === slug; }) || {};
    const allRows = variant.rows || [];

    if (!milestones.length && !allRows.length) return;
    if (typeof Chart === "undefined") return;

    // Parse any date string (YYYY-MM-DD, YYYY-MM, or "Jun 2022") to UTC ms.
    function dateTs(dateStr) {
      if (!dateStr) return null;
      var isoDay = dateStr.match(/^(\d{4})-(\d{2})-(\d{2})$/);
      if (isoDay) return Date.UTC(+isoDay[1], +isoDay[2] - 1, +isoDay[3]);
      var isoMonth = dateStr.match(/^(\d{4})-(\d{2})$/);
      if (isoMonth) return Date.UTC(+isoMonth[1], +isoMonth[2] - 1, 1);
      // Formatted "Jun 2022"
      var ts = Date.parse("1 " + dateStr);
      if (!isNaN(ts)) {
        var d = new Date(ts);
        return Date.UTC(d.getFullYear(), d.getMonth(), 1);
      }
      return null;
    }

    function fmtTs(ts) {
      var d = new Date(ts);
      return d.toLocaleDateString("en-US", { month: "short", year: "numeric", timeZone: "UTC" });
    }

    var titleByArxiv = {};
    allRows.forEach(function (row) {
      if (row.arxiv_id && row.title && !titleByArxiv[row.arxiv_id]) {
        titleByArxiv[row.arxiv_id] = row.title;
      }
    });

    var gnnReference = _pickBestReference(allRows, higherIsBetter, ["gcn", "gin", "graphsage"]);
    var mlpReference = _pickBestReference(allRows, higherIsBetter, "mlp");

    var recordKeys = {};
    milestones.forEach(function (m) {
      var ts = dateTs(m.date);
      if (ts == null || m.value == null || !m.model || !m.arxiv_id) return;
      var key = [String(m.arxiv_id), String(m.model), String(ts), Number(m.value).toFixed(10)].join("|");
      recordKeys[key] = true;
    });

    var milestoneTimeline = milestones.map(function (m) {
      return {
        x: dateTs(m.date),
        y: m.value,
        std: m.std,
        arxiv_id: m.arxiv_id,
        model: m.model,
      };
    }).filter(function (m) {
      return m.x != null && typeof m.y === "number" && isFinite(m.y);
    }).sort(function (a, b) { return a.x - b.x; });

    function classifyHistoricalSota(ts, value, std, arxivId, model) {
      if (ts == null || value == null) return { isRecord: false, isSotaMatch: false };
      var activeMilestone = null;
      for (var i = 0; i < milestoneTimeline.length; i++) {
        var m = milestoneTimeline[i];
        if (m.x > ts) break;
        activeMilestone = m;
      }
      if (!activeMilestone) return { isRecord: false, isSotaMatch: false };

      var selfIsMilestone = activeMilestone.x === ts &&
        activeMilestone.arxiv_id === arxivId &&
        activeMilestone.model === model &&
        Math.abs(activeMilestone.y - value) <= 1e-9;

      if (selfIsMilestone) {
        return { isRecord: true, isSotaMatch: false };
      }

      var exactMatch = Math.abs(value - activeMilestone.y) <= 1e-9;
      var overlapMatch = _stdIntervalsOverlap(value, std, activeMilestone.y, activeMilestone.std);
      return {
        isRecord: false,
        isSotaMatch: exactMatch || overlapMatch,
      };
    }

    // ── Scatter dataset: all rows ─────────────────────────────────────
    var scatterData = [];
    var modelBaselineMap = {};
    allRows.forEach(function (row) {
      var val = row.metric_values && row.metric_values[0];
      var std = row.metric_stds && row.metric_stds[0];
      var ts = dateTs(row.date_iso || row.date);
      if (val == null || ts == null) return;
      modelBaselineMap[row.model] = !!row.is_baseline;
      var key = [String(row.arxiv_id || ""), String(row.model || ""), String(ts), Number(val).toFixed(10)].join("|");
      var historicalClass = classifyHistoricalSota(ts, val, std, row.arxiv_id || "", row.model || "");
      var isRecordPoint = !!recordKeys[key] || historicalClass.isRecord;
      var isTieSotaPoint = historicalClass.isSotaMatch;
      scatterData.push({
        x: ts, y: val,
        std: std,
        model: row.model,
        arxiv_id: row.arxiv_id,
        title: row.title || "",
        is_baseline: row.is_baseline,
        uses_external_data: row.uses_external_data === true,
        has_code: !!(row.codebase_url),
        architecture_type: row.architecture_type || "",
        _isStdOutlier: !!row.is_std_outlier,
        _isRecord: isRecordPoint,
        _isSotaMatch: isTieSotaPoint,
      });
    });

    // ── Records dataset: milestones (new bests over time) ─────────────
    var recordData = milestones.map(function (m) {
      return {
        x: dateTs(m.date),
        y: m.value,
        std: m.std,
        model: m.model,
        arxiv_id: m.arxiv_id,
        title: titleByArxiv[m.arxiv_id] || "",
        is_baseline: !!modelBaselineMap[m.model],
        _isRecord: true,
      };
    });

    // Extend step line to today so the horizontal rule reaches the right edge
    var todayTs = (function () {
      var n = new Date();
      return Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), n.getUTCDate());
    })();
    if (recordData.length > 0) {
      recordData.push({
        x: todayTs,
        y: recordData[recordData.length - 1].y,
        std: null, model: null, arxiv_id: null, _isRecord: false,
      });
    }

    // ── X axis bounds ─────────────────────────────────────────────────
    var allTs = scatterData.map(function (d) { return d.x; })
      .concat(recordData.map(function (d) { return d.x; }))
      .filter(Boolean);
    var xMin = allTs.length ? Math.min.apply(null, allTs) : todayTs;
    // Add one month of padding on each side
    var xMinPad = xMin - 30 * 24 * 3600 * 1000;
    var xMaxPad = todayTs;

    var references = [
      gnnReference ? {
        value: gnnReference.value,
        color: "rgba(15,118,110,0.9)",
        dash: [8, 4],
        label: gnnReference.label + " " + _formatMetricValue(gnnReference.value),
        position: "below",
      } : null,
      mlpReference ? {
        value: mlpReference.value,
        color: "rgba(107,114,128,0.9)",
        dash: [3, 4],
        label: mlpReference.label + " " + _formatMetricValue(mlpReference.value),
        position: "above",
      } : null,
    ].filter(Boolean);
    var focusedYBounds = _computeFocusedYBounds(scatterData, recordData, references, higherIsBetter);

    // ── Per-point styling for records line ────────────────────────────
    var recordBg = recordData.map(function (d) { return d._isRecord ? "#2563eb" : "transparent"; });
    var recordRadius = recordData.map(function (d) { return d._isRecord ? 7 : 0; });
    var visibleScatterData = scatterData.filter(function (d) {
      return _isWithinYBounds(d.y, focusedYBounds) && (!d._isStdOutlier || d._isRecord);
    });
    var visibleRecordData = recordData.filter(function (d) {
      return _isWithinYBounds(d.y, focusedYBounds);
    });

    var stdTogglePositionPlugin = {
      id: "stdTogglePosition_" + slug,
      afterLayout: function (chart) {
        _positionChartStdToggle(chart);
      },
    };

    var yearLinesPlugin = {
      id: "yearLines_" + slug,
      beforeDatasetsDraw: function (chart) {
        var x = chart.scales.x;
        if (!x) return;
        var min = x.min;
        var max = x.max;
        if (min == null || max == null) return;
        var startYear = new Date(min).getUTCFullYear();
        var endYear = new Date(max).getUTCFullYear();
        var ctx = chart.ctx;
        var area = chart.chartArea;
        ctx.save();
        ctx.strokeStyle = _chartTheme().grid;
        ctx.lineWidth = 1;
        for (var y = startYear; y <= endYear; y++) {
          var ts = Date.UTC(y, 0, 1);
          if (ts < min || ts > max) continue;
          var px = x.getPixelForValue(ts);
          ctx.beginPath();
          ctx.moveTo(px, area.top);
          ctx.lineTo(px, area.bottom);
          ctx.stroke();
        }
        ctx.restore();
      },
    };

    // ── afterDraw plugin: label each record milestone ─────────────────
    var labelPlugin = {
      id: "recordLabels_" + slug,
      afterDatasetsDraw: function (chart) {
        var meta = chart.getDatasetMeta(1);
        if (!meta || meta.hidden) return;
        var dataset = chart.data.datasets[1];
        var recordPoints = dataset && dataset.data ? dataset.data : [];
        var ctx = chart.ctx;
        ctx.save();
        ctx.font = "bold 11px sans-serif";
        ctx.textAlign = "left";
        var chartArea = chart.chartArea;
        var placedBoxes = [];
        meta.data.forEach(function (point, i) {
          var pd = recordPoints[i];
          if (!pd || !pd._isRecord || !pd.model) return;
          var label = pd.model + " " + _formatMetricValue(pd.y);
          var lx = Math.min(point.x + 5, chartArea.right - ctx.measureText(label).width - 6);
          lx = Math.max(chartArea.left + 4, lx);
          var ly = point.y - 8;
          var width = ctx.measureText(label).width;
          var height = 12;
          if (ly - height < chartArea.top + 2) {
            ly = Math.max(height + 2, chartArea.top - 6);
          }
          var guard = 0;
          while (guard < 12) {
            var overlaps = placedBoxes.some(function (box) {
              return lx < box.right && lx + width > box.left && ly - height < box.bottom && ly > box.top;
            });
            if (!overlaps) break;
            ly -= 13;
            if (ly - height < chartArea.top + 2) {
              ly = Math.min(chartArea.bottom - 4, point.y + 16 + guard * 13);
            }
            guard += 1;
          }
          ctx.fillStyle = _chartTheme().blue;
          ctx.fillText(label, lx, ly);
          placedBoxes.push({ left: lx, right: lx + width, top: ly - height, bottom: ly + 2 });
        });
        ctx.restore();
      },
    };

    // ── afterDraw plugin: draw ± std error bars ───────────────────────
    function _drawErrorBar(ctx, chartArea, px, yScale, yVal, std, color, capHalf) {
      var yHi = yScale.getPixelForValue(yVal + std);
      var yLo = yScale.getPixelForValue(yVal - std);
      if (![px, yHi, yLo].every(function (v) { return typeof v === "number" && isFinite(v); })) return;
      if (px < chartArea.left || px > chartArea.right) return;
      if (Math.max(yHi, yLo) < chartArea.top || Math.min(yHi, yLo) > chartArea.bottom) return;

      var clippedHi = Math.max(chartArea.top, Math.min(chartArea.bottom, yHi));
      var clippedLo = Math.max(chartArea.top, Math.min(chartArea.bottom, yLo));
      if (Math.abs(clippedHi - clippedLo) < 0.5) return;

      ctx.save();
      ctx.beginPath();
      ctx.rect(chartArea.left, chartArea.top, chartArea.right - chartArea.left, chartArea.bottom - chartArea.top);
      ctx.clip();
      ctx.strokeStyle = color;
      ctx.lineWidth = 1.5;
      // vertical stem
      ctx.beginPath(); ctx.moveTo(px, clippedHi); ctx.lineTo(px, clippedLo); ctx.stroke();
      // top cap
      if (yHi >= chartArea.top && yHi <= chartArea.bottom) {
        ctx.beginPath(); ctx.moveTo(px - capHalf, clippedHi); ctx.lineTo(px + capHalf, clippedHi); ctx.stroke();
      }
      // bottom cap
      if (yLo >= chartArea.top && yLo <= chartArea.bottom) {
        ctx.beginPath(); ctx.moveTo(px - capHalf, clippedLo); ctx.lineTo(px + capHalf, clippedLo); ctx.stroke();
      }
      ctx.restore();
    }

    var errorBarsPlugin = {
      id: "errorBars_" + slug,
      afterDatasetsDraw: function (chart) {
        if (!showStd) return;
        var ctx = chart.ctx;
        var yScale = chart.scales.y;
        var chartArea = chart.chartArea;
        // Scatter dataset (index 0)
        var scatterDataset = chart.data.datasets[0];
        var scatterPoints = scatterDataset && scatterDataset.data ? scatterDataset.data : [];
        var sm = chart.getDatasetMeta(0);
        if (sm && !sm.hidden) {
          sm.data.forEach(function (point, i) {
            var d = scatterPoints[i];
            if (!d || d.std == null) return;
            _drawErrorBar(ctx, chartArea, point.x, yScale, d.y, d.std, _semanticPointColors(d).error, 5);
          });
        }
        // Records dataset (index 1)
        var recordDataset = chart.data.datasets[1];
        var recordPoints = recordDataset && recordDataset.data ? recordDataset.data : [];
        var rm = chart.getDatasetMeta(1);
        if (rm && !rm.hidden) {
          rm.data.forEach(function (point, i) {
            var d = recordPoints[i];
            if (!d || !d._isRecord || d.std == null) return;
            _drawErrorBar(ctx, chartArea, point.x, yScale, d.y, d.std, "rgba(37,99,235,0.7)", 7);
          });
        }

        var hp = chart._highlightedPoint;
        if (!hp) return;
        var activeDs = chart.data.datasets[hp.datasetIndex];
        var activeMeta = chart.getDatasetMeta(hp.datasetIndex);
        if (!activeDs || !activeMeta || !activeMeta.data || !activeMeta.data[hp.index]) return;
        var activeDatum = activeDs.data[hp.index];
        if (!activeDatum || activeDatum.std == null) return;
        var activePoint = activeMeta.data[hp.index];
        _drawErrorBar(ctx, chartArea, activePoint.x, yScale, activeDatum.y, activeDatum.std, _semanticPointColors(activeDatum).error, 9);
      },
    };

    var referenceLinesPlugin = {
      id: "referenceLines_" + slug,
      afterDatasetsDraw: function (chart) {
        var refs = references;
        if (!refs.length) return;

        var ctx = chart.ctx;
        var yScale = chart.scales.y;
        var area = chart.chartArea;
        ctx.save();
        refs.forEach(function (ref) {
          var py = yScale.getPixelForValue(ref.value);
          if (!isFinite(py) || py < area.top || py > area.bottom) return;
          ctx.save();
          ctx.strokeStyle = ref.color;
          ctx.lineWidth = 1.25;
          ctx.setLineDash(ref.dash);
          ctx.beginPath();
          ctx.moveTo(area.left, py);
          ctx.lineTo(area.right, py);
          ctx.stroke();
          ctx.restore();
        });
        ctx.restore();
      },
    };

    var referenceLabelsPlugin = {
      id: "referenceLabels_" + slug,
      afterDatasetsDraw: function (chart) {
        var refs = references;
        if (!refs.length) return;

        var ctx = chart.ctx;
        var yScale = chart.scales.y;
        var area = chart.chartArea;
        ctx.save();
        ctx.font = "600 11px sans-serif";
        var refsByValue = refs.slice().sort(function (a, b) { return b.value - a.value; });
        refs.forEach(function (ref) {
          var py = yScale.getPixelForValue(ref.value);
          if (!isFinite(py) || py < area.top || py > area.bottom) return;
          var textWidth = ctx.measureText(ref.label).width;
          var labelX = Math.max(area.left + 8, area.right - textWidth - 12);
          var order = refsByValue.findIndex(function (candidate) { return candidate === ref; });
          var offset = order <= 0 ? -6 : 16 + (order - 1) * 14;
          var unclampedY = py + offset;
          var labelY = Math.min(area.bottom - 4, Math.max(area.top + 12, unclampedY));
          ctx.fillStyle = _chartTheme().labelBg;
          ctx.fillRect(labelX - 4, labelY - 10, textWidth + 8, 14);
          ctx.fillStyle = ref.color;
          ctx.fillText(ref.label, labelX, labelY);
        });
        ctx.restore();
      },
    };

    var chart = new Chart(canvas, {
      type: "scatter",
      data: {
        datasets: [
          {
            label: "All results",
            data: visibleScatterData,
            type: "scatter",
            backgroundColor: visibleScatterData.map(function (d) {
              return _semanticPointColors(d).fill;
            }),
            borderColor: visibleScatterData.map(function (d) {
              return _semanticPointColors(d).stroke;
            }),
            pointRadius: 4,
            pointHoverRadius: 7,
            pointHoverBackgroundColor: visibleScatterData.map(function (d) {
              return _semanticPointColors(d).fill;
            }),
            pointHoverBorderColor: visibleScatterData.map(function (d) {
              return _semanticPointColors(d).stroke;
            }),
            pointHoverBorderWidth: 2,
            order: 2,
          },
          {
            label: "Record",
            data: visibleRecordData,
            type: "line",
            stepped: "before",
            borderColor: "#2563eb",
            backgroundColor: "rgba(37,99,235,0.07)",
            pointBackgroundColor: recordBg,
            pointRadius: recordRadius,
            pointHoverRadius: 10,
            tension: 0,
            fill: false,
            order: 1,
          },
        ],
      },
      options: {
        responsive: true,
        interaction: { mode: "nearest", intersect: true },
        plugins: {
          tooltip: { enabled: false },
          legend: { display: false },
        },
        scales: {
          x: {
            type: "linear",
            min: xMinPad,
            max: xMaxPad,
            title: { display: true, text: "Date", color: _chartTheme().tick },
            grid: { color: _chartTheme().grid },
            afterBuildTicks: function (scale) {
              var min = scale.min;
              var max = scale.max;
              if (min == null || max == null) return;
              var startYear = new Date(min).getUTCFullYear();
              var endYear = new Date(max).getUTCFullYear();
              var ticks = [];
              for (var y = startYear; y <= endYear; y++) {
                var tickValue = Date.UTC(y, 0, 1);
                // Only add tick if it's actually within the data range [min, max]
                if (tickValue >= min && tickValue <= max) {
                  ticks.push({ value: tickValue });
                }
              }
              scale.ticks = ticks;
            },
            ticks: {
              color: _chartTheme().tick,
              callback: function (value) {
                return String(new Date(value).getUTCFullYear());
              },
            },
          },
          y: {
            min: focusedYBounds ? focusedYBounds.min : undefined,
            max: focusedYBounds ? focusedYBounds.max : undefined,
            title: { display: true, text: canvas.dataset.metric || "Score", color: _chartTheme().tick },
            ticks: { precision: 4, color: _chartTheme().tick },
            grid: { color: _chartTheme().grid },
          },
        },
        onHover: function (event, elements) {
          _onChartHover(slug, elements, chart);
        },
        onClick: function (event, elements) {
          _onChartClick(slug, elements, chart);
        },
      },
      plugins: [
        stdTogglePositionPlugin,
        yearLinesPlugin,
        referenceLinesPlugin,
        errorBarsPlugin,
        referenceLabelsPlugin,
        labelPlugin,
      ],
    });

    chart._scatterAll = scatterData.slice();
    chart._recordAll = recordData.slice();
    chart._yBounds = focusedYBounds;
    chart._slug = slug;
    _decorateHistoricalSotaRows(slug, scatterData);
    _applyChartFilters(chart);
    chart.update("none");

    charts[slug] = chart;
  }

  /* ── Chart → Table hover sync ───────────────────────────────────────── */
  function _onChartHover(slug, elements, chart) {
    function setHoveredPoint(nextPoint) {
      var cur = chart._highlightedPoint;
      var changed = !cur || !nextPoint || cur.datasetIndex !== nextPoint.datasetIndex || cur.index !== nextPoint.index;
      if (changed) {
        chart._highlightedPoint = nextPoint;
        chart.update("none");
      }
    }

    _clearRowHighlights("chart-hover-highlight");

    if (!elements.length) {
      chart._lastHoverSelection = null;
      setHoveredPoint(null);
      _updatePreview(slug, chart);
      return;
    }

    setHoveredPoint({ datasetIndex: elements[0].datasetIndex, index: elements[0].index });
    var selection = _selectionFromElement(slug, chart, elements[0]);
    chart._lastHoverSelection = selection;
    if (!selection || !selection.row) {
      _updatePreview(slug, chart);
      return;
    }
    selection.row.classList.add("chart-hover-highlight");
    _updatePreview(slug, chart);
  }

  function _onChartClick(slug, elements, chart) {
    if (!elements.length) return;
    var selection = _selectionFromElement(slug, chart, elements[0]);
    if (!selection || !selection.row) return;

    if (_selectionMatches(chart._pinnedSelection, selection)) {
      chart._pinnedSelection = null;
    } else {
      chart._pinnedSelection = selection;
    }
    _syncPinnedHighlight(chart);
    _updatePreview(slug, chart);
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
        const pointData = chart.data.datasets[0].data || [];
        const idx = pointData.findIndex(function (pd) {
          return pd.arxiv_id === arxivId && pd.model === model;
        });
        if (idx < 0) return;

        chart._highlightedPoint = { datasetIndex: 0, index: idx };
        if (chart.setActiveElements) {
          chart.setActiveElements([{ datasetIndex: 0, index: idx }]);
        }
        chart.update("none");
      });

      row.addEventListener("mouseleave", function () {
        const slug = row.closest(".leaderboard-section")
          ? row.closest(".leaderboard-section").dataset.variant
          : null;
        if (slug && charts[slug]) {
          charts[slug]._highlightedPoint = null;
          if (charts[slug].setActiveElements) charts[slug].setActiveElements([]);
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
      if (aVal === null && bVal === null) return 0;
      if (aVal === null) return 1;
      if (bVal === null) return -1;
      if (typeof aVal === "number" && typeof bVal === "number") {
        return asc ? aVal - bVal : bVal - aVal;
      }
      const cmp = String(aVal).localeCompare(String(bVal));
      return asc ? cmp : -cmp;
    });

    rows.forEach(function (row) { tbody.appendChild(row); });
    _syncTableRows(table);
  }

  function _initMobileRowDetails() {
    function toggleRow(row, btn) {
      if (!row || !btn) return;
      var nextExpanded = !row.classList.contains("mobile-details-open");
      row.classList.toggle("mobile-details-open", nextExpanded);
      btn.setAttribute("aria-expanded", nextExpanded ? "true" : "false");
    }

    document.querySelectorAll(".mobile-details-toggle").forEach(function (btn) {
      btn.addEventListener("click", function (event) {
        event.stopPropagation(); // prevent the row handler from double-firing
        var row = btn.closest("tr");
        toggleRow(row, btn);
      });
    });

    document.querySelectorAll(".result-table tbody tr.result-row").forEach(function (row) {
      row.addEventListener("click", function (event) {
        if (event.target.closest("a")) return; // let link clicks through
        var btn = row.querySelector(".mobile-details-toggle");
        if (!btn) return; // no toggle = desktop or no paper column
        toggleRow(row, btn);
      });
    });
  }

  function _cellValue(row, col) {
    const raw = row.dataset[col];
    if (raw === "" || raw === null || raw === undefined) return null;
    if (col === "date") {
      const isoDay = raw.match(/^(\d{4})-(\d{2})-(\d{2})$/);
      if (isoDay) return Date.UTC(+isoDay[1], +isoDay[2] - 1, +isoDay[3]);
      const isoMonth = raw.match(/^(\d{4})-(\d{2})$/);
      if (isoMonth) return Date.UTC(+isoMonth[1], +isoMonth[2] - 1, 1);
      const parsed = Date.parse("1 " + raw);
      if (!Number.isNaN(parsed)) {
        const d = new Date(parsed);
        return Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), 1);
      }
    }
    const num = parseFloat(raw);
    return isNaN(num) ? raw : num;
  }

  /* ── Wide-table toggle ──────────────────────────────────────────────── */
  var _wideTable = false;
  function toggleWideTable() {
    _wideTable = false;
    document.querySelectorAll(".result-table-wrapper").forEach(function (el) {
      el.classList.remove("wide-table-mode");
      el.style.removeProperty("--wide-table-width");
    });
    _applyModelColumnWidths();
    _applyModelTooltips();
  }

  function _percentile(sortedNums, p) {
    if (!sortedNums.length) return 0;
    var idx = Math.max(0, Math.min(sortedNums.length - 1, Math.floor(p * (sortedNums.length - 1))));
    return sortedNums[idx];
  }

  function _applyModelColumnWidths() {
    document.querySelectorAll(".result-table").forEach(function (table) {
      var wrapper = table.closest(".result-table-wrapper");
      if (!wrapper) return;

      // Calculate model column width based on 90th percentile of content
      var modelCells = Array.from(table.querySelectorAll("tbody td.col-model"));
      var modelLens = modelCells
        .map(function (td) { return (td.innerText || "").replace(/\s+/g, " ").trim().length; })
        .filter(function (n) { return n > 0; })
        .sort(function (a, b) { return a - b; });
      var modelQuantile = _wideTable ? 0.78 : 0.88;
      var modelPx = modelLens.length ? _percentile(modelLens, modelQuantile) : 0;
      var modelChars = Math.ceil(modelPx * (_wideTable ? 1.03 : 1.08));
      modelChars = Math.max(10, Math.min(_wideTable ? 18 : 20, modelChars));

      // Calculate value column width (metric values are typically short)
      var valueCells = Array.from(table.querySelectorAll("tbody td.col-value"));
      var valueChars = 10; // Default
      if (valueCells.length) {
        var valueLens = valueCells
          .map(function (td) { return (td.innerText || "").replace(/\s+/g, " ").trim().length; })
          .filter(function (n) { return n > 0; })
          .sort(function (a, b) { return a - b; });
        if (valueLens.length) {
          var vp90 = _percentile(valueLens, 0.9);
          valueChars = Math.max(8, Math.min(_wideTable ? 11 : 10, Math.ceil(vp90 * 1.05 + 1)));
        }
      }

      var paperCells = Array.from(table.querySelectorAll("tbody td.col-paper"));
      var paperLens = paperCells
        .map(function (td) { return (td.innerText || "").replace(/\s+/g, " ").trim().length; })
        .filter(function (n) { return n > 0; })
        .sort(function (a, b) { return a - b; });
      var paperChars = 30;
      if (paperLens.length) {
        var pp90 = _percentile(paperLens, 0.9);
        paperChars = Math.max(24, Math.min(_wideTable ? 60 : 38, Math.ceil(pp90 * (_wideTable ? 1.05 : 0.92))));
      }

      // Set CSS custom properties
      table.style.setProperty("--model-col-width", Math.min(modelChars, 18) + "ch");
      table.style.setProperty("--value-col-width", Math.min(valueChars, 9) + "ch");
      table.style.setProperty("--paper-col-width", Math.min(paperChars, 30) + "ch");
      _applyRankColumnWidth(table);
      wrapper.classList.remove("wide-table-mode");
      wrapper.style.removeProperty("--wide-table-width");
    });
  }

  function _applyRankColumnWidth(table) {
    if (!table) return;
    var tbody = table.querySelector("tbody");
    if (!tbody) return;

    var maxLen = 1;
    Array.from(tbody.querySelectorAll("tr")).forEach(function (row) {
      if (row.style.display === "none") return;
      var cell = row.querySelector("td.col-rank");
      if (!cell) return;
      var text = (cell.textContent || "").replace(/\s+/g, " ").trim();
      if (text.length > maxLen) maxLen = text.length;
    });

    // ch counts glyph width only; with border-box padding the column needs extra room
    var rankCh = Math.max(3, maxLen + 1);
    table.style.setProperty("--rank-col-width", "calc(" + rankCh + "ch + 1rem)");
  }

  function _findMoreButton(table) {
    if (!table || !table.id) return null;
    return document.querySelector("button[data-table-more='#" + table.id + "']");
  }

  function _syncTableRows(table) {
    if (!table) return;
    var tbody = table.querySelector("tbody");
    if (!tbody) return;

    var collapseAfter = parseInt(table.dataset.collapseAfter || "0", 10);
    var moreBtn = _findMoreButton(table);
    var expanded = !moreBtn || moreBtn.getAttribute("data-expanded") === "true";
    var rows = Array.from(tbody.querySelectorAll("tr"));
    var collapsibleRows = [];
    var visibleIndex = 0;

    rows.forEach(function (row) {
      var hiddenByFilter = !_rowPassesFilters(row);
      var shouldCollapse = collapseAfter > 0 && !expanded && !hiddenByFilter && visibleIndex >= collapseAfter;

      row.classList.toggle("row-collapsed", shouldCollapse);
      row.style.display = hiddenByFilter || shouldCollapse ? "none" : "";

      if (shouldCollapse) {
        collapsibleRows.push(row);
      }
      if (!hiddenByFilter && !shouldCollapse) {
        visibleIndex += 1;
      }
    });

    if (moreBtn) {
      var hiddenCount = collapsibleRows.length;
      var canCollapse = collapseAfter > 0 && rows.some(_rowPassesFilters) &&
        rows.filter(_rowPassesFilters).length > collapseAfter;
      moreBtn.hidden = !canCollapse;
      moreBtn.setAttribute("aria-expanded", expanded ? "true" : "false");
      var visibleTotal = rows.filter(_rowPassesFilters).length;
      moreBtn.textContent = expanded
        ? "Hide rows past row " + collapseAfter
        : "Show all " + visibleTotal + " rows (" + hiddenCount + " hidden)";
    }

    _applyRankColumnWidth(table);
  }

  function _initTableExpanders() {
    document.querySelectorAll("button[data-table-more]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var selector = btn.getAttribute("data-table-more");
        if (!selector) return;
        var table = document.querySelector(selector);
        if (!table) return;
        var expand = btn.getAttribute("data-expanded") !== "true";
        btn.setAttribute("data-expanded", expand ? "true" : "false");
        btn.setAttribute("aria-expanded", expand ? "true" : "false");
        _syncTableRows(table);
      });

      var selector = btn.getAttribute("data-table-more");
      var table = selector ? document.querySelector(selector) : null;
      _syncTableRows(table);
    });
  }

  function _applyModelTooltips() {
    document.querySelectorAll(".result-table tbody td.col-model").forEach(function (td) {
      var row = td.closest("tr");
      if (!row) return;
      var fullModelName = row.dataset.model || "";
      if (!fullModelName) return;

      var anchor = td.querySelector("a");
      var target = anchor || td;
      var isTruncated = td.scrollWidth > td.clientWidth;

      if (isTruncated) {
        target.setAttribute("title", fullModelName);
      } else {
        target.removeAttribute("title");
      }
    });
  }

  /* ── Paper page tables (no charts / filter bar) ─────────────────────── */
  function initPaperTableUtilities() {
    _initSortableColumns();
    _initTableExpanders();
    _initMobileRowDetails();
    _applyModelTooltips();
    window.addEventListener("resize", _applyModelTooltips);
  }

  /* ── Public API ─────────────────────────────────────────────────────── */
  window.leaderboard = {
    init: init,
    initPaperTableUtilities: initPaperTableUtilities,
    switchVariant: switchVariant,
    toggleStd: toggleStd,
    toggleSecondaryMetrics: toggleSecondaryMetrics,
    toggleBaselines: toggleBaselines,
    toggleWideTable: toggleWideTable,
  };

  // Auto-init if config is present
  document.addEventListener("DOMContentLoaded", function () {
    if (window.leaderboardConfig) {
      init();
      _initTableHover();
    } else if (document.querySelector(".paper-page .paper-results-table")) {
      initPaperTableUtilities();
    }
  });
})();

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
    // No error bar plugin used; nothing to update in Chart.js datasets
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

    const cfg = window.leaderboardConfig || {};
    const variant = (cfg.variants || []).find(function (v) { return v.slug === slug; }) || {};
    const allRows = variant.rows || [];

    if (!milestones.length && !allRows.length) return;
    if (typeof Chart === "undefined") return;

    // Snap any date string (YYYY-MM-DD, YYYY-MM, or "Jun 2022") to first-of-month UTC ms.
    function monthTs(dateStr) {
      if (!dateStr) return null;
      // ISO prefix: "2022-06..." → "2022-06-01"
      var iso = dateStr.match(/^(\d{4}-\d{2})/);
      if (iso) return Date.UTC(+iso[1].slice(0, 4), +iso[1].slice(5, 7) - 1, 1);
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

    // ── Scatter dataset: all rows ─────────────────────────────────────
    var scatterData = [];
    allRows.forEach(function (row) {
      var val = row.metric_values && row.metric_values[0];
      var ts = monthTs(row.date_iso || row.date);
      if (val == null || ts == null) return;
      scatterData.push({
        x: ts, y: val,
        std: row.metric_stds && row.metric_stds[0],
        model: row.model,
        arxiv_id: row.arxiv_id,
        is_baseline: row.is_baseline,
      });
    });

    // ── Records dataset: milestones (new bests over time) ─────────────
    var recordData = milestones.map(function (m) {
      return {
        x: monthTs(m.date),
        y: m.value,
        std: m.std,
        model: m.model,
        arxiv_id: m.arxiv_id,
        _isRecord: true,
      };
    });

    // Extend step line to today so the horizontal rule reaches the right edge
    var todayTs = (function () {
      var n = new Date();
      return Date.UTC(n.getUTCFullYear(), n.getUTCMonth(), 1);
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
    var xMaxPad = todayTs + 30 * 24 * 3600 * 1000;

    // ── Per-point styling for records line ────────────────────────────
    var recordBg = recordData.map(function (d) { return d._isRecord ? "#2563eb" : "transparent"; });
    var recordRadius = recordData.map(function (d) { return d._isRecord ? 7 : 0; });

    // ── afterDraw plugin: label each record milestone ─────────────────
    var labelPlugin = {
      id: "recordLabels_" + slug,
      afterDatasetsDraw: function (chart) {
        var meta = chart.getDatasetMeta(1);
        if (!meta || meta.hidden) return;
        var ctx = chart.ctx;
        ctx.save();
        ctx.font = "bold 11px sans-serif";
        ctx.textAlign = "left";
        meta.data.forEach(function (point, i) {
          var pd = recordData[i];
          if (!pd || !pd._isRecord || !pd.model) return;
          // Clamp label inside chart area
          var chartArea = chart.chartArea;
          var lx = Math.min(point.x + 5, chartArea.right - 80);
          ctx.fillStyle = "#1d4ed8";
          ctx.fillText(pd.model, lx, point.y - 8);
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
            data: scatterData,
            type: "scatter",
            backgroundColor: "rgba(156,163,175,0.55)",
            borderColor: "rgba(107,114,128,0.7)",
            pointRadius: 4,
            pointHoverRadius: 7,
            order: 2,
          },
          {
            label: "Record",
            data: recordData,
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
          tooltip: {
            callbacks: {
              title: function (items) {
                var item = items[0];
                var d = item.dataset.data[item.dataIndex];
                if (!d || !d.model) return fmtTs(item.parsed.x);
                return d.model + " (" + fmtTs(item.parsed.x) + ")";
              },
              label: function (item) {
                var d = item.dataset.data[item.dataIndex];
                var label = (canvas.dataset.metric || "Score") + ": " + item.formattedValue;
                if (d && d.std != null) label += " ± " + d.std.toFixed(4);
                return label;
              },
              afterLabel: function (item) {
                var d = item.dataset.data[item.dataIndex];
                return d && d.arxiv_id ? "arXiv:" + d.arxiv_id : "";
              },
            },
          },
          legend: { display: false },
        },
        scales: {
          x: {
            type: "linear",
            min: xMinPad,
            max: xMaxPad,
            title: { display: true, text: "Date" },
            ticks: {
              maxTicksLimit: 10,
              callback: fmtTs,
            },
          },
          y: {
            title: { display: true, text: canvas.dataset.metric || "Score" },
            ticks: { precision: 4 },
          },
        },
        onHover: function (event, elements) {
          _onChartHover(slug, elements, recordData, scatterData);
        },
      },
      plugins: [labelPlugin],
    });

    charts[slug] = chart;
  }

  /* ── Chart → Table hover sync ───────────────────────────────────────── */
  function _onChartHover(slug, elements, recordData, scatterData) {
    // Remove all existing highlights
    document.querySelectorAll("tr.chart-hover-highlight").forEach(function (row) {
      row.classList.remove("chart-hover-highlight");
    });

    if (!elements.length) return;
    var el = elements[0];
    // datasetIndex 0 = scatter (all), 1 = records line
    var data = el.datasetIndex === 1 ? recordData : scatterData;
    var pd = data[el.index];
    if (!pd || !pd.arxiv_id) return;

    // Find matching row in the table for this variant
    var tbody = document.querySelector(
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

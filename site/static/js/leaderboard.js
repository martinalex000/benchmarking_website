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
  const charts = {};           // variant slug -> Chart instance
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
      switchVariant(activeVariant);
    }

    _applyModelColumnWidths();
    window.addEventListener("resize", _applyModelColumnWidths);
  }

  /* ── Variant switching ──────────────────────────────────────────────── */
  function switchVariant(slug) {
    activeVariant = slug;
    document.querySelectorAll(".variant-section").forEach(function (el) {
      el.style.display = el.dataset.variant === slug ? "" : "none";
    });
    _applyModelColumnWidths();
  }

  /* ── Std toggle ─────────────────────────────────────────────────────── */
  function toggleStd(enabled) {
    showStd = enabled;
    document.querySelectorAll(".inline-std").forEach(function (el) {
      el.style.display = enabled ? "" : "none";
    });
    // Re-render all charts so the error bars plugin shows/hides
    Object.values(charts).forEach(function (chart) { chart.update("none"); });
  }

  /* ── Baseline toggle ────────────────────────────────────────────────── */
  function toggleBaselines(enabled) {
    showBaselines = enabled;
    document.querySelectorAll("tr.row-baseline").forEach(function (row) {
      row.style.display = enabled ? "" : "none";
    });
    Object.values(charts).forEach(function (chart) {
      _applyChartFilters(chart);
      chart.update("none");
    });
    _rerank();
  }

  function _applyChartFilters(chart) {
    if (!chart || !chart._scatterAll || !chart._recordAll) return;
    var visibleScatter = showBaselines
      ? chart._scatterAll.slice()
      : chart._scatterAll.filter(function (d) { return !d.is_baseline; });
    var visibleRecord = showBaselines
      ? chart._recordAll.slice()
      : chart._recordAll.filter(function (d) { return !d.is_baseline; });

    chart.data.datasets[0].data = visibleScatter;
    chart.data.datasets[1].data = visibleRecord;

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
        if (chart.tooltip && chart.tooltip.setActiveElements) {
          chart.tooltip.setActiveElements([], { x: 0, y: 0 });
        }
      }
    }
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

    // ── Scatter dataset: all rows ─────────────────────────────────────
    var scatterData = [];
    var modelBaselineMap = {};
    allRows.forEach(function (row) {
      var val = row.metric_values && row.metric_values[0];
      var ts = dateTs(row.date_iso || row.date);
      if (val == null || ts == null) return;
      modelBaselineMap[row.model] = !!row.is_baseline;
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
        x: dateTs(m.date),
        y: m.value,
        std: m.std,
        model: m.model,
        arxiv_id: m.arxiv_id,
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
    var xMaxPad = todayTs + 30 * 24 * 3600 * 1000;

    // ── Per-point styling for records line ────────────────────────────
    var recordBg = recordData.map(function (d) { return d._isRecord ? "#2563eb" : "transparent"; });
    var recordRadius = recordData.map(function (d) { return d._isRecord ? 7 : 0; });

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
        ctx.strokeStyle = "rgba(31,41,55,0.12)";
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

    // ── afterDraw plugin: draw ± std error bars ───────────────────────
    function _drawErrorBar(ctx, px, yScale, yVal, std, color, capHalf) {
      var yHi = yScale.getPixelForValue(yVal + std);
      var yLo = yScale.getPixelForValue(yVal - std);
      ctx.save();
      ctx.strokeStyle = color;
      ctx.lineWidth = 1.5;
      // vertical stem
      ctx.beginPath(); ctx.moveTo(px, yHi); ctx.lineTo(px, yLo); ctx.stroke();
      // top cap
      ctx.beginPath(); ctx.moveTo(px - capHalf, yHi); ctx.lineTo(px + capHalf, yHi); ctx.stroke();
      // bottom cap
      ctx.beginPath(); ctx.moveTo(px - capHalf, yLo); ctx.lineTo(px + capHalf, yLo); ctx.stroke();
      ctx.restore();
    }

    var errorBarsPlugin = {
      id: "errorBars_" + slug,
      afterDatasetsDraw: function (chart) {
        if (!showStd) return;
        var ctx = chart.ctx;
        var yScale = chart.scales.y;
        // Scatter dataset (index 0)
        var sm = chart.getDatasetMeta(0);
        if (sm && !sm.hidden) {
          sm.data.forEach(function (point, i) {
            var d = scatterData[i];
            if (!d || d.std == null) return;
            _drawErrorBar(ctx, point.x, yScale, d.y, d.std, "rgba(107,114,128,0.55)", 5);
          });
        }
        // Records dataset (index 1)
        var rm = chart.getDatasetMeta(1);
        if (rm && !rm.hidden) {
          rm.data.forEach(function (point, i) {
            var d = recordData[i];
            if (!d || !d._isRecord || d.std == null) return;
            _drawErrorBar(ctx, point.x, yScale, d.y, d.std, "rgba(37,99,235,0.7)", 7);
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
        _drawErrorBar(ctx, activePoint.x, yScale, activeDatum.y, activeDatum.std, "rgba(251,191,36,0.95)", 9);
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
            pointHoverBackgroundColor: "#f59e0b",
            pointHoverBorderColor: "#fbbf24",
            pointHoverBorderWidth: 2,
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
                if (showStd && d && d.std != null) label += " ± " + d.std.toFixed(4);
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
              callback: function (value) {
                return String(new Date(value).getUTCFullYear());
              },
            },
          },
          y: {
            title: { display: true, text: canvas.dataset.metric || "Score" },
            ticks: { precision: 4 },
          },
        },
        onHover: function (event, elements) {
          _onChartHover(slug, elements, chart);
        },
      },
      plugins: [yearLinesPlugin, labelPlugin, errorBarsPlugin],
    });

    chart._scatterAll = scatterData.slice();
    chart._recordAll = recordData.slice();
    _applyChartFilters(chart);
    chart.update("none");

    charts[slug] = chart;
  }

  /* ── Chart → Table hover sync ───────────────────────────────────────── */
  function _onChartHover(slug, elements, chart) {
    // Remove all existing highlights
    document.querySelectorAll("tr.chart-hover-highlight").forEach(function (row) {
      row.classList.remove("chart-hover-highlight");
    });

    // Clear hover preview
    var preview = document.getElementById("hover-preview-" + slug);

    if (!elements.length) {
      if (preview) preview.style.display = "none";
      return;
    }
    var el = elements[0];
    // datasetIndex 0 = scatter (all), 1 = records line
    var data = chart.data.datasets[el.datasetIndex].data || [];
    var pd = data[el.index];
    if (!pd || !pd.arxiv_id) {
      if (preview) preview.style.display = "none";
      return;
    }

    // Find matching row in the table for this variant
    var tbody = document.querySelector(
      ".leaderboard-section[data-variant='" + slug + "'] .result-table tbody"
    );
    var matchedRow = null;
    if (tbody) {
      tbody.querySelectorAll("tr").forEach(function (row) {
        if (row.dataset.arxiv === pd.arxiv_id && row.dataset.model === pd.model) {
          row.classList.add("chart-hover-highlight");
          matchedRow = row;
        }
      });
    }

    // Show hover preview below chart
    if (preview && matchedRow) {
      var tbl = matchedRow.closest("table");
      var headers = tbl ? Array.from(tbl.querySelectorAll("thead th")).map(function (th) {
        return th.textContent.trim();
      }) : [];
      var cells = Array.from(matchedRow.querySelectorAll("td"));
      var parts = [];
      cells.forEach(function (td, i) {
        var hdr = headers[i] || "";
        // Skip rank and type columns for readability.
        if (i === 0 || hdr === "Type") return;
        var txt = td.textContent.trim().replace(/\s+/g, " ");
        if (txt && txt !== "—") {
          parts.push("<span class='preview-item'>" +
            (hdr ? "<span class='preview-hdr'>" + hdr + "</span>" : "") +
            "<span class='preview-val'>" + txt + "</span></span>");
        }
      });
      preview.innerHTML = "<span class='preview-label'>Hovered</span><div class='preview-items'>" + parts.join("") + "</div>";
      preview.style.display = "";
    } else if (preview) {
      preview.style.display = "none";
    }
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
        const meta = chart.getDatasetMeta(0);
        const pt = meta && meta.data ? meta.data[idx] : null;
        if (chart.tooltip && chart.tooltip.setActiveElements && pt) {
          chart.tooltip.setActiveElements([{ datasetIndex: 0, index: idx }], { x: pt.x, y: pt.y });
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
          if (charts[slug].tooltip && charts[slug].tooltip.setActiveElements) {
            charts[slug].tooltip.setActiveElements([], { x: 0, y: 0 });
          }
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
    _rerank();
  }

  function _cellValue(row, col) {
    const raw = row.dataset[col];
    if (raw === "" || raw === null || raw === undefined) return null;
    const num = parseFloat(raw);
    return isNaN(num) ? raw : num;
  }

  /* ── Wide-table toggle ──────────────────────────────────────────────── */
  var _wideTable = false;
  function toggleWideTable() {
    _wideTable = !_wideTable;
    document.querySelectorAll(".result-table-wrapper").forEach(function (el) {
      if (_wideTable) {
        el.classList.add("wide-table-mode");
      } else {
        el.classList.remove("wide-table-mode");
      }
    });
    var btn = document.getElementById("wide-table-btn");
    if (btn) btn.textContent = _wideTable ? "⤡ Compact width" : "⤢ Balanced width";
    _applyModelColumnWidths();
  }

  function _percentile(sortedNums, p) {
    if (!sortedNums.length) return 0;
    var idx = Math.max(0, Math.min(sortedNums.length - 1, Math.floor(p * (sortedNums.length - 1))));
    return sortedNums[idx];
  }

  function _applyModelColumnWidths() {
    document.querySelectorAll(".result-table").forEach(function (table) {
      var modelCells = Array.from(table.querySelectorAll("tbody td.col-model"));
      if (!modelCells.length) return;
      var lengths = modelCells
        .map(function (td) { return (td.textContent || "").replace(/\s+/g, " ").trim().length; })
        .filter(function (n) { return n > 0; })
        .sort(function (a, b) { return a - b; });
      if (!lengths.length) return;

      // Use 90th percentile + 20% for dynamic width calculation
      var p90 = _percentile(lengths, 0.9);
      var targetChars = Math.ceil(p90 * 1.2);
      // Keep a sensible range for the model column
      targetChars = Math.max(10, Math.min(34, targetChars));
      if (_wideTable) {
        targetChars = Math.min(38, targetChars + 3);
      }
      
      var wrapper = table.closest(".result-table-wrapper");
      if (wrapper) {
        table.style.setProperty("--model-col-width", targetChars + "ch");
        if (_wideTable) {
          wrapper.classList.add("wide-table-mode");
        } else {
          wrapper.classList.remove("wide-table-mode");
        }
      }
    });
  }

  /* ── Public API ─────────────────────────────────────────────────────── */
  window.leaderboard = {
    init: init,
    switchVariant: switchVariant,
    toggleStd: toggleStd,
    toggleBaselines: toggleBaselines,
    toggleWideTable: toggleWideTable,
  };

  // Auto-init if config is present
  document.addEventListener("DOMContentLoaded", function () {
    if (window.leaderboardConfig) {
      init();
      _initTableHover();
    }
  });
})();

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
    const showAllVariants = !!cfg.showAllVariants;

    variants.forEach(function (v) {
      const canvas = document.getElementById("chart-" + v.slug);
      if (canvas) {
        buildChart(canvas, v.slug, cfg.higherIsBetter !== false);
      }
    });

    _initSortableColumns();
    _initTableExpanders();

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
    showStd = enabled;
    document.querySelectorAll(".inline-std").forEach(function (el) {
      el.style.display = enabled ? "" : "none";
    });
    // Re-render all charts so the error bars plugin shows/hides
    Object.values(charts).forEach(function (chart) { chart.update("none"); });
    _applyModelColumnWidths();
    _applyModelTooltips();
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

  function _buildPreviewItems(row) {
    if (!row) return "";
    var tbl = row.closest("table");
    var headers = tbl ? Array.from(tbl.querySelectorAll("thead th")).map(function (th) {
      return th.textContent.trim();
    }) : [];
    var cells = Array.from(row.querySelectorAll("td"));
    var parts = [];
    cells.forEach(function (td, i) {
      var hdr = headers[i] || "";
      if (i === 0 || hdr === "Type") return;
      var txt = td.textContent.trim().replace(/\s+/g, " ");
      if (txt && txt !== "—") {
        parts.push("<span class='preview-item'>" +
          (hdr ? "<span class='preview-hdr'>" + hdr + "</span>" : "") +
          "<span class='preview-val'>" + txt + "</span></span>");
      }
    });
    return parts.join("");
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
    var parts = _buildPreviewItems(selection.row);
    if (!parts) {
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
      "</div><div class='preview-items'>" + parts + "</div>";
    preview.style.display = "";

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
    if (/^gcn(?:\s|\(|$)/.test(raw)) return "gcn";
    if (/^gin(?:\s|\(|$)/.test(raw)) return "gin";
    if (/^graphsage(?:\s|\(|$)/.test(raw)) return "graphsage";
    if (/^mlp(?:\s|\(|$)/.test(raw)) return "mlp";
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

    var titleByArxiv = {};
    allRows.forEach(function (row) {
      if (row.arxiv_id && row.title && !titleByArxiv[row.arxiv_id]) {
        titleByArxiv[row.arxiv_id] = row.title;
      }
    });

    var gnnReference = _pickBestReference(allRows, higherIsBetter, ["gcn", "gin", "graphsage"]);
    var mlpReference = _pickBestReference(allRows, higherIsBetter, "mlp");

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
        title: row.title || "",
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
          ctx.fillStyle = "#1d4ed8";
          ctx.fillText(label, lx, ly);
          placedBoxes.push({ left: lx, right: lx + width, top: ly - height, bottom: ly + 2 });
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
        var scatterDataset = chart.data.datasets[0];
        var scatterPoints = scatterDataset && scatterDataset.data ? scatterDataset.data : [];
        var sm = chart.getDatasetMeta(0);
        if (sm && !sm.hidden) {
          sm.data.forEach(function (point, i) {
            var d = scatterPoints[i];
            if (!d || d.std == null) return;
            _drawErrorBar(ctx, point.x, yScale, d.y, d.std, "rgba(107,114,128,0.55)", 5);
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

    var referenceLinesPlugin = {
      id: "referenceLines_" + slug,
      afterDatasetsDraw: function (chart) {
        var refs = [
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
        if (!refs.length) return;

        var ctx = chart.ctx;
        var yScale = chart.scales.y;
        var area = chart.chartArea;
        ctx.save();
        ctx.font = "600 11px sans-serif";
        refs.forEach(function (ref, idx) {
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

          var textWidth = ctx.measureText(ref.label).width;
          var labelX = Math.max(area.left + 8, area.right - textWidth - 12);
          var offset = ref.position === "below" ? 16 + idx * 14 : -6 - idx * 14;
          var unclampedY = py + offset;
          var labelY = Math.min(area.bottom - 4, Math.max(area.top + 12, unclampedY));
          ctx.fillStyle = "rgba(255,255,255,0.88)";
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
                if (!d || !d.model) return item.dataset.label;
                return d.model;
              },
              label: function (item) {
                var d = item.dataset.data[item.dataIndex];
                var value = item.parsed && typeof item.parsed.y === "number" ? item.parsed.y : item.raw && item.raw.y;
                var label = (canvas.dataset.metric || "Score") + ": " + _formatMetricValue(value);
                if (showStd && d && d.std != null) label += " ± " + d.std.toFixed(4);
                return label;
              },
              footer: function (items) {
                var item = items[0];
                var d = item.dataset.data[item.dataIndex];
                if (!d) return "";
                var lines = [fmtTs(item.parsed.x)];
                if (d.title) lines.push(_truncateTitle(d.title));
                return lines;
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
        onClick: function (event, elements) {
          _onChartClick(slug, elements, chart);
        },
      },
      plugins: [yearLinesPlugin, referenceLinesPlugin, labelPlugin, errorBarsPlugin],
    });

    chart._scatterAll = scatterData.slice();
    chart._recordAll = recordData.slice();
    chart._slug = slug;
    _applyChartFilters(chart);
    chart.update("none");

    charts[slug] = chart;
  }

  /* ── Chart → Table hover sync ───────────────────────────────────────── */
  function _onChartHover(slug, elements, chart) {
    _clearRowHighlights("chart-hover-highlight");

    if (!elements.length) {
      chart._lastHoverSelection = null;
      _updatePreview(slug, chart);
      return;
    }
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
      var modelP90 = modelLens.length ? _percentile(modelLens, 0.9) : 0;
      var modelChars = Math.ceil(modelP90 * 1.12);
      modelChars = Math.max(11, Math.min(_wideTable ? 24 : 20, modelChars));

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
      table.style.setProperty("--model-col-width", modelChars + "ch");
      table.style.setProperty("--value-col-width", valueChars + "ch");
      table.style.setProperty("--paper-col-width", paperChars + "ch");

      // Update wrapper class
      if (_wideTable) {
        wrapper.classList.add("wide-table-mode");

        // Balanced mode should be "as much as needed", not "as wide as possible".
        // 1) Let table use natural content width.
        // 2) Cap at viewport so there is never horizontal page/table scrolling.
        // 3) If over cap, reduce paper/model/value widths until it fits while staying single-line.
        // Keep a safety margin from viewport edges and avoid subpixel overflow artifacts.
        var viewportCap = Math.max(320, window.innerWidth - 56);
        var fitCap = Math.max(300, viewportCap - 8);
        var minPaper = 18;
        var minModel = 10;
        var minValue = 7;
        var guard = 0;

        while (table.scrollWidth > fitCap && guard < 48) {
          if (paperChars > minPaper) {
            paperChars -= 1;
          } else if (modelChars > minModel) {
            modelChars -= 1;
          } else if (valueChars > minValue) {
            valueChars -= 1;
          } else {
            break;
          }
          table.style.setProperty("--paper-col-width", paperChars + "ch");
          table.style.setProperty("--model-col-width", modelChars + "ch");
          table.style.setProperty("--value-col-width", valueChars + "ch");
          guard += 1;
        }

        // Add a 1px buffer so rendered table width does not exceed wrapper because of rounding.
        var needed = Math.min(viewportCap, table.scrollWidth + 1);
        wrapper.style.setProperty("--wide-table-width", needed + "px");
      } else {
        wrapper.classList.remove("wide-table-mode");
        wrapper.style.removeProperty("--wide-table-width");
      }
    });
  }

  function _initTableExpanders() {
    document.querySelectorAll("button[data-table-more]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var selector = btn.getAttribute("data-table-more");
        if (!selector) return;
        var table = document.querySelector(selector);
        if (!table) return;
        var expand = btn.getAttribute("data-expanded") !== "true";
        table.querySelectorAll("tbody tr.row-collapsed").forEach(function (row) {
          row.style.display = expand ? "" : "none";
        });
        btn.setAttribute("data-expanded", expand ? "true" : "false");
        btn.textContent = expand ? "Show less" : (btn.getAttribute("data-default-label") || "More");
        _rerank();
      });

      // Persist original label for toggling back.
      btn.setAttribute("data-default-label", btn.textContent.trim());
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

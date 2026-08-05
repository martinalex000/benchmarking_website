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

  if (typeof performance !== "undefined") {
    performance.mark("leaderboard:scripts_loaded");
  }

  const CROWDED_PLOT_THRESHOLD = 200;
  const TOP_N_ALWAYS_VISIBLE = 10;

  /* ── State ─────────────────────────────────────────────────────────── */
  const charts = {};           // variant slug -> Chart instance
  let _perfChartsPending = 0;
  let showStd = true;
  let showBaselines = true;
  let showSecondaryMetrics = false;
  let showFlatAllMetrics = true;
  let showExternalData = true;
  let showNoCode = true;
  let activeVariant = null;
  const variantTargetSelection = {};
  const variantMetricIndex = {};
  const variantLogScale = {};
  const SCI_NOTATION_THRESHOLD = 1e-4;

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
    walk: true,
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

  function _perfEnabled() {
    try {
      if (new URLSearchParams(window.location.search).get("perf") === "1") return true;
      return localStorage.getItem("leaderboardPerf") === "1";
    } catch (e) {
      return false;
    }
  }

  function _perfMeasureMs(name) {
    var entries = performance.getEntriesByName(name);
    return entries.length ? Math.round(entries[0].duration * 10) / 10 : null;
  }

  function _reportPerfSummary() {
    var rows = [];
    Object.values(charts).forEach(function (chart) {
      var slug = chart._slug || "?";
      var prefix = "chart-" + slug + ":";
      rows.push({
        variant: slug,
        points: chart._pointCount,
        crowded: chart._isCrowded ? "yes" : "no",
        parse_ms: _perfMeasureMs(prefix + "parse"),
        create_ms: _perfMeasureMs(prefix + "create"),
        layout_ms: _perfMeasureMs(prefix + "layout"),
        error_bars_ms: Math.round((chart._perfErrorBarsMs || 0) * 10) / 10,
      });
    });
    console.table(rows);
    var initMs = _perfMeasureMs("leaderboard:init");
    if (initMs != null) {
      console.log("leaderboard init:", initMs, "ms");
    }
  }

  function _shouldDrawDatumStd(chart, datum) {
    if (!datum || datum.std == null) return false;
    if (chart._isCrowded && datum.is_baseline && !datum._isRecord && !datum._isSotaMatch) {
      return false;
    }
    return true;
  }

  const rowsJsonCache = {};
  const chartPointsCache = {};

  function _scheduleDeferredLayout() {
    var run = function () {
      _applyModelColumnWidths();
      _applyModelTooltips();
    };
    if (typeof requestIdleCallback === "function") {
      requestIdleCallback(run, { timeout: 2000 });
    } else {
      setTimeout(run, 0);
    }
  }

  function _normalizeAssetUrl(url) {
    var cleaned = String(url || "").trim();
    if (
      (cleaned.charAt(0) === '"' && cleaned.charAt(cleaned.length - 1) === '"') ||
      (cleaned.charAt(0) === "'" && cleaned.charAt(cleaned.length - 1) === "'")
    ) {
      cleaned = cleaned.slice(1, -1);
    }
    return cleaned;
  }

  function _siteBasePath() {
    var meta = document.querySelector('meta[name="site-base-path"]');
    return meta ? String(meta.content || "").replace(/\/$/, "") : "";
  }

  function _resolveAssetUrl(url) {
    url = _normalizeAssetUrl(url);
    if (!url || /^https?:\/\//i.test(url)) {
      return url;
    }
    if (url.charAt(0) === "/") {
      var base = _siteBasePath();
      if (base && url.indexOf(base + "/") !== 0 && url !== base) {
        return base + url;
      }
    }
    return url;
  }

  function _fetchJson(url) {
    url = _resolveAssetUrl(url);
    return fetch(url, { credentials: "same-origin" }).then(function (resp) {
      if (!resp.ok) throw new Error("Failed to load " + url);
      return resp.json();
    });
  }

  function _fetchChartPoints(chartJsonUrl) {
    if (!chartJsonUrl) return Promise.resolve(null);
    if (chartPointsCache[chartJsonUrl]) {
      return Promise.resolve(chartPointsCache[chartJsonUrl]);
    }
    return _fetchJson(chartJsonUrl).then(function (payload) {
      var points = payload && payload.points ? payload.points : [];
      chartPointsCache[chartJsonUrl] = points;
      return points;
    });
  }

  function _chartPointsToRows(points) {
    return (points || []).map(function (p) {
      return {
        metric_values: [p.value],
        metric_stds: [p.std],
        date_iso: p.date_iso,
        date: p.date_iso,
        model: p.model,
        model_plain: p.model_plain || p.model,
        arxiv_id: p.arxiv_id,
        title: p.title,
        is_baseline: p.is_baseline,
        uses_external_data: p.uses_external_data,
        codebase_url: p.has_code ? "1" : "",
        architecture_type: p.architecture_type,
        is_std_outlier: p.is_std_outlier,
      };
    });
  }

  function _scheduleChartBuild(canvas, slug, cfg) {
    var variant = (cfg.variants || []).find(function (v) { return v.slug === slug; }) || {};
    var defaultIdx = _defaultMetricIndex(variant);
    var selection = variantTargetSelection[slug];
    if (selection == null) {
      selection = String(variantMetricIndex[slug] != null ? variantMetricIndex[slug] : defaultIdx);
    }
    selection = _normalizeTargetSelection(selection, variant);
    var metricIndex = _targetMetricIndex(variant, selection);
    variantTargetSelection[slug] = selection;
    variantMetricIndex[slug] = metricIndex;
    variantLogScale[slug] = _chartDefaultLogScale(variant) ||
      _readSessionBool(_sessionKey("log", slug), false);
    var metrics = variant.metrics || [];
    var milestones = _milestonesForTarget(canvas, variant, metricIndex);
    canvas.dataset.milestones = JSON.stringify(milestones);
    canvas.dataset.metric = _metricLabel(variant, metricIndex);
    var run = function () {
      var chartJson = variant.chart_json || "";
      if (chartJson) {
        _fetchChartPoints(chartJson).then(function (points) {
          if (!canvas.isConnected) return;
          buildChart(canvas, slug, cfg.higherIsBetter !== false, points, _chartBuildOptions(slug, variant));
          _syncLogScaleToggle(slug, variantMetricIndex[slug] || 0);
        }).catch(function (err) {
          console.error("Chart data load failed for", slug, err);
        });
        return;
      }
      buildChart(canvas, slug, cfg.higherIsBetter !== false, null, _chartBuildOptions(slug, variant));
    };
    if (typeof requestAnimationFrame === "function") {
      requestAnimationFrame(run);
    } else {
      run();
    }
  }

  function _escapeHtml(text) {
    return String(text || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function _formatMetricValue(value) {
    if (typeof value !== "number" || !isFinite(value)) return "—";
    if (value !== 0 && Math.abs(value) < SCI_NOTATION_THRESHOLD) {
      return value.toExponential(2);
    }
    return value.toFixed(4);
  }

  function _slugify(text) {
    return String(text || "")
      .toLowerCase()
      .trim()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");
  }

  function _needsSciNotation(values) {
    return (values || []).some(function (v) {
      return typeof v === "number" && isFinite(v) && v !== 0 && Math.abs(v) < SCI_NOTATION_THRESHOLD;
    });
  }

  function _allPositive(values) {
    return (values || []).every(function (v) {
      return typeof v === "number" && isFinite(v) && v > 0;
    });
  }

  function _getVariant(slug) {
    var cfg = window.leaderboardConfig || {};
    return (cfg.variants || []).find(function (v) { return v.slug === slug; }) || {};
  }

  function _defaultMetricIndex(variant) {
    var metrics = variant.metrics || [];
    var defaultMetric = variant.default_metric || variant.primary_metric;
    var idx = metrics.indexOf(defaultMetric);
    return idx >= 0 ? idx : 0;
  }

  function _isAllTargetSelection(selection) {
    return String(selection || "") === "all";
  }

  function _normalizeTargetSelection(selection, variant) {
    if (_isAllTargetSelection(selection)) return "all";
    var metrics = variant.metrics || [];
    var idx = parseInt(selection, 10);
    if (isNaN(idx) || idx < 0 || idx >= metrics.length) {
      return String(_defaultMetricIndex(variant));
    }
    return String(idx);
  }

  function _targetMetricIndex(variant, selection) {
    if (_isAllTargetSelection(selection)) {
      return _defaultMetricIndex(variant);
    }
    var idx = parseInt(selection, 10);
    return isNaN(idx) ? _defaultMetricIndex(variant) : idx;
  }

  function _milestonesForTarget(canvas, variant, metricIndex) {
    var metrics = variant.metrics || [];
    var metricKey = metrics[metricIndex];
    var byMetric = variant.milestones_by_metric || {};
    if (metricKey && byMetric[metricKey] && byMetric[metricKey].length) {
      return byMetric[metricKey];
    }
    if (variant.milestones && variant.milestones.length) {
      return variant.milestones;
    }
    var canvasByMetric = {};
    if (canvas) {
      try {
        canvasByMetric = JSON.parse(canvas.getAttribute("data-milestones-by-metric") || "{}");
      } catch (e) { /* ignore */ }
    }
    if (metricKey && canvasByMetric[metricKey] && canvasByMetric[metricKey].length) {
      return canvasByMetric[metricKey];
    }
    if (!canvas) return [];
    try {
      return JSON.parse(canvas.getAttribute("data-milestones") || "[]");
    } catch (e) {
      return [];
    }
  }

  function _metricLabel(variant, metricIndex) {
    var labels = variant.metric_display_names || variant.metrics || [];
    return labels[metricIndex] || (variant.metrics || [])[metricIndex] || "Score";
  }

  function _targetOptionLabel(variant, metricIndex) {
    var label = _metricLabel(variant, metricIndex);
    var counts = variant.metric_counts;
    if (counts && counts[metricIndex] != null) {
      return label + " (" + counts[metricIndex] + ")";
    }
    return label;
  }

  function _syncTargetPickerLabels(variant) {
    if (!variant || !variant.slug) return;
    var slug = variant.slug;
    [document.getElementById("chart-target-" + slug)].forEach(function (select) {
      if (!select) return;
      Array.from(select.options).forEach(function (opt) {
        if (_isAllTargetSelection(opt.value)) return;
        var idx = parseInt(opt.value, 10);
        if (!isNaN(idx)) opt.textContent = _targetOptionLabel(variant, idx);
      });
    });
  }

  function _valuesForMetric(rows, metricIndex) {
    return (rows || []).map(function (row) {
      var vals = row.metric_values || [];
      return vals[metricIndex];
    }).filter(function (v) { return typeof v === "number" && isFinite(v); });
  }

  function _sessionKey(prefix, slug) {
    return "leaderboard:" + prefix + ":" + slug;
  }

  function _readSessionInt(key, fallback) {
    try {
      var raw = sessionStorage.getItem(key);
      if (raw == null || raw === "") return fallback;
      var parsed = parseInt(raw, 10);
      return isNaN(parsed) ? fallback : parsed;
    } catch (e) {
      return fallback;
    }
  }

  function _readSessionBool(key, fallback) {
    try {
      var raw = sessionStorage.getItem(key);
      if (raw == null) return fallback;
      return raw === "1";
    } catch (e) {
      return fallback;
    }
  }

  function _writeSession(key, value) {
    try {
      sessionStorage.setItem(key, String(value));
    } catch (e) { /* ignore */ }
  }

  function _truncateText(text, maxLen) {
    var str = String(text || "");
    return str.length > maxLen ? str.slice(0, maxLen - 3) + "..." : str;
  }

  function _formatMobileDate(dateDisplay) {
    return String(dateDisplay || "").replace(/([A-Za-z]+)\s+20([0-9]{2})/, "$1 '$2");
  }

  function _archBadgeHtml(row) {
    if (!row || !row.architecture_label) return "";
    var type = _escapeHtml(row.architecture_type || "");
    var title = _escapeHtml(row.architecture_title || "");
    var label = _escapeHtml(row.architecture_label);
    return '<span class="mini-badge mini-badge-arch mini-badge-arch-' + type +
      '" title="' + title + '">' + label + "</span>";
  }

  function _metricValueHtml(val, std, isStdOutlier, stacked) {
    if (val == null) return "—";
    var stdClass = isStdOutlier ? " inline-std-outlier" : "";
    var blockClass = stacked ? "metric-stacked-block" : "metric-primary-block";
    var valueClass = stacked ? "metric-stacked-value" : "metric-primary-value";
    var stdSpanClass = stacked ? "metric-stacked-std inline-std" : "metric-primary-std inline-std";
    var html = '<div class="' + blockClass + '"><span class="' + valueClass + '">' +
      _formatMetricValue(val) + "</span>";
    if (std != null) {
      html += '<span class="' + stdSpanClass + stdClass + '">±' + _formatMetricValue(std) + "</span>";
    }
    html += "</div>";
    return html;
  }

  function _buildDatasetRowHtml(row, index, metrics, collapseAfter) {
    var vals = row.metric_values || [];
    var stds = row.metric_stds || [];
    var primaryVal = vals[0];
    var classes = ["result-row"];
    if (row.is_baseline) classes.push("row-baseline"); else classes.push("row-proposed");
    if (row.is_overridden) classes.push("row-overridden");
    if (row.is_best) classes.push("row-best");
    if (index === 0) classes.push("row-current-sota");
    if (collapseAfter > 0 && index >= collapseAfter) classes.push("row-collapsed");

    var extData = row.uses_external_data === true ? "1" : (row.uses_external_data === false ? "0" : "");
    var hasCode = row.codebase_url ? "1" : "0";
    var dateDisplay = row.date_display || row.date || "—";
    var mobileDate = _formatMobileDate(dateDisplay);
    var rowDetailsId = "mobile-details-js-" + index;

    var html = '<tr class="' + classes.join(" ") + '" data-original-index="' + index + '"' +
      ' data-model="' + _escapeHtml(row.model_plain || row.model || "") + '"' +
      ' data-value="' + (row.sort_value != null ? row.sort_value : (primaryVal != null ? primaryVal : "")) + '"';
    metrics.forEach(function (_metric, j) {
      var mv = vals[j];
      html += ' data-value-' + j + '="' + (mv != null ? mv : "") + '"';
    });
    html += ' data-params="' + (row.params_millions != null ? row.params_millions : "") + '"' +
      ' data-date="' + _escapeHtml(row.date_iso || row.date || "") + '"' +
      ' data-arxiv="' + _escapeHtml(row.arxiv_id || "") + '"' +
      ' data-architecture="' + _escapeHtml(row.architecture_type || "") + '"' +
      ' data-external-data="' + extData + '"' +
      ' data-has-code="' + hasCode + '">';

    html += '<td class="col-rank" data-label="Rank">' + (index + 1) + "</td>";
    html += '<td class="col-model" data-label="Model"><div class="leaderboard-entry-head"><div class="leaderboard-entry-main">';
    html += '<div class="leaderboard-model-name">' + (row.model || "") + "</div>";
    html += '<div class="leaderboard-entry-meta"><div class="leaderboard-badges">';
    if (row.codebase_url) {
      html += '<a class="mini-badge mini-badge-code" href="' + _escapeHtml(row.codebase_url) +
        '" target="_blank" rel="noopener" title="Code available">code ↗</a>';
    }
    if (row.uses_external_data) {
      html += '<span class="mini-badge mini-badge-external" title="Uses external data during training">ext data</span>';
    }
    html += _archBadgeHtml(row);
    if (row.params_millions) {
      html += '<span class="mini-badge mini-badge-neutral">' + Number(row.params_millions).toFixed(1) + "M</span>";
    }
    if (row.is_overridden) {
      html += '<span class="override-badge" title="' + _escapeHtml(row.override_reason || "") + '">✎</span>';
    }
    if (row.is_baseline) {
      html += '<span class="tag-baseline">baseline</span>';
    } else {
      html += '<span class="tag-proposed">★ proposed</span>';
    }
    html += "</div></div></div></td>";

    metrics.forEach(function (metric, j) {
      var val = vals[j];
      var std = stds[j];
      var colClass = "col-value";
      if (j === 0) colClass += " col-primary";
      else colClass += " col-secondary-metric";
      html += '<td class="' + colClass + '" data-label="' + _escapeHtml(metric) + '" data-metric-index="' + j + '">';
      html += _metricValueHtml(val, std, row.is_std_outlier, j > 0);
      if (j === 0 && metrics.length > 1) {
        html += '<div class="secondary-metrics" hidden>';
        metrics.forEach(function (secMetric, k) {
          if (k === 0) return;
          var secVal = vals[k];
          var secStd = stds[k];
          if (secVal == null) return;
          html += '<div class="secondary-metric"><span class="secondary-metric-name">' +
            _escapeHtml(secMetric) + '</span><span class="metric-stacked-block metric-stacked-block-inline">' +
            '<span class="metric-stacked-value">' + _formatMetricValue(secVal) + "</span>";
          if (secStd != null) {
            html += '<span class="metric-stacked-std inline-std' +
              (row.is_std_outlier ? " inline-std-outlier" : "") + '">±' + _formatMetricValue(secStd) + "</span>";
          }
          html += "</span></div>";
        });
        html += "</div>";
      }
      html += "</td>";
    });

    html += '<td class="col-paper mobile-details-hit" id="' + rowDetailsId + '" data-label="Paper">';
    html += '<div class="paper-cell-row"><div class="paper-title-wrap">';
    var conferenceLabel = row.published_conference || row.published_venue || "";
    var conferenceSlug = row.published_conference_slug || (
      row.published_conference_short ? _slugify(row.published_conference_short) : _slugify(conferenceLabel)
    );
    if (conferenceLabel) {
      html += '<a class="paper-conference-badge" href="' + _siteBasePath() + "/papers/?conference=" +
        encodeURIComponent(conferenceSlug) + '" title="Filter papers by venue">' +
        _escapeHtml(conferenceLabel) + "</a>";
    }
    if (row.arxiv_id) {
      var paperHref = "papers/" + encodeURIComponent(row.arxiv_id) + "/";
      var paperTitle = row.title ? _truncateText(row.title, 96) : ("arXiv:" + row.arxiv_id);
      html += '<a class="paper-title-link" href="' + paperHref + '" title="arXiv:' +
        _escapeHtml(row.arxiv_id) + (row.title ? (" — " + _escapeHtml(row.title)) : "") + '">' +
        _escapeHtml(paperTitle) + "</a>";
    } else {
      html += "—";
    }
    if (row.codebase_url) {
      html += '<a class="paper-code-link" href="' + _escapeHtml(row.codebase_url) +
        '" target="_blank" rel="noopener">code ↗</a>';
    } else {
      html += '<span class="paper-code-missing" title="No code link available">no code</span>';
    }
    html += '</div><div class="paper-inline-meta">';
    if (conferenceLabel) {
      html += '<a class="paper-conference-badge paper-conference-badge-mobile" href="' +
        _siteBasePath() + "/papers/?conference=" + encodeURIComponent(conferenceSlug) +
        '" title="Filter papers by venue">' + _escapeHtml(conferenceLabel) + "</a>";
    }
    html += '<span class="paper-date-inline paper-date-inline-full">' + _escapeHtml(dateDisplay) + "</span>";
    html += '<span class="paper-date-inline paper-date-inline-short">' + _escapeHtml(mobileDate) + "</span>";
    html += '<button type="button" class="mobile-details-toggle" aria-expanded="false" aria-controls="' +
      rowDetailsId + '" aria-label="Toggle details">▾</button>';
    html += "</div></div></td></tr>";
    return html;
  }

  function _tableVariantMetrics(table) {
    var match = (table.id || "").match(/^tbl-(.+)$/);
    if (!match) return [];
    var slug = match[1];
    var cfg = window.leaderboardConfig || {};
    var variant = (cfg.variants || []).find(function (v) { return v.slug === slug; });
    return variant && variant.metrics ? variant.metrics : [];
  }

  function _appendDatasetRows(table, rows, startIndex, collapseAfter) {
    if (!table || !rows || !rows.length) return;
    var metrics = _tableVariantMetrics(table);
    if (!metrics.length) return;
    var tbody = table.querySelector("tbody");
    if (!tbody) return;
    var html = rows.map(function (row, offset) {
      return _buildDatasetRowHtml(row, startIndex + offset, metrics, collapseAfter);
    }).join("");
    tbody.insertAdjacentHTML("beforeend", html);
  }

  function _ensureAllRowsLoaded(table) {
    if (!table || table.dataset.rowsLoaded === "all") {
      return Promise.resolve();
    }
    var url = table.dataset.rowsJson;
    if (!url) {
      table.dataset.rowsLoaded = "all";
      return Promise.resolve();
    }
    if (rowsJsonCache[url]) {
      var cached = rowsJsonCache[url];
      var cachedInitial = parseInt(table.dataset.initialRows || "0", 10);
      var cachedCollapseAfter = parseInt(table.dataset.collapseAfter || "0", 10);
      var cachedAllRows = cached && cached.rows ? cached.rows : [];
      var cachedExtraRows = cachedAllRows.slice(cachedInitial);
      _appendDatasetRows(table, cachedExtraRows, cachedInitial, cachedCollapseAfter);
      table.dataset.rowsLoaded = "all";
      var cachedSlug = (table.id || "").replace(/^tbl-/, "");
      var cachedVariant = _getVariant(cachedSlug);
      var cachedSelection = variantTargetSelection[cachedSlug];
      if (cachedSelection != null) {
        _applyTargetSelectionToTable(table, cachedSelection, cachedVariant);
      } else {
        _syncTableRows(table);
      }
      return Promise.resolve(cached);
    }
    return _fetchJson(url).then(function (payload) {
      rowsJsonCache[url] = payload;
      var initial = parseInt(table.dataset.initialRows || "0", 10);
      var collapseAfter = parseInt(table.dataset.collapseAfter || "0", 10);
      var allRows = payload && payload.rows ? payload.rows : [];
      var extraRows = allRows.slice(initial);
      _appendDatasetRows(table, extraRows, initial, collapseAfter);
      table.dataset.rowsLoaded = "all";
      var slug = (table.id || "").replace(/^tbl-/, "");
      var variant = _getVariant(slug);
      var selection = variantTargetSelection[slug];
      if (selection != null) {
        _applyTargetSelectionToTable(table, selection, variant);
      } else {
        _syncTableRows(table);
      }
      return payload;
    });
  }

  /* ── Init ───────────────────────────────────────────────────────────── */
  function init() {
    const cfg = window.leaderboardConfig || {};
    const variants = cfg.variants || [];
    const showAllVariants = !!cfg.showAllVariants;

    _initTargetPickers();

    variants.forEach(function (v) {
      const canvas = document.getElementById("chart-" + v.slug);
      if (canvas) {
        _scheduleChartBuild(canvas, v.slug, cfg);
      }
    });

    _initSortableColumns();
    _initTableExpanders();
    _initSecondaryMetricsNotices();
    _initMobileRowDetails();

    _initChartToggles();
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

    _scheduleDeferredLayout();
    window.addEventListener("resize", _applyModelColumnWidths);
    window.addEventListener("resize", _applyModelTooltips);
    window.addEventListener("resize", _syncSecondaryMetricsPlatform);
    if (window.matchMedia) {
      var mobileChartQuery = window.matchMedia("(max-width: 980px)");
      var syncMobileChartMode = function () {
        Object.values(charts).forEach(_applyChartFilters);
      };
      if (mobileChartQuery.addEventListener) {
        mobileChartQuery.addEventListener("change", syncMobileChartMode);
      } else if (mobileChartQuery.addListener) {
        mobileChartQuery.addListener(syncMobileChartMode);
      }
    }
    _syncSecondaryMetricsPlatform();

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

  function _chartBuildOptions(slug, variant) {
    var metricIndex = variantMetricIndex[slug];
    if (metricIndex == null) metricIndex = _defaultMetricIndex(variant);
    return {
      metricIndex: metricIndex,
      useLogScale: !!variantLogScale[slug],
      metricLabel: _metricLabel(variant, metricIndex),
    };
  }

  function _chartDefaultLogScale(variant) {
    return !!(variant && variant.chart_default_log_scale);
  }

  function _chartHiddenModelSet(variant) {
    var names = (variant && variant.chart_hidden_models) || [];
    var hidden = {};
    names.forEach(function (name) {
      var key = String(name || "").trim().toLowerCase();
      if (key) hidden[key] = true;
    });
    return hidden;
  }

  function _isChartHiddenModel(rowOrPoint, hiddenModels) {
    if (!rowOrPoint || !hiddenModels) return false;
    var names = [rowOrPoint.model_plain, rowOrPoint.model];
    return names.some(function (name) {
      var key = String(name || "").trim().toLowerCase();
      return key && hiddenModels[key];
    });
  }

  function _chartValuesForTarget(slug, variant, metricIndex, chartPoints) {
    var hiddenModels = _chartHiddenModelSet(variant);
    if (chartPoints) {
      return chartPoints.filter(function (p) {
        return !_isChartHiddenModel(p, hiddenModels);
      }).map(function (p) { return p.value; }).filter(function (v) {
        return typeof v === "number" && isFinite(v);
      });
    }
    if (metricIndex === 0) {
      var chartJson = variant.chart_json || "";
      if (chartJson && chartPointsCache[chartJson]) {
        return chartPointsCache[chartJson].filter(function (p) {
          return !_isChartHiddenModel(p, hiddenModels);
        }).map(function (p) { return p.value; }).filter(function (v) {
          return typeof v === "number" && isFinite(v);
        });
      }
    }
    var rowsJson = variant.rows_json || "";
    if (rowsJson && rowsJsonCache[rowsJson] && rowsJsonCache[rowsJson].rows) {
      return _valuesForMetric(rowsJsonCache[rowsJson].rows.filter(function (row) {
        return !_isChartHiddenModel(row, hiddenModels);
      }), metricIndex);
    }
    return _valuesForMetric((variant.rows || []).filter(function (row) {
      return !_isChartHiddenModel(row, hiddenModels);
    }), metricIndex);
  }

  function _syncLogScaleToggle(slug, metricIndex) {
    var variant = _getVariant(slug);
    var canvas = document.getElementById("chart-" + slug);
    if (!canvas) return;
    var wrap = canvas.closest(".chart-plot-wrap");
    var btn = wrap ? wrap.querySelector(".chart-log-toggle") : null;
    if (!btn) return;
    var values = _chartValuesForTarget(slug, variant, metricIndex, null);
    var milestones = _milestonesForTarget(canvas, variant, metricIndex);
    milestones.forEach(function (m) {
      if (typeof m.value === "number" && isFinite(m.value)) values.push(m.value);
    });
    var canLog = values.length > 0 &&
      _allPositive(values) &&
      (_needsSciNotation(values) || _chartDefaultLogScale(variant));
    btn.hidden = !canLog;
    if (!canLog) {
      variantLogScale[slug] = false;
      _writeSession(_sessionKey("log", slug), 0);
      btn.classList.remove("is-on");
      btn.setAttribute("aria-pressed", "false");
      return;
    }
    var isOn = !!variantLogScale[slug];
    btn.classList.toggle("is-on", isOn);
    btn.setAttribute("aria-pressed", isOn ? "true" : "false");
  }

  function _applyMobileTargetColumn(table, metricIndex, label) {
    if (!table) return;
    table.querySelectorAll("th.col-value, td.col-value").forEach(function (cell) {
      var idx = parseInt(cell.getAttribute("data-metric-index") || "0", 10);
      var show = idx === metricIndex;
      cell.classList.toggle("mobile-target-visible", show);
      cell.style.display = "";
    });
    var head = table.closest(".result-table-wrapper");
    head = head ? head.querySelector(".mobile-result-table-head span:nth-child(3)") : null;
    if (head && label) head.textContent = label;
    table.querySelectorAll("tbody tr.result-row").forEach(function (row) {
      var raw = row.getAttribute("data-value-" + metricIndex);
      if (raw != null && raw !== "") row.dataset.value = raw;
    });
  }

  function _metricIndexFromCell(cell) {
    if (!cell) return 0;
    var idx = cell.getAttribute("data-metric-index");
    if (idx != null && idx !== "") return parseInt(idx, 10) || 0;
    var col = cell.getAttribute("data-col") || "";
    if (col === "value") return 0;
    var match = col.match(/^value-(\d+)$/);
    return match ? parseInt(match[1], 10) : 0;
  }

  function _applyFlatTargetColumn(table, metricIndex) {
    if (!table) return;
    table.querySelectorAll("th.col-value, td.col-value").forEach(function (cell) {
      var idx = _metricIndexFromCell(cell);
      cell.classList.toggle("flat-target-visible", idx === metricIndex);
    });
    table.querySelectorAll("tbody tr.result-row").forEach(function (row) {
      var raw = row.getAttribute("data-value-" + metricIndex);
      if (raw != null && raw !== "") row.dataset.value = raw;
    });
  }

  function _rowMetricValue(row, metricIndex) {
    if (!row) return null;
    var raw = row.getAttribute("data-value-" + metricIndex);
    if (raw == null || raw === "") return null;
    var parsed = parseFloat(raw);
    return isNaN(parsed) ? null : parsed;
  }

  function _sortRowsForTarget(table, metricIndex, higherIsBetter) {
    if (!table) return;
    var tbody = table.querySelector("tbody");
    if (!tbody) return;

    var rows = Array.from(tbody.querySelectorAll("tr.result-row"));
    rows.sort(function (a, b) {
      var aVal = _rowMetricValue(a, metricIndex);
      var bVal = _rowMetricValue(b, metricIndex);
      var aMissing = aVal == null || !isFinite(aVal);
      var bMissing = bVal == null || !isFinite(bVal);

      if (aMissing && bMissing) {
        return (parseInt(a.dataset.originalIndex || "0", 10) || 0) -
          (parseInt(b.dataset.originalIndex || "0", 10) || 0);
      }
      if (aMissing) return 1;
      if (bMissing) return -1;
      if (aVal !== bVal) {
        return higherIsBetter ? (bVal - aVal) : (aVal - bVal);
      }
      return (parseInt(a.dataset.originalIndex || "0", 10) || 0) -
        (parseInt(b.dataset.originalIndex || "0", 10) || 0);
    });

    rows.forEach(function (row) {
      tbody.appendChild(row);
    });
  }

  function _applyTargetSelectionToTable(table, selection, variant) {
    if (!table || !variant) return;
    var normalizedSelection = _normalizeTargetSelection(selection, variant);
    var metricIndex = _targetMetricIndex(variant, normalizedSelection);
    var label = _metricLabel(variant, metricIndex);
    var showAll = _isAllTargetSelection(normalizedSelection);

    table.classList.toggle("show-flat-all-metrics", showAll);
    table.classList.toggle("show-secondary-metrics", showAll);

    if (showAll) {
      table.querySelectorAll("th.col-value, td.col-value").forEach(function (cell) {
        cell.classList.remove("flat-target-visible");
        cell.classList.remove("mobile-target-visible");
      });
    } else {
      _applyFlatTargetColumn(table, metricIndex);
    }

    _applyMobileTargetColumn(table, metricIndex, showAll ? "All" : label);
    _sortRowsForTarget(table, metricIndex, variant.higher_is_better !== false);
    _syncTableRows(table);
  }

  function _desktopTargetPickerGroup(slug) {
    var bar = document.querySelector('.leaderboard-section[data-variant="' + slug + '"] .leaderboard-filter-bar');
    return bar ? bar.querySelector(".desktop-target-picker-group") : null;
  }

  function _syncDesktopTargetPickerVisibility(slug, showPicker) {
    var group = _desktopTargetPickerGroup(slug);
    if (group) group.hidden = !showPicker;
  }

  function _flatMetricsToggleBtn(slug) {
    var bar = document.querySelector('.leaderboard-section[data-variant="' + slug + '"] .leaderboard-filter-bar');
    return bar ? bar.querySelector('.flat-metrics-toggle[data-variant="' + slug + '"]') : null;
  }

  function _syncFlatMetricsToggleButton(slug, showAll) {
    var btn = _flatMetricsToggleBtn(slug);
    if (!btn) return;
    btn.classList.toggle("is-on", !!showAll);
    btn.setAttribute("aria-pressed", showAll ? "true" : "false");
    btn.textContent = showAll ? "all metrics" : "+ metrics";
    btn.title = showAll
      ? "Show all target columns in the table"
      : "Show one target column — pick the target below";
  }

  function _applyFlatMetricsMode(table, showAll, slug) {
    if (!table || table.dataset.flatMetrics !== "1") return;
    table.classList.toggle("show-flat-all-metrics", !!showAll);
    table.classList.toggle("show-secondary-metrics", !!showAll);
    if (showAll) {
      table.querySelectorAll("th.col-value, td.col-value").forEach(function (cell) {
        cell.classList.remove("flat-target-visible");
      });
      _syncDesktopTargetPickerVisibility(slug, false);
    } else {
      var metricIndex = variantMetricIndex[slug];
      if (metricIndex == null) {
        var variant = _getVariant(slug);
        metricIndex = _defaultMetricIndex(variant);
      }
      _applyFlatTargetColumn(table, metricIndex);
      _syncDesktopTargetPickerVisibility(slug, true);
    }
    _syncFlatMetricsToggleButton(slug, showAll);
    _writeSession(_sessionKey("flatAll", slug), showAll ? 1 : 0);
  }

  function toggleFlatAllMetrics(enabled, slug) {
    if (!_secondaryMetricsDesktopOnly()) return;
    showFlatAllMetrics = !!enabled;
    document.querySelectorAll('.result-table[data-flat-metrics="1"]').forEach(function (table) {
      var tableSlug = table.closest(".leaderboard-section")?.dataset.variant || slug;
      if (slug && tableSlug !== slug) return;
      _applyFlatMetricsMode(table, showFlatAllMetrics, tableSlug);
    });
    _applyModelColumnWidths();
    _applyModelTooltips();
  }

  function _syncTargetPickers(slug, selection) {
    var variant = _getVariant(slug);
    var normalizedSelection = _normalizeTargetSelection(selection, variant);
    var metricIndex = _targetMetricIndex(variant, normalizedSelection);

    variantTargetSelection[slug] = normalizedSelection;
    variantMetricIndex[slug] = metricIndex;
    _writeSession(_sessionKey("metric", slug), normalizedSelection);

    var chartSelect = document.getElementById("chart-target-" + slug);
    if (chartSelect && chartSelect.value !== normalizedSelection) {
      chartSelect.value = normalizedSelection;
    }

    var table = document.getElementById("tbl-" + slug);
    if (table && table.dataset.flatMetrics === "1") {
      _applyTargetSelectionToTable(table, normalizedSelection, variant);
    }

    var title = document.getElementById("chart-title-" + slug);
    if (title) {
      title.textContent = "SOTA Progression";
    }

    _syncLogScaleToggle(slug, metricIndex);
  }

  function _rebuildChartForTarget(slug) {
    var canvas = document.getElementById("chart-" + slug);
    if (!canvas) return;
    var variant = _getVariant(slug);
    var cfg = window.leaderboardConfig || {};
    var selection = variantTargetSelection[slug];
    if (selection == null) selection = String(variantMetricIndex[slug] != null ? variantMetricIndex[slug] : _defaultMetricIndex(variant));
    var metricIndex = _targetMetricIndex(variant, selection);
    var metrics = variant.metrics || [];
    var milestones = _milestonesForTarget(canvas, variant, metricIndex);
    canvas.dataset.milestones = JSON.stringify(milestones);
    canvas.dataset.metric = _metricLabel(variant, metricIndex);
    if (charts[slug]) {
      charts[slug].destroy();
      delete charts[slug];
    }
    var chartJson = variant.chart_json || "";
    if (chartJson) {
      _fetchChartPoints(chartJson).then(function (points) {
        if (!canvas.isConnected) return;
        buildChart(canvas, slug, cfg.higherIsBetter !== false, points, _chartBuildOptions(slug, variant));
      });
      return;
    }
    buildChart(canvas, slug, cfg.higherIsBetter !== false, null, _chartBuildOptions(slug, variant));
  }

  function _switchTarget(slug, selection) {
    var table = document.getElementById("tbl-" + slug);
    var applySelection = function () {
      _syncTargetPickers(slug, selection);
      _rebuildChartForTarget(slug);
      _applyModelColumnWidths();
    };

    if (table && table.dataset.flatMetrics === "1") {
      _ensureAllRowsLoaded(table).then(applySelection).catch(function (err) {
        console.error("Failed to load leaderboard rows for target switch", err);
        applySelection();
      });
      return;
    }

    applySelection();
  }

  function _initTargetPickers() {
    var cfg = window.leaderboardConfig || {};
    (cfg.variants || []).forEach(function (variant) {
      var slug = variant.slug;
      if (!slug) return;
      var defaultIdx = _defaultMetricIndex(variant);
      var table = document.getElementById("tbl-" + slug);
      var storedSelection = "";
      try {
        storedSelection = sessionStorage.getItem(_sessionKey("metric", slug)) || "";
      } catch (e) {
        storedSelection = "";
      }
      if (!storedSelection) {
        storedSelection = table && table.classList.contains("show-flat-all-metrics") ? "all" : String(defaultIdx);
      }
      storedSelection = _normalizeTargetSelection(storedSelection, variant);
      variantTargetSelection[slug] = storedSelection;
      variantMetricIndex[slug] = _targetMetricIndex(variant, storedSelection);
      variantLogScale[slug] = _chartDefaultLogScale(variant) ||
        _readSessionBool(_sessionKey("log", slug), false);

      var chartSelect = document.getElementById("chart-target-" + slug);
      if (chartSelect && !chartSelect.dataset.bound) {
        chartSelect.dataset.bound = "1";
        chartSelect.addEventListener("change", function () {
          _switchTarget(slug, chartSelect.value);
        });
      }

      if (table && table.dataset.flatMetrics === "1") {
        _syncTargetPickers(slug, storedSelection);
      }

      _syncTargetPickerLabels(variant);
      if (chartSelect) chartSelect.value = storedSelection;
      _syncLogScaleToggle(slug, variantMetricIndex[slug]);
    });
  }

  function toggleLogScale(enabled, slug) {
    if (!slug) return;
    variantLogScale[slug] = !!enabled;
    _writeSession(_sessionKey("log", slug), enabled ? 1 : 0);
    var container = document.querySelector('.chart-container[data-variant="' + slug + '"]');
    var btn = container ? container.querySelector(".chart-log-toggle") : null;
    if (btn) {
      btn.classList.toggle("is-on", !!enabled);
      btn.setAttribute("aria-pressed", enabled ? "true" : "false");
    }
    _rebuildChartForTarget(slug);
  }

  function _initChartToggles() {
    document.querySelectorAll(".chart-log-toggle").forEach(function (btn) {
      if (btn.dataset.logToggleBound) return;
      btn.dataset.logToggleBound = "1";
      btn.addEventListener("click", function () {
        var container = btn.closest(".chart-container");
        var slug = container ? container.dataset.variant : null;
        toggleLogScale(!btn.classList.contains("is-on"), slug);
      });
    });
    document.querySelectorAll(".chart-std-toggle").forEach(function (btn) {
      if (btn.dataset.stdToggleBound) return;
      btn.dataset.stdToggleBound = "1";
      btn.addEventListener("click", function () {
        toggleStd(!btn.classList.contains("is-on"));
      });
    });
    document.querySelectorAll(".chart-baselines-toggle[data-filter='baselines']").forEach(function (btn) {
      if (btn.dataset.baselinesToggleBound) return;
      btn.dataset.baselinesToggleBound = "1";
      btn.addEventListener("click", function () {
        toggleBaselines(!btn.classList.contains("is-on"));
      });
    });
    _syncChartStdToggle(showStd);
    _syncFilterButton("baselines", showBaselines);
  }

  /* ── Secondary-metrics toggle ─────────────────────────────────────── */
  function _secondaryMetricsDesktopOnly() {
    return window.matchMedia("(min-width: 981px)").matches;
  }

  function _showRecordPoint(datum) {
    return !!(datum && datum._isRecord);
  }

  function _syncSecondaryMetricsPlatform() {
    if (!_secondaryMetricsDesktopOnly() && showSecondaryMetrics) {
      var hasFlat = document.querySelector(".dataset-flat-metrics");
      if (!hasFlat) {
        toggleSecondaryMetrics(false);
        return;
      }
    }
    _syncAllSecondaryMetricsViews();
  }

  function _isTableRowExpandPending(table) {
    var collapseAfter = parseInt(table.dataset.collapseAfter || "0", 10);
    if (collapseAfter <= 0) return false;
    var moreBtn = _findMoreButton(table);
    if (!moreBtn || moreBtn.hidden) return false;
    return moreBtn.getAttribute("data-expanded") !== "true";
  }

  function _tableShowsSecondaryCols(table) {
    // Paper pages always render every reported metric. Treat genuinely wide
    // multi-metric tables like the dataset page's expanded metric view.
    if (_secondaryMetricsDesktopOnly() &&
        table.classList.contains("paper-multi-metric-cols") &&
        table.querySelectorAll("thead th.col-value").length > 3) {
      return true;
    }
    if (_secondaryMetricsDesktopOnly() && table.classList.contains("dataset-flat-metrics")) {
      return table.classList.contains("show-flat-all-metrics");
    }
    return _secondaryMetricsDesktopOnly() &&
      table.classList.contains("dataset-multi-metric-cols") &&
      table.classList.contains("show-secondary-metrics") &&
      !table.classList.contains("secondary-metrics-blocked");
  }

  function _findSecondaryMetricsNotice(table) {
    var wrapper = table && table.closest(".result-table-wrapper");
    return wrapper ? wrapper.querySelector(".secondary-metrics-notice") : null;
  }

  function _syncSecondaryMetricsView(table) {
    if (!table || !table.classList.contains("dataset-multi-metric-cols")) return;
    var notice = _findSecondaryMetricsNotice(table);
    if (!_secondaryMetricsDesktopOnly()) {
      table.classList.remove("secondary-metrics-blocked");
      if (notice) notice.hidden = true;
      table.querySelectorAll(".secondary-metrics").forEach(function (block) {
        // CSS reveals this content only when its mobile row is expanded.
        block.hidden = false;
        block.classList.remove("is-visible");
      });
      return;
    }
    var wantsMetrics = table.classList.contains("show-secondary-metrics");
    if (!wantsMetrics) {
      table.classList.remove("secondary-metrics-blocked");
      if (notice) notice.hidden = true;
      table.querySelectorAll(".secondary-metrics").forEach(function (block) {
        block.hidden = true;
        block.classList.remove("is-visible");
      });
      return;
    }
    var blocked = _isTableRowExpandPending(table);
    table.classList.toggle("secondary-metrics-blocked", blocked);
    if (notice) notice.hidden = !blocked;
    table.querySelectorAll(".secondary-metrics").forEach(function (block) {
      var showMobile = !blocked;
      block.hidden = !showMobile;
      block.classList.toggle("is-visible", showMobile);
    });
  }

  function _syncAllSecondaryMetricsViews() {
    document.querySelectorAll(".dataset-multi-metric-cols").forEach(_syncSecondaryMetricsView);
  }

  function toggleSecondaryMetrics(enabled) {
    if (enabled && !_secondaryMetricsDesktopOnly()) {
      return;
    }
    showSecondaryMetrics = !!enabled;
    _syncFilterButton("secondary-metrics", showSecondaryMetrics);
    document.querySelectorAll(".result-table").forEach(function (table) {
      table.classList.toggle("show-secondary-metrics", showSecondaryMetrics);
    });
    document.querySelectorAll(".chart-hover-preview").forEach(function (preview) {
      preview.querySelectorAll(".secondary-metrics").forEach(function (block) {
        block.hidden = !showSecondaryMetrics;
        block.classList.toggle("is-visible", showSecondaryMetrics);
      });
    });
    _syncAllSecondaryMetricsViews();
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
    if (
      archType === "gnn" ||
      archType === "hybrid" ||
      archType === "graph_transformer" ||
      archType === "llm" ||
      archType === "walk"
    ) {
      return archType;
    }
    if (TRADITIONAL_ARCH_TYPES[archType]) return "traditional";
    return null;
  }

  function _isTopNRow(row, n) {
    if (!row || !row.dataset) return false;
    var idx = parseInt(row.dataset.originalIndex, 10);
    return !isNaN(idx) && idx < n;
  }

  function _isDatasetLeaderboardRow(row) {
    var table = row && row.closest(".result-table");
    return !!(table && table.classList.contains("dataset-multi-metric-cols"));
  }

  function _isTopNDatum(slug, datum, n) {
    var row = _findRowForDatum(slug, datum);
    return _isTopNRow(row, n);
  }

  function _rowPassesFilters(row) {
    if (!row) return true;
    if (!showBaselines && row.classList.contains("row-baseline")) {
      if (_isDatasetLeaderboardRow(row) && _isTopNRow(row, TOP_N_ALWAYS_VISIBLE)) {
        /* keep top-N dataset rows */
      } else if (!_isDatasetLeaderboardRow(row) && _isSotaBaselineRow(row)) {
        /* keep SOTA/global-top rows on paper pages */
      } else {
        return false;
      }
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

  function _datumPassesFilters(datum, slug) {
    if (!datum) return false;
    if (!showBaselines && datum.is_baseline && !datum._isRecord) {
      if (slug && _isTopNDatum(slug, datum, TOP_N_ALWAYS_VISIBLE)) {
        /* keep top-N table rows on chart */
      } else {
        return false;
      }
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

  function _finalizeChartUpdate(chart) {
    if (!chart) return;
    var measureLayout = _perfEnabled() && !chart._perfLayoutMeasured;
    var perfPrefix = chart._slug ? "chart-" + chart._slug + ":" : null;
    if (measureLayout && perfPrefix) {
      performance.mark(perfPrefix + "layout-start");
    }
    chart.update("none");
    // Scatter markers reuse element slots by index; after reordering data Chart.js
    // may need a second pass once layout has settled so points and plugins agree.
    requestAnimationFrame(function () {
      if (!chart.canvas || !chart.canvas.isConnected) return;
      chart.update("none");
      if (measureLayout && perfPrefix) {
        chart._perfLayoutMeasured = true;
        performance.mark(perfPrefix + "layout-end");
        performance.measure(perfPrefix + "layout", perfPrefix + "layout-start", perfPrefix + "layout-end");
        _perfChartsPending -= 1;
        if (_perfChartsPending <= 0) {
          _reportPerfSummary();
        }
      }
    });
  }

  function _applyRowFilters() {
    document.querySelectorAll(".result-table").forEach(function (table) {
      _syncTableRows(table);
    });
    Object.values(charts).forEach(function (chart) {
      _applyChartFilters(chart);
      _finalizeChartUpdate(chart);
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
          if (!_secondaryMetricsDesktopOnly()) return;
          toggleSecondaryMetrics(nextOn);
        } else if (key === "flat-all-metrics") {
          if (!_secondaryMetricsDesktopOnly()) return;
          var slug = btn.getAttribute("data-variant") || null;
          toggleFlatAllMetrics(nextOn, slug);
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
    if (!showSecondaryMetrics) {
      clone.querySelectorAll("td.col-value.col-secondary-metric").forEach(function (td) {
        td.remove();
      });
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

  function _pickBestReference(rows, higherIsBetter, families, metricIndex) {
    var wanted = Array.isArray(families) ? families : [families];
    var idx = metricIndex || 0;
    var best = null;
    rows.forEach(function (row) {
      var family = _normalizeModelFamily(row.model_plain || row.model);
      var value = row.metric_values && row.metric_values[idx];
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

  function _oldestRecordValue(recordData) {
    var records = (recordData || []).filter(function (d) {
      return d && d._isRecord && typeof d.y === "number" && isFinite(d.y);
    }).sort(function (a, b) { return a.x - b.x; });
    return records.length ? records[0].y : null;
  }

  // Drop baseline references that are far from the first SOTA and outside the best half.
  function _isRemoteBaselineReference(ref, allVals, oldestBest, higherIsBetter) {
    if (!ref || typeof ref.value !== "number" || !isFinite(ref.value)) return false;
    if (!allVals || !allVals.length) return false;

    var sorted = allVals.slice().sort(function (a, b) { return a - b; });
    var median = _quantile(sorted, 0.5);
    var span = sorted[sorted.length - 1] - sorted[0];
    var closeSpan = Math.max(span * 0.25, 1e-9);

    var outsideTopHalf = higherIsBetter
      ? ref.value < median
      : ref.value > median;
    if (!outsideTopHalf) return false;

    if (oldestBest == null || !isFinite(oldestBest)) return true;
    return Math.abs(ref.value - oldestBest) > closeSpan;
  }

  function _referencesForYScale(references, scatterData, recordData, higherIsBetter) {
    var allVals = (scatterData || []).map(function (d) { return d && d.y; }).filter(function (v) {
      return typeof v === "number" && isFinite(v);
    });
    var oldestBest = _oldestRecordValue(recordData);
    return (references || []).filter(function (ref) {
      return !_isRemoteBaselineReference(ref, allVals, oldestBest, higherIsBetter);
    });
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
      : _quantile(allVals, 0.45);
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

  function _computeFocusedLogYBounds(scatterData, recordData, refs, higherIsBetter) {
    var positiveScatter = (scatterData || []).map(function (d) {
      return d && typeof d.y === "number" && isFinite(d.y) && d.y > 0 ? d.y : null;
    }).filter(function (v) { return v != null; }).sort(function (a, b) { return a - b; });
    var positiveFocus = []
      .concat((recordData || []).map(function (d) {
        return d && typeof d.y === "number" && isFinite(d.y) && d.y > 0 ? d.y : null;
      }).filter(function (v) { return v != null; }))
      .concat((refs || []).map(function (ref) {
        return ref && typeof ref.value === "number" && isFinite(ref.value) && ref.value > 0
          ? ref.value
          : null;
      }).filter(function (v) { return v != null; }));

    if (!positiveScatter.length && !positiveFocus.length) return null;
    if (!positiveFocus.length) positiveFocus = positiveScatter.slice();

    var scatterLogs = positiveScatter.map(function (v) { return Math.log10(v); }).filter(function (v) {
      return typeof v === "number" && isFinite(v);
    });
    var focusLogs = positiveFocus.map(function (v) { return Math.log10(v); }).filter(function (v) {
      return typeof v === "number" && isFinite(v);
    });
    if (!focusLogs.length) return null;

    var minLog = Math.min.apply(null, focusLogs);
    var maxLog = Math.max.apply(null, focusLogs);
    var lowTail = _quantile(scatterLogs, higherIsBetter ? 0.04 : 0.02);
    var highTail = _quantile(scatterLogs, higherIsBetter ? 0.96 : 0.98);
    if (lowTail != null) minLog = Math.min(minLog, lowTail);
    if (highTail != null) maxLog = Math.max(maxLog, highTail);

    if (!(minLog < maxLog) || !isFinite(minLog) || !isFinite(maxLog)) return null;

    var pad = Math.min(0.22, Math.max((maxLog - minLog) * 0.06, 0.08));
    var minVal = Math.pow(10, minLog - pad);
    var maxVal = Math.pow(10, maxLog + pad);

    if (!(minVal > 0) || !(maxVal > minVal)) return null;
    return {
      min: minVal,
      max: maxVal,
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
      fill: "rgba(107,114,128,0.78)",
      stroke: "rgba(75,85,99,0.9)",
      error: "rgba(75,85,99,0.78)",
    };
  }

  function _scatterPointRadius(datum) {
    return datum && (datum._isRecord || datum._isSotaMatch) ? 4 : 3;
  }

  function _scatterPointBorderWidth(datum) {
    return datum && (datum._isRecord || datum._isSotaMatch) ? 2 : 0;
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
      return _datumPassesFilters(d, chart._slug);
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
    chart.data.datasets[0].pointRadius = visibleScatter.map(_scatterPointRadius);
    chart.data.datasets[0].pointHoverRadius = visibleScatter.map(function (d) {
      return _scatterPointRadius(d) + 3;
    });
    chart.data.datasets[0].pointBorderWidth = visibleScatter.map(_scatterPointBorderWidth);

    chart.data.datasets[1].pointBackgroundColor = visibleRecord.map(function (d) {
      return _showRecordPoint(d) ? "#2563eb" : "transparent";
    });
    chart.data.datasets[1].pointRadius = visibleRecord.map(function (d) {
      return _showRecordPoint(d) ? 7 : 0;
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
  function buildChart(canvas, slug, higherIsBetter, chartPoints, buildOptions) {
    buildOptions = buildOptions || {};
    var metricIndex = buildOptions.metricIndex || 0;
    var useLogScale = !!buildOptions.useLogScale;
    var metricLabel = buildOptions.metricLabel || canvas.dataset.metric || "Score";

    let milestones = [];
    try {
      milestones = JSON.parse(canvas.dataset.milestones || "[]");
    } catch (e) { /* ignore */ }

    const cfg = window.leaderboardConfig || {};
    const variant = (cfg.variants || []).find(function (v) { return v.slug === slug; }) || {};
    const allRows = (chartPoints && metricIndex === 0 && !(variant.rows && variant.rows.length))
      ? _chartPointsToRows(chartPoints)
      : (variant.rows && variant.rows.length ? variant.rows : _chartPointsToRows(chartPoints || []));
    const hiddenModels = _chartHiddenModelSet(variant);
    const chartRows = allRows.filter(function (row) {
      return !_isChartHiddenModel(row, hiddenModels);
    });

    if (!milestones.length && !chartRows.length) return;
    if (typeof Chart === "undefined") return;

    var perfPrefix = "chart-" + slug + ":";
    if (_perfEnabled()) {
      performance.mark(perfPrefix + "parse-start");
    }

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
    chartRows.forEach(function (row) {
      if (row.arxiv_id && row.title && !titleByArxiv[row.arxiv_id]) {
        titleByArxiv[row.arxiv_id] = row.title;
      }
    });

    var gnnReference = _pickBestReference(chartRows, higherIsBetter, ["gcn", "gin", "graphsage"], metricIndex);
    var mlpReference = hiddenModels.mlp
      ? null
      : _pickBestReference(chartRows, higherIsBetter, "mlp", metricIndex);

    var recordKeys = {};
    milestones = milestones.filter(function (m) {
      return !_isChartHiddenModel(m, hiddenModels);
    });
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
    chartRows.forEach(function (row) {
      var val = row.metric_values && row.metric_values[metricIndex];
      var std = row.metric_stds && row.metric_stds[metricIndex];
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
        color: _chartCssVar("--chart-reference-gnn", "rgba(15,118,110,0.9)"),
        dash: [8, 4],
        label: gnnReference.label + " " + _formatMetricValue(gnnReference.value),
        position: "below",
      } : null,
      mlpReference ? {
        value: mlpReference.value,
        color: _chartCssVar("--chart-reference-mlp", "rgba(107,114,128,0.9)"),
        dash: [3, 4],
        label: mlpReference.label + " " + _formatMetricValue(mlpReference.value),
        position: "above",
      } : null,
    ].filter(Boolean);
    var scaleReferences = _referencesForYScale(references, scatterData, recordData, higherIsBetter);
    var focusedYBounds = useLogScale
      ? _computeFocusedLogYBounds(scatterData, recordData, scaleReferences, higherIsBetter)
      : _computeFocusedYBounds(scatterData, recordData, scaleReferences, higherIsBetter);

    // ── Per-point styling for records line ────────────────────────────
    var recordBg = recordData.map(function (d) { return _showRecordPoint(d) ? "#2563eb" : "transparent"; });
    var recordRadius = recordData.map(function (d) { return _showRecordPoint(d) ? 7 : 0; });
    var visibleScatterData = scatterData.filter(function (d) {
      return (!useLogScale || d.y > 0) &&
        _isWithinYBounds(d.y, focusedYBounds) &&
        (!d._isStdOutlier || d._isRecord);
    });
    visibleScatterData = visibleScatterData.filter(function (d) {
      return _datumPassesFilters(d, slug);
    });
    visibleScatterData = _sortScatterByPriority(visibleScatterData);
    var visibleRecordData = recordData.filter(function (d) {
      return (!useLogScale || d.y > 0) && _isWithinYBounds(d.y, focusedYBounds);
    });

    if (_perfEnabled()) {
      performance.mark(perfPrefix + "parse-end");
      performance.measure(perfPrefix + "parse", perfPrefix + "parse-start", perfPrefix + "parse-end");
    }

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
        function overlapsAny(box) {
          return placedBoxes.some(function (placed) {
            return box.left < placed.right &&
              box.right > placed.left &&
              box.top < placed.bottom &&
              box.bottom > placed.top;
          });
        }
        function clampLabelBox(box) {
          var dx = 0;
          var dy = 0;
          if (box.left < chartArea.left + 4) dx = chartArea.left + 4 - box.left;
          if (box.right > chartArea.right - 4) dx = chartArea.right - 4 - box.right;
          if (box.top < chartArea.top + 4) dy = chartArea.top + 4 - box.top;
          if (box.bottom > chartArea.bottom - 4) dy = chartArea.bottom - 4 - box.bottom;
          return {
            x: box.x + dx,
            y: box.y + dy,
            left: box.left + dx,
            right: box.right + dx,
            top: box.top + dy,
            bottom: box.bottom + dy,
          };
        }
        function labelBox(x, y, width, height) {
          return {
            x: x,
            y: y,
            left: x,
            right: x + width,
            top: y - height,
            bottom: y + 2,
          };
        }
        function labelPenalty(box, point) {
          var cx = (box.left + box.right) / 2;
          var cy = (box.top + box.bottom) / 2;
          var dx = cx - point.x;
          var dy = cy - point.y;
          return dx * dx + dy * dy;
        }
        function overlapArea(box) {
          return placedBoxes.reduce(function (total, placed) {
            var width = Math.max(0, Math.min(box.right, placed.right) - Math.max(box.left, placed.left));
            var height = Math.max(0, Math.min(box.bottom, placed.bottom) - Math.max(box.top, placed.top));
            return total + width * height;
          }, 0);
        }
        meta.data.forEach(function (point, i) {
          var pd = recordPoints[i];
          if (!_showRecordPoint(pd) || !pd.model) return;
          var label = pd.model + " " + _formatMetricValue(pd.y);
          var width = ctx.measureText(label).width;
          var height = 12;
          var candidates = [
            labelBox(point.x - width - 12, point.y - 8, width, height),
            labelBox(point.x - width - 12, point.y + height + 7, width, height),
            labelBox(point.x - width / 2 - 8, point.y - 15, width, height),
            labelBox(point.x - width / 2 - 8, point.y + height + 14, width, height),
            labelBox(point.x - width - 18, point.y + height + 20, width, height),
            labelBox(point.x + 7, point.y - 8, width, height),
            labelBox(point.x + 7, point.y + height + 7, width, height),
            labelBox(point.x + 14, point.y - 22, width, height),
          ].map(clampLabelBox);
          var chosen = null;
          candidates.some(function (box) {
            if (!overlapsAny(box)) {
              chosen = box;
              return true;
            }
            return false;
          });
          if (!chosen) {
            chosen = candidates.slice().sort(function (a, b) {
              var overlapA = overlapArea(a);
              var overlapB = overlapArea(b);
              if (overlapA !== overlapB) return overlapA - overlapB;
              return labelPenalty(a, point) - labelPenalty(b, point);
            })[0];
          }
          ctx.fillStyle = _chartTheme().labelBg;
          ctx.fillRect(chosen.left - 2, chosen.top - 1, chosen.right - chosen.left + 4, chosen.bottom - chosen.top + 3);
          ctx.fillStyle = _chartTheme().blue;
          ctx.fillText(label, chosen.x, chosen.y);
          placedBoxes.push(chosen);
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
        var trackPerf = _perfEnabled() && !chart._perfLayoutMeasured;
        var t0 = trackPerf ? performance.now() : 0;
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
            if (!_shouldDrawDatumStd(chart, d)) return;
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
            if (!_showRecordPoint(d) || !_shouldDrawDatumStd(chart, d)) return;
            _drawErrorBar(ctx, chartArea, point.x, yScale, d.y, d.std, "rgba(37,99,235,0.7)", 7);
          });
        }

        var hp = chart._highlightedPoint;
        if (hp) {
          var activeDs = chart.data.datasets[hp.datasetIndex];
          var activeMeta = chart.getDatasetMeta(hp.datasetIndex);
          if (activeDs && activeMeta && activeMeta.data && activeMeta.data[hp.index]) {
            var activeDatum = activeDs.data[hp.index];
            var activePoint = activeMeta.data[hp.index];
            if (_shouldDrawDatumStd(chart, activeDatum)) {
              _drawErrorBar(
                ctx, chartArea, activePoint.x, yScale, activeDatum.y, activeDatum.std,
                _semanticPointColors(activeDatum).error, 9
              );
            }
          }
        }
        if (trackPerf) {
          chart._perfErrorBarsMs = (chart._perfErrorBarsMs || 0) + (performance.now() - t0);
        }
      },
    };

    var referenceLinesPlugin = {
      id: "referenceLines_" + slug,
      afterDatasetsDraw: function (chart) {
        var refs = scaleReferences;
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
        var refs = scaleReferences;
        if (!refs.length) return;

        var ctx = chart.ctx;
        var yScale = chart.scales.y;
        var area = chart.chartArea;
        var plotWrap = chart.canvas && chart.canvas.closest(".chart-plot-wrap");
        var labelsOnLeft = !!plotWrap && plotWrap.classList.contains("chart-plot-wrap-lower-is-better");
        ctx.save();
        ctx.font = "600 11px sans-serif";
        var refsByValue = refs.slice().sort(function (a, b) { return b.value - a.value; });
        refs.forEach(function (ref) {
          var py = yScale.getPixelForValue(ref.value);
          if (!isFinite(py) || py < area.top || py > area.bottom) return;
          var textWidth = ctx.measureText(ref.label).width;
          var labelX = labelsOnLeft
            ? area.left + 8
            : Math.max(area.left + 8, area.right - textWidth - 12);
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

    if (_perfEnabled()) {
      performance.mark(perfPrefix + "create-start");
    }
    var chart = new Chart(canvas, {
      type: "scatter",
      data: {
        datasets: [
          {
            label: "All results",
            data: visibleScatterData,
            type: "scatter",
            parsing: {
              xAxisKey: "x",
              yAxisKey: "y",
            },
            backgroundColor: visibleScatterData.map(function (d) {
              return _semanticPointColors(d).fill;
            }),
            borderColor: visibleScatterData.map(function (d) {
              return _semanticPointColors(d).stroke;
            }),
            pointRadius: visibleScatterData.map(_scatterPointRadius),
            pointHoverRadius: visibleScatterData.map(function (d) {
              return _scatterPointRadius(d) + 3;
            }),
            pointBorderWidth: visibleScatterData.map(_scatterPointBorderWidth),
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
            parsing: {
              xAxisKey: "x",
              yAxisKey: "y",
            },
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
        maintainAspectRatio: false,
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
            type: useLogScale ? "logarithmic" : "linear",
            min: focusedYBounds ? focusedYBounds.min : undefined,
            max: focusedYBounds ? focusedYBounds.max : undefined,
            title: { display: true, text: metricLabel, color: _chartTheme().tick },
            ticks: {
              color: _chartTheme().tick,
              callback: function (value) {
                return _formatMetricValue(Number(value));
              },
            },
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
        yearLinesPlugin,
        referenceLinesPlugin,
        errorBarsPlugin,
        referenceLabelsPlugin,
        labelPlugin,
      ],
    });

    if (_perfEnabled()) {
      performance.mark(perfPrefix + "create-end");
      performance.measure(perfPrefix + "create", perfPrefix + "create-start", perfPrefix + "create-end");
    }

    chart._useLogScale = useLogScale;
    chart._metricIndex = metricIndex;
    chart._scatterAll = scatterData.slice();
    chart._recordAll = recordData.slice();
    chart._yBounds = focusedYBounds;
    chart._slug = slug;
    chart._pointCount = scatterData.length;
    chart._isCrowded = scatterData.length > CROWDED_PLOT_THRESHOLD;
    _decorateHistoricalSotaRows(slug, scatterData);
    _applyChartFilters(chart);
    _finalizeChartUpdate(chart);

    charts[slug] = chart;
    _syncLogScaleToggle(slug, metricIndex);
    if (_perfEnabled()) {
      _perfChartsPending += 1;
    }
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

  function _highlightChartRow(slug, row) {
    if (!slug || !row || !charts[slug]) return;
    var arxivId = row.dataset.arxiv;
    var model = row.dataset.model;
    var chart = charts[slug];
    var pointData = chart.data.datasets[0].data || [];
    var idx = pointData.findIndex(function (pd) {
      return pd.arxiv_id === arxivId && pd.model === model;
    });
    if (idx < 0) return;
    chart._highlightedPoint = { datasetIndex: 0, index: idx };
    if (chart.setActiveElements) {
      chart.setActiveElements([{ datasetIndex: 0, index: idx }]);
    }
    chart.update("none");
  }

  function _clearChartRowHighlight(slug) {
    if (!slug || !charts[slug]) return;
    charts[slug]._highlightedPoint = null;
    if (charts[slug].setActiveElements) charts[slug].setActiveElements([]);
    charts[slug].update("none");
  }

  /* ── Table → Chart hover sync ───────────────────────────────────────── */
  function _initTableHover() {
    document.querySelectorAll(".leaderboard-section .result-table tbody").forEach(function (tbody) {
      if (tbody.dataset.hoverDelegated) return;
      tbody.dataset.hoverDelegated = "1";
      var hoveredRow = null;
      tbody.addEventListener("mouseover", function (event) {
        var row = event.target.closest("tr.result-row");
        if (!row || row === hoveredRow) return;
        hoveredRow = row;
        var section = row.closest(".leaderboard-section");
        var slug = section ? section.dataset.variant : null;
        _highlightChartRow(slug, row);
      });
      tbody.addEventListener("mouseout", function (event) {
        var row = event.target.closest("tr.result-row");
        if (!row) return;
        var related = event.relatedTarget;
        if (related && row.contains(related)) return;
        hoveredRow = null;
        var section = row.closest(".leaderboard-section");
        var slug = section ? section.dataset.variant : null;
        _clearChartRowHighlight(slug);
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
      if (btn.dataset.mobileDetailsBound === "1") return;
      btn.dataset.mobileDetailsBound = "1";
      btn.addEventListener("click", function (event) {
        event.stopPropagation(); // prevent the row handler from double-firing
        var row = btn.closest("tr");
        toggleRow(row, btn);
      });
    });

    document.querySelectorAll(".result-table tbody tr.result-row").forEach(function (row) {
      if (row.dataset.mobileDetailsBound === "1") return;
      row.dataset.mobileDetailsBound = "1";
      row.addEventListener("click", function (event) {
        if (event.target.closest("a")) return; // let link clicks through
        var btn = row.querySelector(".mobile-details-toggle");
        if (!btn) return; // no toggle = desktop or no paper column
        toggleRow(row, btn);
      });
    });
  }

  function _cellValue(row, col) {
    if (col === "value" || (col && col.indexOf("value-") === 0)) {
      var valueRaw = row.getAttribute(col === "value" ? "data-value" : ("data-" + col));
      if (valueRaw === "" || valueRaw === null || valueRaw === undefined) return null;
      var numVal = parseFloat(valueRaw);
      return isNaN(numVal) ? valueRaw : numVal;
    }
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
  function toggleWideTable() {
    toggleSecondaryMetrics(!showSecondaryMetrics);
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

      var tableWide = !wrapper.classList.contains("paper-table-narrow-mode") &&
        _tableShowsSecondaryCols(table);
      var isWidePaperMetrics = table.classList.contains("paper-multi-metric-cols") && tableWide;
      // Apply wide-mode sizing before measuring. Otherwise the first pass uses
      // the generic 18ch metric tracks and keeps that excess width cached.
      wrapper.classList.toggle("wide-table-mode", tableWide);
      if (tableWide) {
        wrapper.style.removeProperty("--wide-table-width");
      }
      var isFlatAllMetrics = table.classList.contains("dataset-flat-metrics") &&
        table.classList.contains("show-flat-all-metrics");

      // Calculate model column width based on 90th percentile of content
      var modelCells = Array.from(table.querySelectorAll("tbody td.col-model"));
      var modelLens = modelCells
        .map(function (td) { return (td.innerText || "").replace(/\s+/g, " ").trim().length; })
        .filter(function (n) { return n > 0; })
        .sort(function (a, b) { return a - b; });
      var modelQuantile = tableWide ? 0.72 : 0.88;
      var modelPx = modelLens.length ? _percentile(modelLens, modelQuantile) : 0;
      var modelChars = Math.ceil(modelPx * (tableWide ? 0.88 : 1.08));
      modelChars = Math.max(tableWide ? 7 : 10, Math.min(tableWide ? 12 : 20, modelChars));

      // Calculate value column width (primary metric values only)
      var valueCells = Array.from(table.querySelectorAll("tbody td.col-value.col-primary"));
      var valueChars = 10; // Default
      if (valueCells.length) {
        var valueLens = valueCells
          .map(function (td) { return (td.innerText || "").replace(/\s+/g, " ").trim().length; })
          .filter(function (n) { return n > 0; })
          .sort(function (a, b) { return a - b; });
        if (valueLens.length) {
          var vp90 = _percentile(valueLens, 0.9);
          valueChars = Math.max(8, Math.min(tableWide ? 11 : 10, Math.ceil(vp90 * 1.05 + 1)));
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
        paperChars = Math.max(24, Math.min(tableWide ? 60 : 38, Math.ceil(pp90 * (tableWide ? 1.05 : 0.92))));
      }

      // Set CSS custom properties
      if (tableWide) {
        table.style.setProperty("--model-col-width", modelChars + "ch");
        table.style.setProperty("--value-col-width", valueChars + "ch");
        table.style.setProperty("--paper-col-width", paperChars + "ch");
      } else {
        table.style.setProperty("--model-col-width", Math.min(modelChars, 18) + "ch");
        table.style.setProperty("--value-col-width", Math.min(valueChars, 9) + "ch");
        table.style.setProperty("--paper-col-width", Math.min(paperChars, 30) + "ch");
      }
      _applyRankColumnWidth(table);

      if (tableWide) {
        var viewportCap = Math.max(320, window.innerWidth - 56);
        var fitCap = Math.max(300, viewportCap - 8);
        // Paper result tables have no room to hide the model name: prefer a
        // shorter paper-title column over collapsing it to a handful of glyphs.
        var minPaper = isWidePaperMetrics ? 15 : 24;
        var minModel = isWidePaperMetrics ? 12 : 7;
        var minValue = 7;
        var guard = 0;

        if (!isFlatAllMetrics) {
          while (table.scrollWidth > fitCap && guard < 48) {
            if (modelChars > minModel) {
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

          // Dataset tables benefit from using spare room for their paper title.
          // Paper result tables instead keep natural metric widths so a wide
          // view is centered around the content rather than filling the viewport.
          if (!isWidePaperMetrics) {
            var maxPaper = Math.max(paperChars + 48, 80);
            guard = 0;
            while (table.scrollWidth < fitCap - 2 && paperChars < maxPaper && guard < 96) {
              paperChars += 1;
              table.style.setProperty("--paper-col-width", paperChars + "ch");
              guard += 1;
            }
          }

          guard = 0;
          while (table.scrollWidth > fitCap && paperChars > minPaper && guard < 24) {
            paperChars -= 1;
            table.style.setProperty("--paper-col-width", paperChars + "ch");
            guard += 1;
          }
        }

        var needed = Math.min(viewportCap, table.scrollWidth + 1);
        wrapper.style.setProperty("--wide-table-width", needed + "px");
      } else {
        wrapper.style.removeProperty("--wide-table-width");
      }
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
      var totalRowCount = parseInt(table.dataset.rowCount || String(rows.length), 10);
      var loadedAll = table.dataset.rowsLoaded === "all" || !table.dataset.rowsJson;
      var filterPassingLoaded = rows.filter(_rowPassesFilters).length;
      var canCollapse = collapseAfter > 0 && (
        loadedAll ? filterPassingLoaded > collapseAfter : totalRowCount > collapseAfter
      );
      moreBtn.hidden = !canCollapse;
      moreBtn.setAttribute("aria-expanded", expanded ? "true" : "false");
      if (expanded) {
        moreBtn.textContent = "Hide rows past row " + collapseAfter;
      } else if (loadedAll) {
        moreBtn.textContent = "Show all " + filterPassingLoaded + " rows (" + hiddenCount + " hidden)";
      } else {
        moreBtn.textContent = "Show all " + totalRowCount + " rows (" +
          Math.max(0, totalRowCount - collapseAfter) + " hidden)";
      }
    }

    _applyRankColumnWidth(table);
    _syncSecondaryMetricsView(table);
    if (showSecondaryMetrics) {
      _applyModelColumnWidths();
    }
  }

  function _initSecondaryMetricsNotices() {
    document.querySelectorAll(".secondary-metrics-expand-link").forEach(function (link) {
      if (link.dataset.noticeBound) return;
      link.dataset.noticeBound = "1";
      link.addEventListener("click", function () {
        var wrapper = link.closest(".result-table-wrapper");
        var table = wrapper && wrapper.querySelector(".result-table");
        if (!table) return;
        var moreBtn = _findMoreButton(table);
        if (moreBtn && moreBtn.getAttribute("data-expanded") !== "true") {
          moreBtn.click();
        }
      });
    });
  }

  function _initTableExpanders() {
    document.querySelectorAll("button[data-table-more]").forEach(function (btn) {
      if (btn.dataset.tableMoreBound) return;
      btn.dataset.tableMoreBound = "1";
      btn.addEventListener("click", function () {
        var selector = btn.getAttribute("data-table-more");
        if (!selector) return;
        var table = document.querySelector(selector);
        if (!table) return;
        var expand = btn.getAttribute("data-expanded") !== "true";
        if (expand) {
          btn.disabled = true;
          _ensureAllRowsLoaded(table).then(function () {
            btn.disabled = false;
            btn.setAttribute("data-expanded", "true");
            btn.setAttribute("aria-expanded", "true");
            _syncTableRows(table);
            _scheduleDeferredLayout();
          }).catch(function (err) {
            btn.disabled = false;
            console.error("Failed to load leaderboard rows", err);
          });
          return;
        }
        btn.setAttribute("data-expanded", "false");
        btn.setAttribute("aria-expanded", "false");
        _syncTableRows(table);
      });

      var selector = btn.getAttribute("data-table-more");
      var table = selector ? document.querySelector(selector) : null;
      _syncTableRows(table);
    });
  }

  function _initPaperTableWidthControls() {
    document.querySelectorAll(".paper-table-width-toggle").forEach(function (btn) {
      if (btn.dataset.widthToggleBound) return;
      btn.dataset.widthToggleBound = "1";

      var wrapper = btn.closest(".result-table-outer")?.querySelector(".result-table-wrapper");
      if (!wrapper) return;

      function sync() {
        var narrow = wrapper.classList.contains("paper-table-narrow-mode");
        btn.textContent = narrow ? "Wide view" : "Narrow view";
        btn.setAttribute("aria-pressed", narrow ? "false" : "true");
      }

      btn.addEventListener("click", function () {
        wrapper.classList.toggle("paper-table-narrow-mode");
        _applyModelColumnWidths();
        _applyModelTooltips();
        sync();
      });
      sync();
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
    _initSecondaryMetricsNotices();
    _initMobileRowDetails();
    _initPaperTableWidthControls();
    _applyModelColumnWidths();
    _applyModelTooltips();
    window.addEventListener("resize", function () {
      _applyModelColumnWidths();
      _applyModelTooltips();
    });
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
    if (_perfEnabled()) {
      performance.mark("leaderboard:dom_ready");
    }
    if (window.leaderboardConfig) {
      init();
      _initTableHover();
      if (_perfEnabled()) {
        performance.mark("leaderboard:init_done");
        performance.measure("leaderboard:init", "leaderboard:dom_ready", "leaderboard:init_done");
        if (_perfChartsPending === 0) {
          _reportPerfSummary();
        }
      }
    } else if (document.querySelector(".paper-page .paper-results-table")) {
      initPaperTableUtilities();
    }
  });
})();

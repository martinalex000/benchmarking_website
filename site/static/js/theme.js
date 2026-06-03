/**
 * Theme toggle: persists choice in localStorage; falls back to OS preference.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "theme";

  function getStoredTheme() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (err) {
      return null;
    }
  }

  function systemTheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function resolveTheme() {
    var stored = getStoredTheme();
    return stored === "light" || stored === "dark" ? stored : systemTheme();
  }

  function applyTheme(theme) {
    document.documentElement.dataset.theme = theme;
    var btn = document.getElementById("theme-toggle");
    if (!btn) return;
    var isDark = theme === "dark";
    btn.setAttribute("aria-label", isDark ? "Switch to light mode" : "Switch to dark mode");
    btn.setAttribute("title", isDark ? "Light mode" : "Dark mode");
    btn.setAttribute("aria-pressed", isDark ? "true" : "false");
  }

  function setTheme(theme, persist) {
    applyTheme(theme);
    if (persist) {
      try {
        localStorage.setItem(STORAGE_KEY, theme);
      } catch (err) {
        /* ignore quota / private mode */
      }
    }
    window.dispatchEvent(
      new CustomEvent("sitethemechange", { detail: { theme: theme } })
    );
  }

  function cssVar(name, fallback) {
    var value = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    return value || fallback;
  }

  window.siteChartTheme = function () {
    return {
      tick: cssVar("--chart-tick", "#1f2937"),
      grid: cssVar("--chart-grid", "rgba(31, 41, 55, 0.12)"),
      bar: cssVar("--chart-bar", "rgba(37, 99, 235, 0.72)"),
      barBorder: cssVar("--blue", "#2563eb"),
      miniBar: cssVar("--chart-bar-mini", "rgba(37, 99, 235, 0.55)"),
    };
  };

  window.__applySiteTheme = applyTheme;
  window.__resolveSiteTheme = resolveTheme;

  applyTheme(resolveTheme());

  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.getElementById("theme-toggle");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
      setTheme(next, true);
    });
  });

  var schemeMq = window.matchMedia("(prefers-color-scheme: dark)");
  function onSystemSchemeChange() {
    if (getStoredTheme() === "light" || getStoredTheme() === "dark") return;
    setTheme(systemTheme(), false);
  }
  if (schemeMq.addEventListener) {
    schemeMq.addEventListener("change", onSystemSchemeChange);
  } else if (schemeMq.addListener) {
    schemeMq.addListener(onSystemSchemeChange);
  }
})();

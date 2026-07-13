/**
 * paper-page.js — sticky title bar and MRR explanation popover on paper single pages.
 */
(function () {
  "use strict";

  function initStickyPaperTitle() {
    var titleEl = document.getElementById("paper-page-title");
    var bar = document.getElementById("paper-sticky-title");
    if (!titleEl || !bar || !("IntersectionObserver" in window)) {
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        var titleVisible = entries[0] && entries[0].isIntersecting;
        bar.classList.toggle("is-visible", !titleVisible);
        bar.setAttribute("aria-hidden", titleVisible ? "true" : "false");
      },
      { threshold: 0, rootMargin: "0px" }
    );
    observer.observe(titleEl);
  }

  function initMrrPopover() {
    var btn = document.querySelector(".proposed-model-mrr-btn");
    var popover = document.getElementById("paper-mrr-popover");
    if (!btn || !popover) {
      return;
    }

    function closePopover() {
      popover.hidden = true;
      btn.setAttribute("aria-expanded", "false");
    }

    function openPopover() {
      popover.hidden = false;
      btn.setAttribute("aria-expanded", "true");
    }

    btn.addEventListener("click", function (event) {
      event.stopPropagation();
      if (popover.hidden) {
        openPopover();
      } else {
        closePopover();
      }
    });

    document.addEventListener("click", function (event) {
      if (popover.hidden) {
        return;
      }
      if (popover.contains(event.target) || btn.contains(event.target)) {
        return;
      }
      closePopover();
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        closePopover();
      }
    });
  }

  function initAbstractToggle() {
    var abstract = document.querySelector(".paper-abstract");
    if (!abstract) {
      return;
    }

    var copy = abstract.querySelector(".paper-abstract-copy");
    var text = abstract.querySelector(".paper-abstract-text");
    var button = abstract.querySelector(".paper-abstract-toggle");
    var mobileQuery = window.matchMedia("(max-width: 720px)");
    if (!copy || !text || !button) {
      return;
    }

    function updateToggle() {
      if (!mobileQuery.matches) {
        copy.classList.remove("is-expanded");
        button.hidden = true;
        button.setAttribute("aria-expanded", "false");
        return;
      }

      if (copy.classList.contains("is-expanded")) {
        button.hidden = false;
        return;
      }
      button.hidden = text.scrollHeight <= text.clientHeight + 1;
    }

    function toggle() {
      if (!mobileQuery.matches || button.hidden) {
        return;
      }
      var expanded = copy.classList.toggle("is-expanded");
      button.textContent = expanded ? "Show less" : "Read more";
      button.setAttribute("aria-expanded", String(expanded));
    }

    abstract.addEventListener("click", function (event) {
      if (event.target.closest("a")) {
        return;
      }
      toggle();
    });
    mobileQuery.addEventListener("change", updateToggle);
    window.addEventListener("resize", updateToggle);
    requestAnimationFrame(updateToggle);
  }

  document.addEventListener("DOMContentLoaded", function () {
    if (!document.querySelector(".paper-page")) {
      return;
    }
    initStickyPaperTitle();
    initMrrPopover();
    initAbstractToggle();
  });
})();

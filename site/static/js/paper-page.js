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

  document.addEventListener("DOMContentLoaded", function () {
    if (!document.querySelector(".paper-page")) {
      return;
    }
    initStickyPaperTitle();
    initMrrPopover();
  });
})();

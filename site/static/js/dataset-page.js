(function () {
  "use strict";

  document.querySelectorAll("[data-dataset-research]").forEach(function (container) {
    var button = container.querySelector(".dataset-research-toggle");
    var details = container.querySelector("[data-dataset-research-details]");
    if (!button || !details) return;

    details.hidden = true;
    container.classList.add("is-enhanced");

    button.addEventListener("click", function () {
      var expanded = button.getAttribute("aria-expanded") === "true";
      button.setAttribute("aria-expanded", String(!expanded));
      button.textContent = expanded ? "Show details" : "Hide details";
      details.hidden = expanded;
    });
  });
})();

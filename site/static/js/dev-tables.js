/** Lazy, dependency-free renderer for development-export detail tables. */
(function () {
  "use strict";

  var PAGE_SIZE = 100;

  function cell(value, label) {
    var td = document.createElement("td");
    td.textContent = value == null ? "" : String(value);
    td.dataset.label = label;
    return td;
  }

  function labelStaticTables() {
    document.querySelectorAll(".dev-page table").forEach(function (table) {
      var labels = Array.from(table.querySelectorAll("thead th")).map(function (th) {
        return th.textContent.trim();
      });
      table.querySelectorAll("tbody tr").forEach(function (row) {
        Array.from(row.cells).forEach(function (td, index) {
          if (labels[index]) td.dataset.label = labels[index];
        });
      });
    });
  }

  function renderTable(host, table) {
    var rows = table.rows || [];
    var columns = table.columns || [];
    var controls = document.createElement("div");
    controls.className = "dev-table-controls";
    var search = document.createElement("input");
    search.className = "dev-table-search";
    search.type = "search";
    search.placeholder = "Filter rows";
    var meta = document.createElement("span");
    meta.className = "dev-table-meta";
    controls.append(search, meta);
    var scroll = document.createElement("div");
    scroll.className = "dev-table-scroll";
    var element = document.createElement("table");
    var head = document.createElement("thead");
    var headRow = document.createElement("tr");
    columns.forEach(function (column) {
      var th = document.createElement("th");
      th.textContent = column.label || column.key;
      headRow.appendChild(th);
    });
    head.appendChild(headRow);
    var body = document.createElement("tbody");
    element.append(head, body);
    scroll.appendChild(element);
    var pagination = document.createElement("div");
    pagination.className = "dev-table-controls";
    host.append(controls, scroll, pagination);
    var page = 0;

    function filteredRows() {
      var term = search.value.trim().toLowerCase();
      if (!term) return rows;
      return rows.filter(function (row) {
        return columns.some(function (column) {
          return String(row[column.key] || "").toLowerCase().indexOf(term) !== -1;
        });
      });
    }

    function draw() {
      var filtered = filteredRows();
      var pages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
      page = Math.min(page, pages - 1);
      body.replaceChildren();
      filtered.slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE).forEach(function (row) {
        var tr = document.createElement("tr");
        columns.forEach(function (column) {
          tr.appendChild(cell(row[column.key], column.label || column.key));
        });
        body.appendChild(tr);
      });
      meta.textContent = filtered.length + " matching rows";
      pagination.replaceChildren();
      if (pages > 1) {
        var previous = document.createElement("button");
        previous.className = "dev-table-page";
        previous.textContent = "Previous";
        previous.disabled = page === 0;
        previous.addEventListener("click", function () { page -= 1; draw(); });
        var next = document.createElement("button");
        next.className = "dev-table-page";
        next.textContent = "Next";
        next.disabled = page === pages - 1;
        next.addEventListener("click", function () { page += 1; draw(); });
        var label = document.createElement("span");
        label.className = "dev-table-meta";
        label.textContent = "Page " + (page + 1) + " of " + pages;
        pagination.append(previous, label, next);
      }
    }

    search.addEventListener("input", function () { page = 0; draw(); });
    draw();
  }

  document.addEventListener("DOMContentLoaded", function () {
    labelStaticTables();
    document.querySelectorAll(".dev-json-tables[data-src]").forEach(function (host) {
      fetch(host.dataset.src, { credentials: "same-origin" })
        .then(function (response) {
          if (!response.ok) throw new Error("Could not load development table data");
          return response.json();
        })
        .then(function (payload) {
          host.replaceChildren();
          (payload.tables || []).forEach(function (table) { renderTable(host, table); });
        })
        .catch(function () { host.textContent = "Could not load detailed table data."; });
    });
  });
})();

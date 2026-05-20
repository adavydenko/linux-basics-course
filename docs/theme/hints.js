(function () {
  document.querySelectorAll("[data-hint]").forEach(function (node) {
    if (!node.getAttribute("title")) {
      node.setAttribute("title", node.getAttribute("data-hint"));
    }
  });
})();

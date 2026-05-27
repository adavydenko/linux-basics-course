(function () {
  function addPdfDownloadButton() {
    var buttons = document.querySelector(".right-buttons");
    if (!buttons || document.getElementById("pdf-download-link")) {
      return;
    }

    var script = document.currentScript || document.querySelector('script[src$="pdf-download.js"]');
    var pdfUrl = script ? new URL("../assets/linux-basics-course.pdf", script.src).href : "assets/linux-basics-course.pdf";

    var link = document.createElement("a");
    link.id = "pdf-download-link";
    link.href = pdfUrl;
    link.download = "linux-basics-course.pdf";
    link.title = "Скачать PDF";
    link.setAttribute("aria-label", "Скачать пособие в PDF");

    var icon = document.createElement("i");
    icon.id = "pdf-download-button";
    icon.className = "fa fa-file-pdf-o";
    icon.setAttribute("aria-hidden", "true");

    link.appendChild(icon);
    buttons.insertBefore(link, buttons.firstElementChild);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", addPdfDownloadButton);
  } else {
    addPdfDownloadButton();
  }
})();

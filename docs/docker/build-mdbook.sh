#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-all}"
PDF_FILE="linux-basics-course.pdf"

prepare_build_info() {
  mkdir -p theme

  if [[ ! -f build-info.json ]]; then
    cat > build-info.json <<'EOF'
{
  "version": "dev",
  "commit": "unknown",
  "builtAt": "unknown"
}
EOF
  fi

  if [[ ! -f theme/build-info.js ]]; then
    cat > theme/build-info.js <<'EOF'
window.__BOOK_BUILD_INFO__ = {
  version: "dev",
  commit: "unknown",
  builtAt: "unknown"
};
EOF
  fi
}

prepare_hints() {
  if [[ -x ../scripts/generate-hints-from-glossary.sh ]]; then
    ../scripts/generate-hints-from-glossary.sh \
      "$(pwd)/A1-Glossary/01-Glossary.ru.md" \
      "$(pwd)/hints.toml"
  fi
}

prepare_assets() {
  if [[ -d ../images ]]; then
    mkdir -p images
    cp -R ../images/. images/
  fi
}

build_html() {
  prepare_build_info
  prepare_hints
  prepare_assets
  mdbook build .
}

postprocess_print_html() {
  # Доводка print.html до печатной формы (см. scripts/postprocess-print-html.py):
  # пометить языковой переключатель, обернуть истории-мостики и т.д.
  local script="../scripts/postprocess-print-html.py"
  if [[ -f "$script" ]]; then
    if command -v python3 >/dev/null 2>&1; then
      python3 "$script" book/print.html || true
    else
      echo "postprocess: python3 не найден, пропускаю доводку print.html" >&2
    fi
  fi
}

build_pdf() {
  mkdir -p dist book/assets

  if [[ ! -f book/print.html ]]; then
    echo "book/print.html not found. Run 'build-mdbook html' first, or use 'build-mdbook all'." >&2
    exit 1
  fi

  postprocess_print_html

  weasyprint book/print.html "dist/${PDF_FILE}"
  cp "dist/${PDF_FILE}" "book/assets/${PDF_FILE}"
}

case "$MODE" in
  all)
    build_html
    build_pdf
    ;;
  html)
    build_html
    ;;
  pdf)
    build_pdf
    ;;
  mdbook)
    shift
    exec mdbook "$@"
    ;;
  weasyprint)
    shift
    exec weasyprint "$@"
    ;;
  *)
    exec mdbook "$@"
    ;;
esac

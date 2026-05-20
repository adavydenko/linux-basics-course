#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

IMAGE_TAG="${IMAGE_TAG:-linux-basics-course-mdbook:0.4.52}"
MODE="${1:-all}"
BUILD_VERSION_PREFIX="${BUILD_VERSION_PREFIX:-dev}"

case "$MODE" in
  all|html|pdf)
    ;;
  *)
    echo "Usage: $0 [all|html|pdf]" >&2
    exit 1
    ;;
esac

BUILD_TS="${BUILD_TS:-$(date -u +"%Y-%m-%dT%H:%M:%SZ")}"
BUILD_COMMIT="${BUILD_COMMIT:-$(git rev-parse --short HEAD 2>/dev/null || echo unknown)}"

mkdir -p docs/theme

"$ROOT/scripts/generate-hints-from-glossary.sh"

cat > docs/build-info.json <<EOF
{
  "version": "${BUILD_VERSION_PREFIX}-${BUILD_TS}",
  "commit": "${BUILD_COMMIT}",
  "builtAt": "${BUILD_TS}"
}
EOF

cat > docs/theme/build-info.js <<EOF
window.__BOOK_BUILD_INFO__ = {
  version: "${BUILD_VERSION_PREFIX}-${BUILD_TS}",
  commit: "${BUILD_COMMIT}",
  builtAt: "${BUILD_TS}"
};
EOF

echo "Generated build marker: ${BUILD_VERSION_PREFIX}-${BUILD_TS} (${BUILD_COMMIT})"
echo "Building mdBook Docker image '$IMAGE_TAG'..."
docker build -t "$IMAGE_TAG" docs

echo "Running mdBook Docker build mode: $MODE"
docker run --rm \
  --user "$(id -u):$(id -g)" \
  -v "$ROOT:/workspace" \
  -w /workspace/docs \
  "$IMAGE_TAG" "$MODE"

case "$MODE" in
  all)
    echo "Done. HTML book is in docs/book/"
    echo "PDF written to docs/dist/linux-basics-course.pdf"
    echo "Stable Pages path: docs/book/assets/linux-basics-course.pdf"
    ;;
  html)
    echo "Done. HTML book is in docs/book/"
    ;;
  pdf)
    echo "PDF written to docs/dist/linux-basics-course.pdf"
    echo "Stable Pages path: docs/book/assets/linux-basics-course.pdf"
    ;;
esac

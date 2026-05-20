#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PORT="${PORT:-8088}"

if [[ ! -f "$ROOT/docs/book/index.html" ]]; then
  echo "docs/book/index.html not found. Run ./scripts/build-mdbook.sh html first." >&2
  exit 1
fi

cd "$ROOT/docs/book"
echo "Serving mdBook at http://localhost:${PORT}/"
exec python3 -m http.server "$PORT"

#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GLOSSARY="${1:-$ROOT/docs/A1-Glossary/01-Glossary.ru.md}"
OUTPUT="${2:-$ROOT/docs/hints.toml}"

if [[ ! -f "$GLOSSARY" ]]; then
  echo "Glossary not found: $GLOSSARY" >&2
  exit 1
fi

perl -Mutf8 -CSDA -ne '
	  BEGIN {
	    print "# Generated from docs/A1-Glossary/01-Glossary.ru.md.\n";
	    print "# Do not edit manually; run scripts/generate-hints-from-glossary.sh.\n";
	    $separator = "\n";
	  }

  next unless /^\*\*(.+?)\*\*\s+\x{2014}\s+(.+)$/;

  my ($term, $hint) = ($1, $2);
  for ($term, $hint) {
    s/`//g;
    s/\*\*//g;
    s/^\s+|\s+$//g;
  }

  next if $term eq q{} || $hint eq q{} || $seen{$term}++;

  for ($term, $hint) {
    s/\\/\\\\/g;
    s/"/\\"/g;
  }

	  print $separator;
	  print "[\"$term\"]\n";
	  print "hint = \"$hint\"\n";
	' "$GLOSSARY" > "$OUTPUT"

echo "Generated $OUTPUT from $GLOSSARY"

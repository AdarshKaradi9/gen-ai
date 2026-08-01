#!/bin/sh
# Wraps the artifact source (which ships without <html>/<head>/<body>, since the
# Artifact host supplies them) into a standalone page you can open from disk.
set -e
dir=$(dirname "$0")

{
  cat <<'HEAD'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  *, *::before, *::after { box-sizing: border-box; }
  * { margin: 0; }
  img, svg, video, canvas { display: block; max-width: 100%; }
  button, input, select, textarea { font: inherit; }
</style>
</head>
<body>
HEAD
  cat "$dir/n1-health-optimizer.html"
  printf '\n</body>\n</html>\n'
} > "$dir/n1-health-optimizer.standalone.html"

echo "wrote $dir/n1-health-optimizer.standalone.html"

#!/bin/sh
# Vizney Styles — put a dashboard style in the current project folder.
#
#   curl -fsSL https://styles.vizney.com/install.sh | sh -s -- anthropic
#
# Writes DASHBOARD.md (the spec) to the project root and the dashboard-style skill to
# .claude/skills/dashboard-style/ (SKILL.md with tokens.css, tokens.json, <style>.tps,
# powerbi-theme.json and prompt.md). Nothing else is touched. Re-run with FORCE=1 to replace
# files that already exist. The same files come as a zip on each style's page.
set -eu

style="${1:-}"
base="${VIZNEY_STYLES_BASE:-https://raw.githubusercontent.com/yehwanhwang/vizney-styles/main}"
skill=".claude/skills/dashboard-style"

if [ -z "$style" ]; then
  echo "Usage: curl -fsSL https://styles.vizney.com/install.sh | sh -s -- <style>   (for example: anthropic)" >&2
  echo "Styles: https://styles.vizney.com" >&2
  exit 1
fi
case "$style" in
  *[!a-z0-9-]*) echo "Unknown style: $style" >&2; exit 1 ;;
esac
command -v curl >/dev/null 2>&1 || { echo "curl is required." >&2; exit 1; }

if [ "${FORCE:-0}" != 1 ] && { [ -e DASHBOARD.md ] || [ -e "$skill/SKILL.md" ]; }; then
  echo "DASHBOARD.md or $skill already exists here. Re-run with FORCE=1 to replace them:" >&2
  echo "  curl -fsSL https://styles.vizney.com/install.sh | FORCE=1 sh -s -- $style" >&2
  exit 1
fi

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT INT TERM
fetch() {
  curl -fsSL "$base/$style/$1" -o "$tmp/$2" || { echo "Could not download $style/$1. Is \"$style\" a style on https://styles.vizney.com ?" >&2; exit 1; }
}

fetch DASHBOARD.md DASHBOARD.md
fetch skill/SKILL.md SKILL.md
for f in tokens.css tokens.json "$style.tps" powerbi-theme.json prompt.md; do
  fetch "$f" "$f"
done

mkdir -p "$skill"
mv "$tmp/DASHBOARD.md" DASHBOARD.md
for f in SKILL.md tokens.css tokens.json "$style.tps" powerbi-theme.json prompt.md; do
  mv "$tmp/$f" "$skill/$f"
done

echo "Added the $style dashboard style:"
echo "  DASHBOARD.md                  the spec"
echo "  $skill/   the skill (build, restyle, review) and the tool files"
echo "Ask your agent for a dashboard, for example: \"Build our monthly operations dashboard to DASHBOARD.md.\""
echo "Tableau: paste the palettes in $skill/$style.tps into My Tableau Repository/Preferences.tps."
echo "Power BI: View > Themes > Browse for themes > $skill/powerbi-theme.json."

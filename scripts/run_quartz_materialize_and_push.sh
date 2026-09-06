#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${REPO_DIR:-$HOME/repos/quartz}"
SESSIONS_DIR="${SESSIONS_DIR:-$HOME/Documents/buses/sessions_bus/sessions/daily}"
GENERATED_DIR="${GENERATED_DIR:-$REPO_DIR/content_generated}"
CONTENT_DIR="${CONTENT_DIR:-$REPO_DIR/content}"
# SEED_ROOT_DIR="${SEED_ROOT_DIR:-$REPO_DIR/content_manual_backup}"
SEED_ROOT_DIR="${SEED_ROOT_DIR:-$REPO_DIR/content_}"
BRANCH="${BRANCH:-main}"
COMMIT_PREFIX="${COMMIT_PREFIX:-quartz: refresh materialized sessions}"
INCLUDE_PUBLIC="${INCLUDE_PUBLIC:-0}"

# Keep public sync explicit. Add/remove folders here.
PUBLIC_DIRS=(
  Accounting
  AI
  Automation
  Branding
  Business
  CRM
  Data
  Dev
  month_journals
)

# Force the intended Node/npm toolchain for Quartz
export PATH="$HOME/.n/bin:/usr/local/bin:/usr/bin:/bin"

cd "$REPO_DIR"

echo "[debug] repo=$REPO_DIR"
echo "[debug] sessions_dir=$SESSIONS_DIR"
echo "[debug] node=$(command -v node)"
echo "[debug] node_version=$(node -v)"
echo "[debug] npm=$(command -v npm)"
echo "[debug] npm_version=$(npm -v)"

echo "[1/8] materialize sessions"
python3 tools/materialize_sessions.py \
  --sessions-dir "$SESSIONS_DIR" \
  --output-dir "$GENERATED_DIR" \
  --clean-output

echo "[2/8] seed root files"
mkdir -p "$CONTENT_DIR"
if [[ ! -f "$GENERATED_DIR/index.md" ]]; then
  if [[ -f "$SEED_ROOT_DIR/index.md" ]]; then
    cp "$SEED_ROOT_DIR/index.md" "$GENERATED_DIR/index.md"
  else
    echo "ERROR: missing index.md in both generated and seed root"
    exit 2
  fi
fi

echo "[3/8] sync generated content into content/"
cp "$GENERATED_DIR/index.md" "$CONTENT_DIR/index.md"

for d in "${PUBLIC_DIRS[@]}"; do
  if [[ -d "$GENERATED_DIR/$d" ]]; then
    mkdir -p "$CONTENT_DIR/$d"
    rsync -a --delete "$GENERATED_DIR/$d/" "$CONTENT_DIR/$d/"
  fi
done

echo "[4/8] normalize markdown characters"
find "$CONTENT_DIR" -type f -name '*.md' -print0 | xargs -0 sed -i 's/–/-/g'

echo "[5/8] detect content changes"
if git diff --quiet -- content/; then
  echo "No materialized content changes detected. Exiting cleanly."
  exit 0
fi

echo "[6/8] build quartz"
npm exec quartz build

echo "[7/8] commit changes"
git add content
if [[ "$INCLUDE_PUBLIC" == "1" ]]; then
  git add public
fi

if git diff --cached --quiet; then
  echo "Nothing staged after build. Exiting cleanly."
  exit 0
fi

STAMP="$(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$COMMIT_PREFIX [$STAMP]"

echo "[8/8] push"
git push origin "$BRANCH"

echo "Done."

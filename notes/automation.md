Good — let’s make this repeatable, safe, and auditable. Below I give:

1. a **robust local bash runner** (`deploy_site.sh`) that runs your pipeline in strict sequence, with lockfile, dry-run, safety checks, and a careful commit/push step that never stages `public/`;
2. a short **systemd** unit snippet (optional) so you can run it automatically on the machine; and
3. a sample **GitHub Actions** workflow (optional) to run the same sequence in CI (if you prefer remote automation).

I kept the script conservative by default (requires a clean repo unless you pass `--allow-dirty`) and includes sanity checks so you don’t accidentally commit big data files or the built `public/` folder.

---

## 1) `deploy_site.sh` — local runner (safe, sequential)

Save as `~/bin/deploy_site.sh` (or in repo), make executable `chmod +x deploy_site.sh`.

```bash
#!/usr/bin/env bash
# deploy_site.sh
# Purpose: run data/materialization pipelines in sequence, build the static site with Quartz,
# then create a safe commit and push (never commit public/).
#
# Usage:
#   ./deploy_site.sh \
#       --start 2025-10-05 --end 2025-10-30 \
#       --summary-dir /home/matias/Documents/GPT/data/15_sessions_parsed \
#       --output-dir /home/matias/repos/quartz/content3 \
#       --repo-dir /home/matias/repos/quartz \
#       [--dry-run] [--preview] [--allow-dirty] [--msg "chore(site): ..."]
#
set -euo pipefail

# Defaults
DRY_RUN=false
PREVIEW=false
ALLOW_DIRTY=false
COMMIT_MSG=""
LOCKFILE="/tmp/deploy_site.lock"

function usage {
  cat <<EOF
Usage: $0 --start DATE --end DATE --summary-dir DIR --output-dir DIR --repo-dir DIR [options]

Required:
  --start YYYY-MM-DD
  --end   YYYY-MM-DD
  --summary-dir PATH
  --output-dir PATH
  --repo-dir PATH

Options:
  --dry-run         : Print steps but do not commit or push.
  --preview         : After build run 'npx quartz build --serve' (blocking) for local preview.
  --allow-dirty     : Allow running when repo has local uncommitted changes (dangerous).
  --msg "message"   : Commit message (defaults to chore(site): automated build <timestamp>)
  -h, --help
EOF
  exit 1
}

# Simple arg parsing
while [[ $# -gt 0 ]]; do
  case "$1" in
    --start) START="$2"; shift 2;;
    --end) END="$2"; shift 2;;
    --summary-dir) SUMMARY_DIR="$2"; shift 2;;
    --output-dir) OUTPUT_DIR="$2"; shift 2;;
    --repo-dir) REPO_DIR="$2"; shift 2;;
    --dry-run) DRY_RUN=true; shift;;
    --preview) PREVIEW=true; shift;;
    --allow-dirty) ALLOW_DIRTY=true; shift;;
    --msg) COMMIT_MSG="$2"; shift 2;;
    -h|--help) usage;;
    *) echo "Unknown arg: $1"; usage;;
  esac
done

# required
: "${START:?Missing --start}"
: "${END:?Missing --end}"
: "${SUMMARY_DIR:?Missing --summary-dir}"
: "${OUTPUT_DIR:?Missing --output-dir}"
: "${REPO_DIR:?Missing --repo-dir}"

if [[ -z "$COMMIT_MSG" ]]; then
  COMMIT_MSG="chore(site): automated build content (${START}→${END}) @ $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
fi

# Prevent concurrent runs
if [[ -e "$LOCKFILE" ]]; then
  echo "Lockfile $LOCKFILE exists. Another run may be active. Inspect and remove if stale."
  exit 2
fi
trap 'rm -f "$LOCKFILE"; echo "Lockfile removed";' EXIT
touch "$LOCKFILE"

echo "=== Deploy runner starting ==="
echo "Start: $START  End: $END"
echo "Summary dir: $SUMMARY_DIR"
echo "Materialized output dir: $OUTPUT_DIR"
echo "Repo dir: $REPO_DIR"
echo "Dry run: $DRY_RUN  Preview: $PREVIEW  Allow dirty: $ALLOW_DIRTY"
echo

# Check required commands
for cmd in python3 npx git; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "Required command not found: $cmd" >&2
    exit 3
  fi
done

# Step 0: ensure repo exists and is accessible
if [[ ! -d "$REPO_DIR" ]]; then
  echo "Repo directory not found: $REPO_DIR" >&2
  exit 4
fi

pushd "$REPO_DIR" >/dev/null

# Optional: ensure we are on main (or let user be explicit)
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "Git branch: $CURRENT_BRANCH"

# Check clean working tree unless allowed
if [[ "$ALLOW_DIRTY" != "true" ]]; then
  if [[ -n "$(git status --porcelain)" ]]; then
    echo "Working tree is dirty; please commit/stash changes or run with --allow-dirty" >&2
    exit 5
  fi
fi

popd >/dev/null

# ========== Pipeline sequence ==========
# Run these sequentially; fail fast on error.

echo "1) Running daily aggregator and pipeline (901/902)"
echo "-> python3 901_run_all_daily.py --start $START --end $END"
if [[ "$DRY_RUN" != "true" ]]; then
  python3 901_run_all_daily.py --start "$START" --end "$END"
fi

echo "-> python3 scripts/902_run_pipeline_for_day.py --start $START --end $END"
if [[ "$DRY_RUN" != "true" ]]; then
  python3 scripts/902_run_pipeline_for_day.py --start "$START" --end "$END"
fi

echo "2) Prepare Chroma global"
echo "-> python3 scripts/10_prepare_chroma_global.py"
if [[ "$DRY_RUN" != "true" ]]; then
  python3 scripts/10_prepare_chroma_global.py
fi

echo "3) Materialize content"
echo "-> python3 scripts/20_materialize_content.py --summary-dir $SUMMARY_DIR --output-dir $OUTPUT_DIR"
if [[ "$DRY_RUN" != "true" ]]; then
  python3 scripts/20_materialize_content.py --summary-dir "$SUMMARY_DIR" --output-dir "$OUTPUT_DIR"
fi

# Optional: copy or sync materialized content into repo content path (if different)
# If your quartz content directory is the OUTPUT_DIR, skip this block. Otherwise adapt as needed:
# e.g., rsync -av --delete "$OUTPUT_DIR"/ "$REPO_DIR"/content/
echo "4) Prepare repo: quartz build"
pushd "$REPO_DIR" >/dev/null

# Guardrail: ensure public/ is gitignored
if ! grep -qxF 'public/' .gitignore; then
  echo "Adding public/ to .gitignore"
  if [[ "$DRY_RUN" != "true" ]]; then
    echo 'public/' >> .gitignore
    git add .gitignore
    git commit -m "chore(site): add public/ to .gitignore (automated guardrail)" || true
  fi
fi

echo "Cleaning prior artifacts (public/.quartz-cache public/*)"
if [[ "$DRY_RUN" != "true" ]]; then
  rm -rf public/.quartz-cache public/* || true
fi

echo "Building site: npx quartz build"
if [[ "$DRY_RUN" != "true" ]]; then
  npx quartz build
else
  echo "(dry-run) npx quartz build"
fi

# Sanity checks
if [[ "$DRY_RUN" != "true" ]]; then
  if [[ ! -d public ]]; then
    echo "ERROR: public/ is missing after build" >&2
    exit 6
  fi
  if [[ ! -f public/index.html ]]; then
    echo "ERROR: public/index.html missing after build" >&2
    exit 7
  fi
fi

# Optional preview
if [[ "$PREVIEW" == "true" ]]; then
  echo "Running local preview (blocking): npx quartz build --serve"
  if [[ "$DRY_RUN" != "true" ]]; then
    npx quartz build --serve
  else
    echo "(dry-run) npx quartz build --serve"
  fi
fi

# Git safe push steps
echo "Preparing safe commit"
if [[ "$DRY_RUN" == "true" ]]; then
  echo "(dry-run) skipping git commit/push steps"
  popd >/dev/null
  exit 0
fi

# Re-check repo cleanliness (fail if uncommitted unless allow)
if [[ "$ALLOW_DIRTY" != "true" ]]; then
  if [[ -n "$(git -C "$REPO_DIR" status --porcelain)" ]]; then
    echo "Repo became dirty during the run; please inspect and commit manually or re-run with --allow-dirty" >&2
    exit 8
  fi
fi

# Stage changes but ensure public/ is not staged
git -C "$REPO_DIR" add -A
git -C "$REPO_DIR" restore --staged public || true

# Prevent committing large binary data accidentally
STAGED_LARGE=$(git -C "$REPO_DIR" diff --cached --name-only | grep -E '(\.csv|\.parquet|\.gz|\.zip|\.pdf)$' || true)
if [[ -n "$STAGED_LARGE" ]]; then
  echo "WARNING: large files staged: "
  echo "$STAGED_LARGE"
  echo "Unstage them and commit again. Aborting."
  git -C "$REPO_DIR" restore --staged $STAGED_LARGE || true
  exit 9
fi

# Commit minimally (only content/config changes)
git -C "$REPO_DIR" commit -m "$COMMIT_MSG" || {
  echo "Nothing to commit (no changes) or commit failed."
}

echo "Pushing to origin ($CURRENT_BRANCH)"
git -C "$REPO_DIR" push origin "$CURRENT_BRANCH"

popd >/dev/null

echo "=== Deploy runner finished successfully ==="
```

### Key features / guardrails

* **Lockfile** to prevent parallel runs.
* **Fail-fast** (`set -euo pipefail`) so partial failures don’t go unnoticed.
* **Dry-run** and **preview** flags.
* **.gitignore** guard for `public/` (adds it if missing).
* **Never commit `public/`** — `git restore --staged public` protects you.
* **Check staged large files** (CSV/Parquet/GZ/PDF/ZIP) and abort if present.
* **Requires clean repo** unless `--allow-dirty` is passed (explicit override).
* **Informative commit message** auto-generated with date and the start/end window.
* **Traps** to remove lockfile on exit.

---

## 2) systemd service (optional)

If you want the script to run regularly on the machine, create a systemd unit like this and enable it.

`/etc/systemd/system/deploy-site.service`

```ini
[Unit]
Description=Automated deploy site runner
After=network.target

[Service]
Type=oneshot
User=matias
WorkingDirectory=/home/matias/repos/quartz
ExecStart=/home/matias/bin/deploy_site.sh --start 2025-10-05 --end 2025-10-30 \
  --summary-dir /home/matias/Documents/GPT/data/15_sessions_parsed \
  --output-dir /home/matias/repos/quartz/content3 \
  --repo-dir /home/matias/repos/quartz
TimeoutStartSec=3600
```

Then a timer unit for e.g. daily:
`/etc/systemd/system/deploy-site.timer`

```ini
[Unit]
Description=Daily run of deploy-site

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

Enable it:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now deploy-site.timer
```

(Adjust times and user as needed.)

---

## 3) GitHub Actions workflow (optional CI automation)

If you prefer the pipeline to run in GitHub instead of locally, you can create a workflow `.github/workflows/deploy_site.yml`. It will:

* checkout code, set up Python and Node,
* run the same scripts,
* build with `npx quartz build`,
* commit and push with `GITHUB_TOKEN`.

**Note**: GitHub Actions will run in the repo environment; if your materialization depends on local secrets, local files, or external credentials, adapt the workflow to provide those via `secrets`.

```yaml
name: deploy-site

on:
  workflow_dispatch:
  schedule:
    - cron: '0 3 * * *'  # run daily at 03:00 UTC (adjust)

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      - name: Install npm deps
        run: npm install
      - name: Run pipelines
        env:
          START: 2025-10-05
          END: 2025-10-30
        run: |
          python3 901_run_all_daily.py --start ${START} --end ${END}
          python3 scripts/902_run_pipeline_for_day.py --start ${START} --end ${END}
          python3 scripts/10_prepare_chroma_global.py
          python3 scripts/20_materialize_content.py --summary-dir ./data/15_sessions_parsed --output-dir ./content3
      - name: Build site
        run: npx quartz build
      - name: Commit and push changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git restore --staged public || true
          git commit -m "chore(site): automated build from workflow" || echo "No changes to commit"
          git push origin HEAD:main
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Notes for the Action:

* The action uses `$GITHUB_TOKEN` automatically for pushes (no extra secret required).
* Make sure `data/15_sessions_parsed` is present in the repo or produced by the pipeline in the workflow (or uploaded as artifacts from previous jobs).
* If materialization requires external credentials (APIs, cloud), add appropriate repository secrets and pass them as environment variables.

---

## Quick checklist before you run the script

* Confirm `python3` scripts are runnable in your current environment and virtualenv is activated (if needed).
* Make sure `npx` and `quartz` packages are available (maybe `npm ci` once in repo).
* Backup any uncommitted work or use `--allow-dirty` only if you know what you’re doing.
* Test with `--dry-run` first.

---

## Final short critique / second-look

This automation will pay down a lot of friction — but watch for two common failure modes: (1) **schema drift** in materialized content (the site build will break); add a short post-materialize validator (schema check) to fail early; (2) **silent failures** in Python scripts that leave stale partial content — consider adding atomic swap: write output to `public_tmp/` then `rsync --delete` into `public/`, or use temp dirs and only replace on full success.

If you want, I’ll:

* produce a **tiny validator** that checks the materialized content contains required front-matter keys (title, date, slug) across `.md` files and fail early, or
* produce a **systemd timer + logs** helper that emails (or sends Telegram) if the run fails, or
* adapt the `deploy_site.sh` to **rsync** the materialized content into `REPO_DIR/content/` if your materialization writes somewhere else.

Which of those do you want now? I’ll generate the code immediately.


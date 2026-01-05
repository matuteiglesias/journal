Nice raw trace. Here’s a short read of what happened, then a practical, copy-pasteable runbook you can use to automate the journal update workflow end-to-end.

# Quick inference from the session

* You iterated interactively: installed/used playwright to save auth, activated `new_env`, ran the daily pipelines (`901_run_all_daily.py`, `902_run_pipeline_for_day.py`), prepared Chroma (`10_prepare_chroma_global.py`), materialized content (`20_materialize_content.py`) and built the site (npx quartz / yarn build).
* You used local auth export for OpenAI and a plaintext keyring backend in dev. There were several repeated runs while you debugged environment, deps, and site build issues. You committed and pushed generated content to git and deployed via Vercel/quartz.
* Observed patterns to keep: use of date-range flags on the scripts, repeated local builds, manual "save auth" step with playwright, and repeated git commit/push.

What I want you to watch out for: secrets in the shell history, race conditions if two processes run at once, and pushing incomplete builds if a pipeline fails mid-run. The runbook below fixes those.

# Runbook: automated journal update workflow

The goal: reliably run the ingestion → prepare → materialize → build → push pipeline daily and only push if content changed. The runbook includes safe guards: lockfile, dry-run, logs, retries, secrets handling, and basic alerting.

Parts

1. prerequisites
2. wrapper script (bash) you can copy
3. systemd timer (recommended) and cron alternative
4. GitHub Actions CI example (optional)
5. monitoring and failure modes
6. testing checklist and next improvements

---

# 1 Prerequisites

* Linux machine or server with: conda (or venv), git, python3.11, node, yarn, npx, playwright installed and browsers downloaded.
* A Python environment called `new_env` with required pip deps for your scripts.
* A secure place for secrets: prefer OS keyring, or a secrets manager. If you must use files, keep an `.env` with 600 permissions and never commit it. Do not store API keys in shell history.
* `save_auth.py` (playwright auth) available and able to run non-interactively with saved storage if needed.
* Repository structure known: repo root with `scripts/` containing `901_run_all_daily.py`, `902_run_pipeline_for_day.py`, `10_prepare_chroma_global.py`, `20_materialize_content.py`, surface site repo `repos/quartz` etc.

---

# 2 Wrapper script

Save as `~/bin/journal_update.sh` and `chmod +x`. This script:

* acquires an exclusive lock
* loads secrets safely (example expects `.env` with restricted perms)
* optionally does a dry-run
* runs pipelines in order, logs, detects content diffs, commits and pushes only if there are changes
* returns nonzero on failure

```bash
#!/usr/bin/env bash
set -euo pipefail

# config
REPO_DIR="$HOME/Documents/GPT"            # top-level repo with scripts
QUARTZ_DIR="$HOME/repos/quartz"           # site repo to build
ENV_NAME="new_env"
LOG_DIR="$HOME/logs/journal_update"
LOCKFILE="/tmp/journal_update.lock"
DRY_RUN=0                                  # set 1 to test without pushing
TODAY="$(date +%Y-%m-%d)"
START_DATE="${1:-$TODAY}"                  # optional first arg
END_DATE="${2:-$TODAY}"

mkdir -p "$LOG_DIR"
LOGFILE="$LOG_DIR/run-$TODAY.log"
exec > >(tee -a "$LOGFILE") 2>&1

echo "journal update started at $(date) for $START_DATE..$END_DATE"

# acquire lock using flock
exec 200>"$LOCKFILE"
flock -n 200 || { echo "Another run is in progress. Exiting."; exit 2; }

# load secrets safely
ENV_FILE="$HOME/.journal_update_env"
if [[ -f "$ENV_FILE" ]]; then
  # make sure permissions are restricted
  chmod 600 "$ENV_FILE"
  # shellcheck disable=SC1090
  source "$ENV_FILE"
else
  echo "Env file $ENV_FILE missing. Aborting."
  exit 3
fi

# activate environment
# adapt to your shell/conda setup
if command -v conda >/dev/null 2>&1; then
  source "$(conda info --base)/etc/profile.d/conda.sh"
  conda activate "$ENV_NAME"
else
  # assume python -m venv activation path if you prefer
  source "$HOME/.virtualenvs/$ENV_NAME/bin/activate"
fi

cd "$REPO_DIR"

# optional: run playwright save_auth only if there is no saved auth
# this example assumes save_auth.py writes storage to ~/auth.json when needed
if [[ ! -f "$HOME/auth.json" ]]; then
  echo "Saving browser auth..."
  python3 webtest/save_auth.py || { echo "save_auth failed"; }
fi

# run core pipeline steps (use date args the scripts accept)
echo "Running: 901_run_all_daily.py"
python3 scripts/901_run_all_daily.py --start "$START_DATE" --end "$END_DATE" || { echo "901 failed"; exit 4; }

echo "Running: 902_run_pipeline_for_day.py"
python3 scripts/902_run_pipeline_for_day.py --start "$START_DATE" --end "$END_DATE" || { echo "902 failed"; exit 5; }

echo "Running: 10_prepare_chroma_global.py"
python3 scripts/10_prepare_chroma_global.py || { echo "prepare_chroma failed"; exit 6; }

# materialize content into quartz content dir
echo "Running: 20_materialize_content.py"
python3 scripts/20_materialize_content.py --summary-dir "$REPO_DIR/data/15_sessions_parsed" --output-dir "$QUARTZ_DIR/content/" || { echo "materialize failed"; exit 7; }

# build site (in quartz repo)
cd "$QUARTZ_DIR"
git status --porcelain > /tmp/pre_git_status || true
npx quartz build --no-serve || { echo "quartz build failed"; exit 8; }
# optionally run yarn build if needed:
# yarn build

# only commit if there are changes
if [[ -n "$(git status --porcelain)" ]]; then
  echo "Changes found, committing"
  git add content/
  git commit -m "Automated journal materialization: $START_DATE..$END_DATE"
  if [[ "$DRY_RUN" -eq 0 ]]; then
    git push origin main
    # optional: trigger deploy (vercel/other) if not automatic
    # npx vercel --prebuilt
  else
    echo "DRY RUN: skipping push"
  fi
else
  echo "No changes detected, skipping commit/push"
fi

echo "journal update finished at $(date)"
# release lock by exiting
exit 0
```

Notes

* Create `~/.journal_update_env` with exports like `export OPENAI_API_KEY=...` and `export SOME_OTHER_SECRET=...` and `chmod 600 ~/.journal_update_env`. Prefer OS keyring or secret manager instead. Do not save API keys into shell history.
* The wrapper uses flock to prevent concurrent runs.

---

# 3 Scheduling

Systemd timers recommended (more robust than cron). Two small files.

Service unit `/etc/systemd/system/journal-update.service` (system-wide) or placed in `~/.config/systemd/user/` for user-level:

```ini
[Unit]
Description=Journal update pipeline

[Service]
Type=oneshot
ExecStart=/home/youruser/bin/journal_update.sh
WorkingDirectory=/home/youruser
User=youruser
Environment=PATH=/home/youruser/miniconda3/envs/new_env/bin:/usr/bin:/bin
```

Timer `/etc/systemd/system/journal-update.timer`:

```ini
[Unit]
Description=Run journal update daily at 03:30

[Timer]
OnCalendar=*-*-* 03:30:00
Persistent=true

[Install]
WantedBy=timers.target
```

Enable and start:

```bash
systemctl --user daemon-reload
systemctl --user enable --now journal-update.timer
# check:
systemctl --user status journal-update.timer
journalctl --user -u journal-update.service --since "1 hour ago"
```

Cron alternative (less robust):

```cron
30 3 * * * /home/youruser/bin/journal_update.sh >> /home/youruser/logs/journal_update/cron.log 2>&1
```

---

# 4 GitHub Actions CI alternative

If the pipeline should run from CI (push or scheduled), put a workflow that checks out, runs the scripts, builds, and pushes back to repo. Example `.github/workflows/journal.yml`:

```yaml
name: journal-update
on:
  schedule:
    - cron: '30 6 * * *'   # UTC schedule; adjust for timezone
  workflow_dispatch: {}

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: install deps
        run: |
          python -m pip install -r requirements.txt
      - name: run pipelines
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python3 scripts/901_run_all_daily.py --start $(date +%Y-%m-%d) --end $(date +%Y-%m-%d)
          python3 scripts/902_run_pipeline_for_day.py --start $(date +%Y-%m-%d) --end $(date +%Y-%m-%d)
          python3 scripts/10_prepare_chroma_global.py
          python3 scripts/20_materialize_content.py --summary-dir data/15_sessions_parsed --output-dir repos/quartz/content
      - name: build site
        working-directory: repos/quartz
        run: |
          npm ci
          npx quartz build
      - name: push changes
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "Automated journal update: $(date +%Y-%m-%d)"
          file_pattern: "repos/quartz/content/**"
```

Use GitHub secrets for API keys. CI has nice reproducibility and logs but watch OpenAI usage and rate limits.

---

# 5 Monitoring and failure modes

* Keep logs with rotation. The wrapper writes to `~/logs/journal_update`. Rotate with `logrotate` or a simple cron job.
* On failure, the script exits nonzero. Add a final step to send alerts. Minimal options:

  * send an email via `msmtp` or `sendmail`
  * post a message to a Telegram bot or Slack webhook
  * or create a failure file and let an alerting process poll for it
* Keep a health file `/var/run/journal_update.last_success` updated on success with timestamp. A separate monitor can alert if file older than 36 hours.
* Important failure modes to handle:

  * secrets missing or wrong: script should fail fast with clear message
  * OpenAI rate limit or API error: implement retries with backoff inside the Python scripts. If scripts currently do not have retries, wrap them or add try/except in Python.
  * long runs that exceed timer overlap: flock prevents concurrent runs, but consider a longer schedule window.
  * disk space issues: check `df -h` in pre-run checks.
  * Chroma DB or DB locks: make `10_prepare_chroma_global.py` idempotent and safe for partial runs.

---

# 6 Testing checklist before enabling automation

1. Set `DRY_RUN=1` in wrapper. Run manually for a small date range. Verify no pushes occur.
2. Inspect `LOG_DIR/run-<date>.log`. Confirm steps succeed.
3. Remove `DRY_RUN` and run. Confirm commit/push behavior works and site build is valid.
4. Simulate failure in one step and confirm script exits with nonzero and lock releases.
5. Test systemd timer or GitHub Actions run and confirm logs are recorded and reachable.
6. Confirm secrets are not exposed in logs. If any logs include sensitive output, change scripts to redact.

---

# 7 Suggested immediate improvements (next unlocks)

* Add dry-run flag directly to Python scripts if not present; that makes testing safer.
* Add retry/backoff into any calls that hit external APIs (OpenAI, remote scrapers) and instrument metrics for failure counts.
* Use an OS keyring or Hashicorp Vault for secrets instead of a plaintext `.env`. If you must use `keyrings.alt.file.PlaintextKeyring`, ensure minimal permissions and rotate keys periodically.
* Add a minimal dashboard (static page listing last run status, last success timestamp, last logs) to the quartz site for quick ops checks.
* Add a pull request test step: when content production changes large files, run tests to ensure the deploy pipeline still builds.

---

# Final notes and a minimal checklist to copy-paste and run now

* Create `~/.journal_update_env` with `chmod 600` and add `OPENAI_API_KEY` and other secrets. Do not paste keys into chat.
* Place `journal_update.sh` in `~/bin`, `chmod +x`. Run once manually: `~/bin/journal_update.sh 2025-11-09 2025-11-09` (example) with `DRY_RUN=1` inside the script to test.
* After testing, enable systemd timer or add GitHub Actions if you prefer cloud CI.
* Monitor `~/logs/journal_update/run-*.log`.

If you want, I can:

* produce a one-file systemd user service + timer with your exact paths filled, or
* convert the wrapper into a small Python runner that provides colored logs, retries, and an optional webhook alert on failure.

Tell me which of those you prefer and I’ll generate the exact file(s) ready to paste.


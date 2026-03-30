#!/usr/bin/env python3
"""
setup-auto-mode-permissions.py

One-time script to seed ~/.claude/settings.json with ~67 safe permission rules
equivalent to Claude Code's auto-mode baseline. Run once; idempotent (safe to
re-run — skips rules already present).

Usage:
    python3 setup-auto-mode-permissions.py
    python3 setup-auto-mode-permissions.py --dry-run   # preview without writing
"""

import json
import sys
from pathlib import Path

SETTINGS_PATH = Path.home() / ".claude" / "settings.json"

# ~67 safe, local, reversible permission rules (auto-mode equivalent)
SAFE_PERMISSIONS = [
    # ── Built-in Claude Code tools ────────────────────────────────────────────
    "Read(*)",
    "Edit(*)",
    "Write(*)",
    "Glob(*)",
    "Grep(*)",
    "Agent(*)",
    "Skill(*)",
    "WebSearch(*)",
    "WebFetch(*)",
    "NotebookEdit(*)",
    "TaskCreate(*)",
    "TaskUpdate(*)",

    # ── Git read-only ─────────────────────────────────────────────────────────
    "Bash(git status:*)",
    "Bash(git log:*)",
    "Bash(git diff:*)",
    "Bash(git branch:*)",
    "Bash(git show:*)",
    "Bash(git rev-parse:*)",
    "Bash(git remote -v:*)",
    "Bash(git remote get-url:*)",
    "Bash(git stash list:*)",
    "Bash(git fetch:*)",

    # ── Git write (local, reversible) ─────────────────────────────────────────
    "Bash(git add:*)",
    "Bash(git commit:*)",
    "Bash(git checkout:*)",
    "Bash(git switch:*)",
    "Bash(git merge:*)",
    "Bash(git rebase:*)",
    "Bash(git stash:*)",
    "Bash(git tag:*)",
    "Bash(git worktree:*)",

    # ── Package managers ──────────────────────────────────────────────────────
    "Bash(npm install:*)",
    "Bash(npm ci:*)",
    "Bash(npm test:*)",
    "Bash(npm run:*)",
    "Bash(npm audit:*)",
    "Bash(npx:*)",
    "Bash(pip install:*)",
    "Bash(pip3 install:*)",
    "Bash(cargo build:*)",
    "Bash(cargo test:*)",
    "Bash(go build:*)",
    "Bash(go test:*)",
    "Bash(go mod:*)",

    # ── Build & test ──────────────────────────────────────────────────────────
    "Bash(make:*)",
    "Bash(cmake:*)",
    "Bash(pytest:*)",
    "Bash(python3 -m pytest:*)",

    # ── Common safe shell commands ────────────────────────────────────────────
    "Bash(ls:*)",
    "Bash(pwd:*)",
    "Bash(which:*)",
    "Bash(echo:*)",
    "Bash(cat:*)",
    "Bash(head:*)",
    "Bash(tail:*)",
    "Bash(wc:*)",
    "Bash(sort:*)",
    "Bash(uniq:*)",
    "Bash(find:*)",
    "Bash(dirname:*)",
    "Bash(basename:*)",
    "Bash(realpath:*)",
    "Bash(mkdir:*)",
    "Bash(touch:*)",
    "Bash(cp:*)",
    "Bash(mv:*)",
    "Bash(chmod:*)",
    "Bash(date:*)",
    "Bash(env:*)",
    "Bash(printenv:*)",
    "Bash(file:*)",
    "Bash(stat:*)",
    "Bash(diff:*)",
    "Bash(md5sum:*)",
    "Bash(sha256sum:*)",

    # ── GitHub CLI (read & common write) ──────────────────────────────────────
    "Bash(gh pr view:*)",
    "Bash(gh pr list:*)",
    "Bash(gh pr create:*)",
    "Bash(gh issue view:*)",
    "Bash(gh issue list:*)",
    "Bash(gh repo view:*)",
]


def main():
    dry_run = "--dry-run" in sys.argv

    # Load existing settings (or start fresh)
    if SETTINGS_PATH.exists():
        with open(SETTINGS_PATH) as f:
            settings = json.load(f)
    else:
        settings = {}

    permissions = settings.setdefault("permissions", {})
    allow = permissions.setdefault("allow", [])
    existing = set(allow)

    added = [r for r in SAFE_PERMISSIONS if r not in existing]

    if not added:
        print("Nothing to add — all rules already present.")
        return

    print(f"{'Would add' if dry_run else 'Adding'} {len(added)} rule(s):")
    for rule in added:
        print(f"  + {rule}")

    if dry_run:
        print("\nDry run — no changes written.")
        return

    allow.extend(added)
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=2)
        f.write("\n")

    print(f"\nDone. {len(added)} rule(s) added to {SETTINGS_PATH}")


if __name__ == "__main__":
    main()

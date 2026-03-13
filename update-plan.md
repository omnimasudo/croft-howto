# Docs Sync Update Plan

> Generated: 2026-03-13
> Source: Official Claude Code docs at `code.claude.com/docs/en/`
> Repo version: Last updated February 2026
> Latest Claude Code version: 2.1.74 (March 12, 2026)

---

## Phase 1: Critical Updates (Broken/Misleading Content) ✅ COMPLETED

> **Completed**: 2026-03-13 | **Commit**: `8fe4520`

These items were factually wrong or referenced deprecated/removed features.

### Task 1.1: Fix official docs URL ✅

- **Files modified**: `README.md`, `resources.md`, `CATALOG.md`, `02-memory/README.md`, `claude_concepts_guide.md`, `LEARNING-ROADMAP.md`, `STYLE_GUIDE.md`, `.github/ISSUE_TEMPLATE/config.yml`
- **Change**: Replaced 16 instances of `docs.anthropic.com/en/docs/claude-code` URLs with `code.claude.com/docs/en/` equivalents (with correct subpath mapping per page)

### Task 1.2: Mark `/review` as deprecated ✅

- **File**: `01-slash-commands/README.md`
- **Change**: Marked `/review` as **Deprecated** with `code-review` plugin install instructions

### Task 1.3: Mark `/output-style` as deprecated — SKIPPED

- **Reason**: `/output-style` was not present in the repo. No action needed.

### Task 1.4: Fix model name references ✅

- **File**: `01-slash-commands/README.md`
- **Change**: Fixed "Sonnet 4.5" → "Sonnet 4.6" (only outdated instance found)

### Task 1.5: Mark SSE transport as deprecated — SKIPPED

- **Reason**: Already marked as deprecated in `05-mcp/README.md` line 100. No action needed.

### Task 1.6: Fix `Task()` → `Agent()` rename ✅

- **File**: `04-subagents/README.md`
- **Change**: Updated `Task(agent_type)` → `Agent(agent_type)` in description and YAML example. Added backward-compatibility note about v2.1.63 rename.

### Task 1.7: Resolve `/todos` conflict ✅

- **File**: `01-slash-commands/README.md`
- **Change**: Removed `/todos` from built-in commands table. Verified it is not listed in official docs at `code.claude.com/docs/en/interactive-mode`. `/tasks` already covers task management.

### Task 1.8: Resolve memory hierarchy conflict ✅

- **File**: `02-memory/README.md`
- **Change**: Added verification note that `CLAUDE.local.md` is not mentioned in official docs as of March 2026. Kept the entry (may still work as legacy) with recommendation to use `~/.claude/CLAUDE.md` or `.claude/rules/` for new projects.

---

## Phase 2: Missing Commands & Features (Incomplete Content) ✅ COMPLETED

> **Completed**: 2026-03-13

Content existed but was missing significant features that shipped in Jan–Mar 2026.

### Task 2.1: Add missing built-in commands to slash commands table ✅

- **File modified**: `01-slash-commands/README.md`
- **Change**: Added 15 missing commands (`/btw`, `/chrome`, `/diff`, `/extra-usage`, `/feedback`, `/insights`, `/install-slack-app`, `/keybindings`, `/mobile`, `/passes`, `/reload-plugins`, `/remote-control`, `/skills`, `/stickers`, `/upgrade`) in alphabetical order to the built-in commands table

### Task 2.2: Add bundled skills section ✅

- **File modified**: `03-skills/README.md`
- **Change**: Added "Bundled Skills" section documenting 5 built-in skills (`/simplify`, `/batch`, `/debug`, `/loop`, `/claude-api`) between "Skills vs Other Features" and "Sharing Skills" sections

### Task 2.3: Add `${CLAUDE_SKILL_DIR}` to skills substitutions ✅

- **File modified**: `03-skills/README.md`
- **Change**: Added `${CLAUDE_SKILL_DIR}` row to the String Substitutions table

### Task 2.4: Add missing CLI flags — SKIPPED

- **Reason**: All 19 flags were already documented in `10-cli/README.md` across Core Flags, Model & Configuration, Tool & Permission, Workspace & Directory, MCP Configuration, Session Management, and Advanced Features tables. No action needed.

### Task 2.5: Update MCP OAuth documentation ✅

- **File modified**: `05-mcp/README.md`
- **Changes**: Added `oauth.authServerMetadataUrl` config section, `ENABLE_CLAUDEAI_MCP_SERVERS=false` env var, and updated MCP scope terminology (Local/User with old name notes). 4 items (`--callback-port`, `--client-id`/`--client-secret`, env var expansion, Tool Search) were already present.

### Task 2.6: Add missing built-in subagents — SKIPPED

- **Reason**: "Bash" and "Claude Code Guide" subagents were already fully documented in `04-subagents/README.md` with both table entries and detailed subsections. No action needed.

### Task 2.7: Add `autoMemoryDirectory` and auto-memory settings ✅

- **File modified**: `02-memory/README.md`
- **Changes**: Added `autoMemoryDirectory` setting (v2.1.74), v2.1.59+ version requirement note, and `claudeMdExcludes` setting for monorepos. 2 items (`CLAUDE_CODE_DISABLE_AUTO_MEMORY` env var, Windows managed policy path) were already present.

### Task 2.8: Update effort levels ✅

- **File modified**: `09-advanced-features/README.md`
- **Change**: Added visual effort indicators low (○), medium (◐), high (●) in 3 locations. "max" was never mentioned (no removal needed). "ultrathink" note was already present.

### Task 2.9: Update `/context` command description ✅

- **File modified**: `01-slash-commands/README.md`
- **Change**: Updated `/context` description to "Visualize context usage with actionable optimization suggestions" (combined with Task 2.1)

### Task 2.10: Add hook events update ✅

- **File modified**: `06-hooks/README.md`
- **Changes**: Added 2 missing hook events (`InstructionsLoaded`, `Setup`) to events table (updated count 16→18), added HTTP hooks v2.1.63 version note, documented `once: true` in field reference, added `agent_id`/`agent_type`/`worktree` fields to JSON input, added `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` env var. Items already present: 6 other hook events, `last_assistant_message`, component-scoped hooks.

---

## Phase 3: New Feature Coverage (Content Gaps) ✅ COMPLETED

> **Completed**: 2026-03-13

These are significant features that existed in official docs but had no or minimal corresponding content in the guide. All 8 tasks completed — new tutorial content added.

### Task 3.1: Expand Agent Teams tutorial content ✅

- **File modified**: `04-subagents/README.md`
- **Change**: Expanded Agent Teams section from 25 lines to ~140 lines. Added subagents vs agent teams comparison table, enabling instructions (env var + settings.json), starting a team example, display modes table, Mermaid architecture diagram (Team Lead → Shared Task List → Teammates + Mailbox), task assignment and messaging, plan approval workflow, hook events table (TeammateIdle, TaskCompleted), best practices (5 items), limitations (6 items)

### Task 3.2: Add Scheduled Tasks / `/loop` documentation ✅

- **File modified**: `09-advanced-features/README.md`
- **Change**: Added new "Scheduled Tasks" section (~80 lines) between Background Tasks and Permission Modes. Covers `/loop` command syntax, one-time reminders, CronCreate/CronList/CronDelete tools table, behavior details table (jitter, missed fires, persistence), `CLAUDE_CODE_DISABLE_CRON` env var, deployment monitoring example

### Task 3.3: Add Chrome Integration section ✅

- **File modified**: `09-advanced-features/README.md`
- **Change**: Added new "Chrome Integration" section (~65 lines) between Interactive Features and Remote Control. Covers enabling via `--chrome`/`/chrome`, capabilities table (6 items), site-level permissions, how it works, known limitations (Brave/Arc, WSL, third-party providers)

### Task 3.4: Expand Remote Control section ✅

- **File modified**: `09-advanced-features/README.md`
- **Change**: Expanded Remote Control from 18 lines to ~75 lines. Added version/plan requirements, CLI + REPL commands, flags table (--name, --verbose, --sandbox), 3 connection methods (QR code, URL, find by name), security details, Remote Control vs Claude Code on Web comparison table, limitations

### Task 3.5: Expand Plugin Marketplaces ✅

- **File modified**: `07-plugins/README.md`
- **Change**: Added ~80 lines after existing marketplace section. New subsections: marketplace.json schema with code example and field reference table, plugin source types table (6 sources: relative, GitHub, git URL, git-subdir, npm, pip), distribution methods, strict mode with `strictKnownMarketplaces` allowlist

### Task 3.6: Expand LSP Servers in Plugins ✅

- **File modified**: `07-plugins/README.md`
- **Change**: Expanded LSP section from 15 lines to ~70 lines. Added `.lsp.json` configuration locations, 12-field reference table, 3 example configs (Go/gopls, Python/pyright, TypeScript), available LSP plugins table, LSP capabilities summary

### Task 3.7: Expand Keyboard Shortcuts Customization ✅

- **File modified**: `09-advanced-features/README.md`
- **Change**: Added ~60 lines after existing keyboard shortcuts tables. New subsections: customizing keybindings (`/keybindings` command, v2.1.18+), JSON configuration format example, available contexts table (18 contexts), chord support with keystroke syntax, reserved and conflicting keys table

### Task 3.8: Expand Desktop App ✅

- **File modified**: `09-advanced-features/README.md`
- **Change**: Expanded Desktop App from 20 lines to ~100 lines. Added installation info, core features table (6 features), `.claude/launch.json` app preview config, connectors table (6 connectors), remote/SSH sessions, permission modes table, enterprise features

---

## Phase 4: Reference Document Updates (Cascading Changes)

After Phases 1-3, these reference documents need updates to reflect all changes.

### Task 4.1: Update CATALOG.md

- Sync all command counts (40 → 55+ built-in commands)
- Add bundled skills section
- Update subagent count and types
- Add new hook events
- Update MCP features list
- Add agent teams as new capability

### Task 4.2: Update QUICK_REFERENCE.md

- Add new commands to cheat sheet
- Update model names
- Add bundled skills shortcuts
- Add new CLI flags

### Task 4.3: Update INDEX.md

- Add any new files created in Phase 3
- Update file counts and descriptions
- Verify all cross-references

### Task 4.4: Update LEARNING-ROADMAP.md

- Add agent teams to advanced topics
- Add scheduled tasks to intermediate topics
- Update feature counts
- Update self-assessment quiz if needed

### Task 4.5: Update claude_concepts_guide.md

- Sync all feature descriptions with Phases 1-3 changes
- Update model references
- Add new features to relevant sections

### Task 4.6: Update resources.md

- Fix official docs URL
- Add new official doc pages (agent-teams, scheduled-tasks, chrome, keybindings, etc.)
- Verify all external links still work

---

## Phase 5: Validation (Quality Assurance)

### Task 5.1: Link validation

- Check all internal cross-references between files
- Verify all external URLs (official docs, GitHub, etc.)
- Fix any broken anchor links

### Task 5.2: Mermaid diagram review

- Verify all Mermaid diagrams still render correctly
- Update any diagrams that reference outdated features/flows

### Task 5.3: Conflict marker cleanup

- Review and resolve all `<!-- DOCS-SYNC CONFLICT -->` markers
- Get user confirmation on ambiguous items

### Task 5.4: Consistency check

- Ensure model names are consistent across all files
- Ensure command names match between tables and examples
- Ensure version numbers are consistent

---

## Execution Summary

| Phase | Tasks | Priority | Estimated Effort |
|-------|-------|----------|-----------------|
| **Phase 1** | 8 tasks | ✅ Completed 2026-03-13 | Small edits, 1 subagent batch |
| **Phase 2** | 10 tasks (2 skipped) | ✅ Completed 2026-03-13 | 6 files modified, 2 already complete |
| **Phase 3** | 8 tasks | ✅ Completed 2026-03-13 | 3 files modified, ~612 net lines added |
| **Phase 4** | 6 tasks | Required — cascade reference updates | Medium edits after Phases 1-3 |
| **Phase 5** | 4 tasks | Required — quality gate before merge | Automated + manual review |

**Total**: 36 tasks across 5 phases

---

## Notes

- All changes should preserve the repo's existing style: logo headers, Mermaid diagrams, table formatting, code block language tags, heading hierarchy
- Use `Edit` tool (not `Write`) for modifications to existing files
- Launch parallel subagents per directory for Phase 2-3 efficiency
- Phase 4 must run sequentially after Phases 1-3 since reference docs depend on category content

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

## Phase 3: New Feature Coverage (Content Gaps)

These are significant features that exist in official docs but have no corresponding content in the guide. Each needs a decision: create tutorial content, add a TODO note, or skip.

### Task 3.1: Create Agent Teams tutorial content

- **Directory**: `04-subagents/README.md` (add section) or new file
- **Content needed**:
  - What agent teams are vs. subagents (comparison table)
  - How to enable (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`)
  - Starting a team, display modes (in-process vs tmux)
  - Task assignment, teammate messaging, plan approval
  - Architecture: team lead, teammates, shared task list, mailbox
  - Best practices: team size (3-5), task sizing, file conflict avoidance
  - Limitations (experimental, no session resumption, no nested teams)
- **Priority**: High — major new capability
- **Source**: `code.claude.com/docs/en/agent-teams`

### Task 3.2: Create Scheduled Tasks / `/loop` documentation

- **Directory**: `09-advanced-features/README.md` (add section)
- **Content needed**:
  - `/loop [interval] <prompt>` command usage
  - Cron scheduling tools for recurring prompts
  - `CLAUDE_CODE_DISABLE_CRON` env var
  - Use cases: polling deploys, babysitting PRs
- **Priority**: Medium — useful automation feature
- **Source**: `code.claude.com/docs/en/scheduled-tasks`

### Task 3.3: Create Chrome Integration section

- **Directory**: `09-advanced-features/README.md` (add section)
- **Content needed**:
  - `--chrome` / `--no-chrome` flags
  - `/chrome` command for configuration
  - Browser debugging and web testing capabilities
- **Priority**: Medium — beta feature but useful for web developers
- **Source**: `code.claude.com/docs/en/chrome`

### Task 3.4: Create Remote Control section

- **Directory**: `09-advanced-features/README.md` (add section or expand existing)
- **Content needed**:
  - `/remote-control` command (alias `/rc`)
  - `claude remote-control` CLI subcommand
  - Controlling local sessions from claude.ai or Claude app
  - Optional name argument for custom session titles
- **Priority**: Medium — enables mobile/cross-device workflows
- **Source**: `code.claude.com/docs/en/remote-control`

### Task 3.5: Document Plugin Marketplaces

- **File**: `07-plugins/README.md` (add section)
- **Content needed**:
  - Creating and distributing plugin marketplaces
  - Official marketplace submission (claude.ai/settings/plugins/submit)
  - `/plugin marketplace` commands
  - `strictKnownMarketplaces`, `extraKnownMarketplaces` settings
- **Priority**: Medium — plugin ecosystem is maturing
- **Source**: `code.claude.com/docs/en/plugin-marketplaces`, `code.claude.com/docs/en/discover-plugins`

### Task 3.6: Document LSP Servers in Plugins

- **File**: `07-plugins/README.md` (add section)
- **Content needed**:
  - `.lsp.json` configuration format
  - Language server setup for code intelligence
  - Example Go/Python/TypeScript LSP configs
- **Priority**: Low — niche feature, official marketplace covers common languages
- **Source**: `code.claude.com/docs/en/plugins-reference#lsp-servers`

### Task 3.7: Document Keyboard Shortcuts Customization

- **File**: `09-advanced-features/README.md` (add section)
- **Content needed**:
  - `/keybindings` command
  - `~/.claude/keybindings.json` configuration
  - Available keybinding actions (voice:pushToTalk, chat:newline, etc.)
  - Context-aware bindings, chord support
- **Priority**: Low — power user feature
- **Source**: `code.claude.com/docs/en/keybindings`

### Task 3.8: Document Desktop App

- **File**: `09-advanced-features/README.md` (expand existing mention)
- **Content needed**:
  - Download links (macOS, Windows, Windows ARM64)
  - `/desktop` command to hand off session
  - Visual diff review, multiple sessions, cloud session management
- **Priority**: Low — mentioned briefly already, needs expansion
- **Source**: `code.claude.com/docs/en/desktop`, `code.claude.com/docs/en/desktop-quickstart`

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
| **Phase 3** | 8 tasks | Valuable — new feature tutorials | New content creation, 3-4 subagent batches |
| **Phase 4** | 6 tasks | Required — cascade reference updates | Medium edits after Phases 1-3 |
| **Phase 5** | 4 tasks | Required — quality gate before merge | Automated + manual review |

**Total**: 36 tasks across 5 phases

---

## Notes

- All changes should preserve the repo's existing style: logo headers, Mermaid diagrams, table formatting, code block language tags, heading hierarchy
- Use `Edit` tool (not `Write`) for modifications to existing files
- Launch parallel subagents per directory for Phase 2-3 efficiency
- Phase 4 must run sequentially after Phases 1-3 since reference docs depend on category content

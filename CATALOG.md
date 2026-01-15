# Claude Code Feature Catalog

> Quick reference guide to all Claude Code features: commands, agents, skills, plugins, and hooks.

**Navigation**: [Commands](#-slash-commands) | [Sub-Agents](#-sub-agents) | [Skills](#-skills) | [Plugins](#-plugins) | [MCP Servers](#-mcp-servers) | [Hooks](#-hooks)

---

## Slash Commands

Commands are user-invoked shortcuts that execute specific actions.

### Built-in Commands

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/help` | Show help information | Get started, learn commands |
| `/clear` | Clear conversation history | Start fresh, reduce context |
| `/model` | Switch AI model | Change performance/cost |
| `/config` | View/edit configuration | Customize behavior |
| `/status` | Show session status | Check current state |
| `/agents` | List available agents | See delegation options |
| `/skills` | List available skills | See auto-invoke capabilities |
| `/hooks` | List configured hooks | Debug automation |
| `/mcp` | List MCP servers | Check external integrations |
| `/memory` | View loaded memory files | Debug context loading |
| `/plugin` | Manage plugins | Install/remove extensions |
| `/plan` | Enter planning mode | Complex implementations |
| `/rewind` | Rewind to checkpoint | Undo changes, explore alternatives |
| `/checkpoint` | Manage checkpoints | Save/restore states |
| `/cost` | Show token usage costs | Monitor spending |
| `/context` | Show context window usage | Manage conversation length |
| `/export` | Export conversation | Save for reference |
| `/login` | Authenticate with Anthropic | Access features |
| `/logout` | Sign out | Switch accounts |
| `/sandbox` | Toggle sandbox mode | Safe command execution |
| `/vim` | Toggle vim mode | Vim-style editing |
| `/doctor` | Run diagnostics | Troubleshoot issues |
| `/release-notes` | Show release notes | Check new features |
| `/permissions` | Manage permissions | Control access |
| `/session` | Manage sessions | Multi-session workflows |
| `/rename` | Rename current session | Organize sessions |
| `/resume` | Resume previous session | Continue work |
| `/todo` | View/manage todo list | Track tasks |
| `/tasks` | View background tasks | Monitor async operations |

### Custom Commands (Examples)

| Command | Description | When to Use | Tokens | Scope | Installation |
|---------|-------------|-------------|--------|-------|--------------|
| `/optimize` | Analyze code for optimization | Performance improvement | ~500 | Project | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | Prepare pull request | Before submitting PRs | ~400 | Project | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | Generate API documentation | Document APIs | ~600 | Project | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | Create git commit with context | Commit changes | ~300 | User | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | Stage, commit, and push | Quick deployment | ~400 | User | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | Restructure documentation | Improve docs | ~500 | Project | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | Setup CI/CD pipeline | New projects | ~800 | Project | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | Expand test coverage | Improve testing | ~600 | Project | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **Tokens**: Estimated context consumed when command is loaded. **Scope**: `User` = personal workflows (`~/.claude/`), `Project` = team-shared (`.claude/`)

**Reference**: [01-slash-commands/](01-slash-commands/) | [Official Docs](https://docs.anthropic.com/en/docs/claude-code/slash-commands)

**Quick Install (All Custom Commands)**:
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## Sub-Agents

Specialized AI assistants with isolated contexts for specific tasks.

### Built-in Sub-Agents

| Agent | Description | Tools | Model | When to Use |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | Multi-step tasks, research | All tools | Sonnet | Complex research, multi-file tasks |
| **Explore** | Codebase exploration | Read, Glob, Grep | Haiku | Quick searches, understanding code |
| **Plan** | Implementation planning | Read, Glob, Grep, Bash | Sonnet | Architecture design, planning |
| **Bash** | Command execution | Bash | Sonnet | Git operations, terminal tasks |
| **code-reviewer** | Code quality analysis | Read, Glob, Grep | Sonnet | PR reviews, quality checks |
| **code-architect** | Feature architecture design | Read, Glob, Grep, LS | Sonnet | New feature planning |
| **code-explorer** | Deep codebase analysis | Read, Glob, Grep, LS | Sonnet | Understanding existing features |
| **clean-code-reviewer** | Clean Code principles | Read, Grep, Glob, Bash | Sonnet | Maintainability review |

### Custom Sub-Agents (Examples)

| Agent | Description | When to Use | Tokens | Scope | Installation |
|-------|-------------|-------------|--------|-------|--------------|
| `code-reviewer` | Comprehensive code quality | Code review sessions | ~800 | Project | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `test-engineer` | Test strategy & coverage | Test planning | ~700 | Project | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | Technical documentation | API docs, guides | ~600 | Project | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | Security-focused review | Security audits | ~900 | Project | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | Full feature implementation | Feature development | ~1000 | Project | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | Root cause analysis | Bug investigation | ~700 | User | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL queries, data analysis | Data tasks | ~600 | User | `cp 04-subagents/data-scientist.md .claude/agents/` |

> **Tokens**: Estimated context consumed when agent is invoked. **Scope**: `User` = personal (`~/.claude/agents/`), `Project` = team-shared (`.claude/agents/`)

**Reference**: [04-subagents/](04-subagents/) | [Official Docs](https://docs.anthropic.com/en/docs/claude-code/sub-agents)

**Quick Install (All Custom Agents)**:
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## Skills

Auto-invoked capabilities with instructions, scripts, and templates.

### Example Skills

| Skill | Description | When Auto-Invoked | Tokens | Scope | Installation |
|-------|-------------|-------------------|--------|-------|--------------|
| `code-review` | Comprehensive code review | "Review this code", "Check quality" | ~2000 | Project | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | Brand consistency checker | Writing marketing copy | ~1200 | Project | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | API documentation generator | "Generate docs", "Document API" | ~1500 | Project | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | Systematic code refactoring (Martin Fowler) | "Refactor this", "Clean up code" | ~3000 | User | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **Tokens**: Estimated context when skill + references loaded. **Scope**: `User` = personal (`~/.claude/skills/`), `Project` = team-shared (`.claude/skills/`)

### Skill Structure

```
~/.claude/skills/skill-name/
├── SKILL.md          # Skill definition & instructions
├── scripts/          # Helper scripts
└── templates/        # Output templates
```

**Reference**: [03-skills/](03-skills/) | [Official Docs](https://docs.anthropic.com/en/docs/claude-code/skills)

**Quick Install (All Skills)**:
```bash
cp -r 03-skills/* ~/.claude/skills/
```

---

## Plugins

Bundled collections of commands, agents, MCP servers, and hooks.

### Example Plugins

| Plugin | Description | Components | When to Use | Tokens | Scope | Installation |
|--------|-------------|------------|-------------|--------|-------|--------------|
| `pr-review` | PR review workflow | 3 commands, 3 agents, GitHub MCP | Code reviews | ~5000 | Project | `/plugin install pr-review` |
| `devops-automation` | Deployment & monitoring | 4 commands, 3 agents, K8s MCP | DevOps tasks | ~6000 | Project | `/plugin install devops-automation` |
| `documentation` | Doc generation suite | 4 commands, 3 agents, templates | Documentation | ~4000 | Project | `/plugin install documentation` |

> **Tokens**: Total context when all plugin components loaded. **Scope**: `Project` = team-shared, `User` = personal workflows

### Plugin Structure

```
.claude-plugin/
├── plugin.json       # Manifest file
├── commands/         # Slash commands
├── agents/           # Sub-agents
├── skills/           # Skills
├── mcp/              # MCP configurations
├── hooks/            # Hook scripts
└── scripts/          # Utility scripts
```

**Reference**: [07-plugins/](07-plugins/) | [Official Docs](https://docs.anthropic.com/en/docs/claude-code/plugins)

**Plugin Management Commands**:
```bash
/plugin list              # List installed plugins
/plugin install <name>    # Install plugin
/plugin remove <name>     # Remove plugin
/plugin update <name>     # Update plugin
```

---

## MCP Servers

Model Context Protocol servers for external tool and API access.

### Common MCP Servers

| Server | Description | When to Use | Tokens | Scope | Installation |
|--------|-------------|-------------|--------|-------|--------------|
| **GitHub** | PR management, issues, code | GitHub workflows | ~200 | Project | `cp 05-mcp/github-mcp.json .claude/mcp.json` |
| **Database** | SQL queries, data access | Database operations | ~150 | Project | `cp 05-mcp/database-mcp.json .claude/mcp.json` |
| **Filesystem** | Advanced file operations | Complex file tasks | ~100 | User | `cp 05-mcp/filesystem-mcp.json .claude/mcp.json` |
| **Slack** | Team communication | Notifications, updates | ~150 | Project | Configure in settings |
| **Google Docs** | Document access | Doc editing, review | ~200 | Project | Configure in settings |
| **Asana** | Project management | Task tracking | ~150 | Project | Configure in settings |
| **Stripe** | Payment data | Financial analysis | ~200 | Project | Configure in settings |
| **Memory** | Persistent memory | Cross-session recall | ~100 | User | Configure in settings |
| **Context7** | Library documentation | Up-to-date docs lookup | ~50 | Built-in | Built-in |

> **Tokens**: Config overhead (tool calls add more). **Scope**: `Project` = team (`.claude/mcp.json`), `User` = personal (`~/.claude/mcp.json`)

### MCP Configuration Example

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Reference**: [05-mcp/](05-mcp/) | [MCP Protocol Docs](https://modelcontextprotocol.io)

**Quick Install (GitHub MCP)**:
```bash
export GITHUB_TOKEN="your_token" && cp 05-mcp/github-mcp.json .claude/mcp.json
```

---

## Hooks

Event-driven automation that executes shell commands on Claude Code events.

### Hook Events

| Event | Description | When Triggered | Use Cases |
|-------|-------------|----------------|-----------|
| `PreToolUse` | Before tool execution | Before any tool runs | Validation, logging |
| `PostToolUse` | After tool completion | After any tool completes | Formatting, notifications |
| `PermissionRequest` | Permission dialog shown | Before sensitive actions | Custom approval flows |
| `UserPromptSubmit` | Before prompt processing | User sends message | Input validation |
| `Notification` | Notification sent | Claude sends notification | External alerts |
| `Stop` | Agent finishes responding | Response complete | Cleanup, reporting |
| `SubagentStop` | Subagent finishes | Subagent task complete | Chain actions |
| `PreCompact` | Before compact operation | Context compression | State preservation |
| `SessionStart` | Session begins/resumes | Session initialization | Setup tasks |

### Example Hooks

| Hook | Description | Event | Tokens | Scope | Installation |
|------|-------------|-------|--------|-------|--------------|
| `validate-bash.py` | Command validation | PreToolUse:Bash | ~50 | Project | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | Security scanning | PostToolUse:Write | ~50 | Project | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | Auto-formatting | PostToolUse:Write | ~30 | User | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | Prompt validation | UserPromptSubmit | ~50 | Project | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | Token usage tracking | Stop | ~40 | User | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | Pre-commit validation | PreToolUse:Bash | ~30 | Project | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | Command logging | PostToolUse:Bash | ~20 | User | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |

> **Tokens**: Config overhead only (scripts run externally). **Scope**: `Project` = team (`.claude/settings.json`), `User` = personal (`~/.claude/settings.json`)

### Hook Configuration

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "~/.claude/hooks/validate-bash.py"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "~/.claude/hooks/format-code.sh"
      }
    ]
  }
}
```

**Reference**: [06-hooks/](06-hooks/) | [Official Docs](https://docs.anthropic.com/en/docs/claude-code/hooks)

**Quick Install (All Hooks)**:
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## Memory Files

Persistent context loaded automatically across sessions.

### Memory Types

| Type | Location | Scope | Tokens | When to Use |
|------|----------|-------|--------|-------------|
| **Project Memory** | `./CLAUDE.md` | Project (team) | ~500-2000 | Team standards, project rules |
| **Directory Memory** | `./src/api/CLAUDE.md` | Directory | ~200-500 | Module-specific rules |
| **Personal Memory** | `~/.claude/CLAUDE.md` | User (personal) | ~300-1000 | Personal preferences |

> **Tokens**: Varies by content length (auto-loaded every session). Keep memory files concise to preserve context for actual work.

**Reference**: [02-memory/](02-memory/) | [Official Docs](https://docs.anthropic.com/en/docs/claude-code/memory)

**Quick Install**:
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## Quick Reference Matrix

### Feature Selection Guide

| Need | Recommended Feature | Why |
|------|---------------------|-----|
| Quick shortcut | Slash Command | Manual, immediate |
| Persistent context | Memory | Auto-loaded |
| Complex automation | Skill | Auto-invoked |
| Specialized task | Sub-Agent | Isolated context |
| External data | MCP Server | Real-time access |
| Event automation | Hook | Event-triggered |
| Complete solution | Plugin | All-in-one bundle |

### Installation Priority

| Priority | Feature | Command |
|----------|---------|---------|
| 1. Essential | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. Daily Use | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. Quality | Sub-Agents | `cp 04-subagents/*.md .claude/agents/` |
| 4. Automation | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. External | MCP | `cp 05-mcp/github-mcp.json .claude/mcp.json` |
| 6. Advanced | Skills | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. Complete | Plugins | `/plugin install pr-review` |

---

## Complete One-Command Installation

Install all examples from this repository:

```bash
# Create directories
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# Install all features
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## Additional Resources

- [Official Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Learning Roadmap](LEARNING-ROADMAP.md)
- [Main README](README.md)

---

**Last Updated**: January 2026

# Claude Code Examples - Complete Index

This document provides a complete index of all example files organized by feature type.

## Summary Statistics

- **Total Files**: 71 files
- **Categories**: 6 feature categories
- **Plugins**: 3 complete plugins
- **Skills**: 3 complete skills
- **Ready to Use**: All examples

---

## 📁 01. Slash Commands (4 files)

User-invoked shortcuts for common workflows.

| File | Description | Use Case |
|------|-------------|----------|
| `optimize.md` | Code optimization analyzer | Find performance issues |
| `pr.md` | Pull request preparation | PR workflow automation |
| `generate-api-docs.md` | API documentation generator | Generate API docs |
| `README.md` | Documentation | Setup and usage guide |

**Installation Path**: `.claude/commands/`

**Usage**: `/optimize`, `/pr`, `/generate-api-docs`

---

## 🤖 02. Subagents (6 files)

Specialized AI assistants with custom capabilities.

| File | Description | Tools | Use Case |
|------|-------------|-------|----------|
| `code-reviewer.md` | Code quality analysis | read, grep, diff, lint_runner | Comprehensive reviews |
| `test-engineer.md` | Test coverage analysis | read, write, bash, grep | Test automation |
| `documentation-writer.md` | Documentation creation | read, write, grep | Doc generation |
| `secure-reviewer.md` | Security review (read-only) | read, grep | Security audits |
| `implementation-agent.md` | Full implementation | read, write, bash, grep, edit, glob | Feature development |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation Path**: `.claude/agents/`

**Usage**: Automatically delegated by main agent

---

## 💾 03. Memory (4 files)

Persistent context and project standards.

| File | Description | Scope | Location |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | Team project standards | Project-wide | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API-specific rules | Directory | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | Personal preferences | User | `~/.claude/CLAUDE.md` |
| `README.md` | Documentation | - | Reference |

**Installation**: Copy to appropriate location

**Usage**: Automatically loaded by Claude

---

## 🔌 04. MCP Protocol (5 files)

External tool and API integrations.

| File | Description | Integrates With | Use Case |
|------|-------------|-----------------|----------|
| `github-mcp.json` | GitHub integration | GitHub API | PR/issue management |
| `database-mcp.json` | Database queries | PostgreSQL/MySQL | Live data queries |
| `filesystem-mcp.json` | File operations | Local filesystem | File management |
| `multi-mcp.json` | Multiple servers | GitHub + DB + Slack | Complete integration |
| `README.md` | Documentation | - | Setup and usage guide |

**Installation Path**: `.claude/mcp.json`

**Usage**: `/mcp__github__list_prs`, etc.

---

## 🎯 05. Skills (11 files)

Auto-invoked capabilities with scripts and templates.

### Code Review Skill (5 files)
```
code-review/
├── SKILL.md                          # Skill definition
├── scripts/
│   ├── analyze-metrics.py            # Code metrics analyzer
│   └── compare-complexity.py         # Complexity comparison
└── templates/
    ├── review-checklist.md           # Review checklist
    └── finding-template.md           # Finding documentation
```

**Purpose**: Comprehensive code review with security, performance, and quality analysis

**Auto-invoked**: When reviewing code

---

### Brand Voice Skill (4 files)
```
brand-voice/
├── SKILL.md                          # Skill definition
├── templates/
│   ├── email-template.txt            # Email format
│   └── social-post-template.txt      # Social media format
└── tone-examples.md                  # Example messages
```

**Purpose**: Ensure consistent brand voice in communications

**Auto-invoked**: When creating marketing copy

---

### Documentation Generator Skill (2 files)
```
doc-generator/
├── SKILL.md                          # Skill definition
└── generate-docs.py                  # Python doc extractor
```

**Purpose**: Generate comprehensive API documentation from source code

**Auto-invoked**: When creating/updating API documentation

**Plus**: `README.md` - Skills overview and usage guide

**Installation Path**: `~/.claude/skills/` or `.claude/skills/`

---

## 📦 06. Plugins (3 complete plugins, 40 files)

Bundled collections of features.

### PR Review Plugin (10 files)
```
pr-review/
├── plugin.yaml                       # Plugin manifest
├── commands/
│   ├── review-pr.md                  # Comprehensive review
│   ├── check-security.md             # Security check
│   └── check-tests.md                # Test coverage check
├── agents/
│   ├── security-reviewer.md          # Security specialist
│   ├── test-checker.md               # Test specialist
│   └── performance-analyzer.md       # Performance specialist
├── mcp/
│   └── github-config.json            # GitHub integration
├── hooks/
│   └── pre-review.js                 # Pre-review validation
└── README.md                         # Plugin documentation
```

**Features**: Security analysis, test coverage, performance impact

**Commands**: `/review-pr`, `/check-security`, `/check-tests`

**Installation**: `/plugin install pr-review`

---

### DevOps Automation Plugin (15 files)
```
devops-automation/
├── plugin.yaml                       # Plugin manifest
├── commands/
│   ├── deploy.md                     # Deployment
│   ├── rollback.md                   # Rollback
│   ├── status.md                     # System status
│   └── incident.md                   # Incident response
├── agents/
│   ├── deployment-specialist.md      # Deployment expert
│   ├── incident-commander.md         # Incident coordinator
│   └── alert-analyzer.md             # Alert analyzer
├── mcp/
│   └── kubernetes-config.json        # Kubernetes integration
├── hooks/
│   ├── pre-deploy.js                 # Pre-deployment checks
│   └── post-deploy.js                # Post-deployment tasks
├── scripts/
│   ├── deploy.sh                     # Deployment automation
│   ├── rollback.sh                   # Rollback automation
│   └── health-check.sh               # Health checks
└── README.md                         # Plugin documentation
```

**Features**: Kubernetes deployment, rollback, monitoring, incident response

**Commands**: `/deploy`, `/rollback`, `/status`, `/incident`

**Installation**: `/plugin install devops-automation`

---

### Documentation Plugin (14 files)
```
documentation/
├── plugin.yaml                       # Plugin manifest
├── commands/
│   ├── generate-api-docs.md          # API docs generation
│   ├── generate-readme.md            # README creation
│   ├── sync-docs.md                  # Doc synchronization
│   └── validate-docs.md              # Doc validation
├── agents/
│   ├── api-documenter.md             # API doc specialist
│   ├── code-commentator.md           # Code comment specialist
│   └── example-generator.md          # Example creator
├── mcp/
│   └── github-docs-config.json       # GitHub integration
├── templates/
│   ├── api-endpoint.md               # API endpoint template
│   ├── function-docs.md              # Function doc template
│   └── adr-template.md               # ADR template
└── README.md                         # Plugin documentation
```

**Features**: API docs, README generation, doc sync, validation

**Commands**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**Installation**: `/plugin install documentation`

**Plus**: `README.md` - Plugins overview and usage guide

---

## 📚 Documentation Files (7 files)

| File | Location | Description |
|------|----------|-------------|
| `README.md` | `/` | Main examples overview |
| `INDEX.md` | `/` | This complete index |
| `README.md` | `/01-slash-commands/` | Slash commands guide |
| `README.md` | `/02-subagents/` | Subagents guide |
| `README.md` | `/03-memory/` | Memory guide |
| `README.md` | `/04-mcp/` | MCP guide |
| `README.md` | `/05-skills/` | Skills guide |
| `README.md` | `/06-plugins/` | Plugins guide |

---

## 🗂️ Complete File Tree

```
claude-howto/
├── README.md                                    # Main overview
├── INDEX.md                                     # This file
├── QUICK_REFERENCE.md                           # Quick reference card
├── claude_concepts_guide.md                     # Original guide
│
├── 01-slash-commands/                           # Slash Commands
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
│
├── 02-subagents/                                # Subagents
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
│
├── 03-memory/                                   # Memory
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
│
├── 04-mcp/                                      # MCP Protocol
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 05-skills/                                   # Skills
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
│
└── 06-plugins/                                  # Plugins
    ├── pr-review/
    │   ├── plugin.yaml
    │   ├── commands/
    │   │   ├── review-pr.md
    │   │   ├── check-security.md
    │   │   └── check-tests.md
    │   ├── agents/
    │   │   ├── security-reviewer.md
    │   │   ├── test-checker.md
    │   │   └── performance-analyzer.md
    │   ├── mcp/
    │   │   └── github-config.json
    │   ├── hooks/
    │   │   └── pre-review.js
    │   └── README.md
    ├── devops-automation/
    │   ├── plugin.yaml
    │   ├── commands/
    │   │   ├── deploy.md
    │   │   ├── rollback.md
    │   │   ├── status.md
    │   │   └── incident.md
    │   ├── agents/
    │   │   ├── deployment-specialist.md
    │   │   ├── incident-commander.md
    │   │   └── alert-analyzer.md
    │   ├── mcp/
    │   │   └── kubernetes-config.json
    │   ├── hooks/
    │   │   ├── pre-deploy.js
    │   │   └── post-deploy.js
    │   ├── scripts/
    │   │   ├── deploy.sh
    │   │   ├── rollback.sh
    │   │   └── health-check.sh
    │   └── README.md
    ├── documentation/
    │   ├── plugin.yaml
    │   ├── commands/
    │   │   ├── generate-api-docs.md
    │   │   ├── generate-readme.md
    │   │   ├── sync-docs.md
    │   │   └── validate-docs.md
    │   ├── agents/
    │   │   ├── api-documenter.md
    │   │   ├── code-commentator.md
    │   │   └── example-generator.md
    │   ├── mcp/
    │   │   └── github-docs-config.json
    │   ├── templates/
    │   │   ├── api-endpoint.md
    │   │   ├── function-docs.md
    │   │   └── adr-template.md
    │   └── README.md
    └── README.md
```

---

## 🚀 Quick Start by Use Case

### Code Quality & Reviews
```bash
# Install slash command
cp 01-slash-commands/optimize.md .claude/commands/

# Install subagent
cp 02-subagents/code-reviewer.md .claude/agents/

# Install skill
cp -r 05-skills/code-review ~/.claude/skills/

# Or install complete plugin
/plugin install pr-review
```

### DevOps & Deployment
```bash
# Install plugin (includes everything)
/plugin install devops-automation
```

### Documentation
```bash
# Install slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Install subagent
cp 02-subagents/documentation-writer.md .claude/agents/

# Install skill
cp -r 05-skills/doc-generator ~/.claude/skills/

# Or install complete plugin
/plugin install documentation
```

### Team Standards
```bash
# Set up project memory
cp 03-memory/project-CLAUDE.md ./CLAUDE.md

# Edit to match your team's standards
```

### External Integrations
```bash
# Set environment variables
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Install MCP config
cp 04-mcp/multi-mcp.json .claude/mcp.json
```

---

## 📊 Feature Coverage Matrix

| Category | Commands | Agents | MCP | Hooks | Scripts | Templates | Total |
|----------|----------|--------|-----|-------|---------|-----------|-------|
| **Slash Commands** | 3 | - | - | - | - | - | **3** |
| **Subagents** | - | 5 | - | - | - | - | **5** |
| **Memory** | - | - | - | - | - | 3 | **3** |
| **MCP** | - | - | 4 | - | - | - | **4** |
| **Skills** | - | - | - | - | 3 | 7 | **10** |
| **Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | **32** |
| **Docs** | - | - | - | - | - | 8 | **8** |
| **TOTAL** | **14** | **14** | **7** | **3** | **6** | **21** | **65** |

---

## 🎯 Learning Path

### Beginner (Week 1)
1. ✅ Read `README.md`
2. ✅ Install 1-2 slash commands
3. ✅ Create project memory file
4. ✅ Try basic commands

### Intermediate (Week 2-3)
1. ✅ Set up GitHub MCP
2. ✅ Install a subagent
3. ✅ Try delegating tasks
4. ✅ Install a skill

### Advanced (Week 4+)
1. ✅ Install complete plugin
2. ✅ Create custom slash commands
3. ✅ Create custom subagent
4. ✅ Create custom skill
5. ✅ Build your own plugin

---

## 🔍 Search by Keyword

### Performance
- `01-slash-commands/optimize.md` - Performance analysis
- `02-subagents/code-reviewer.md` - Performance review
- `05-skills/code-review/` - Performance metrics
- `06-plugins/pr-review/agents/performance-analyzer.md` - Performance specialist

### Security
- `02-subagents/secure-reviewer.md` - Security review
- `05-skills/code-review/` - Security analysis
- `06-plugins/pr-review/` - Security checks

### Testing
- `02-subagents/test-engineer.md` - Test engineer
- `06-plugins/pr-review/commands/check-tests.md` - Test coverage

### Documentation
- `01-slash-commands/generate-api-docs.md` - API docs command
- `02-subagents/documentation-writer.md` - Doc writer agent
- `05-skills/doc-generator/` - Doc generator skill
- `06-plugins/documentation/` - Complete doc plugin

### Deployment
- `06-plugins/devops-automation/` - Complete DevOps solution

---

## 📝 Notes

- All examples are ready to use
- Modify to fit your specific needs
- Examples follow Claude Code best practices
- Each category has its own README with detailed instructions
- Scripts include proper error handling
- Templates are customizable

---

## 🤝 Contributing

Want to add more examples? Follow the structure:
1. Create appropriate subdirectory
2. Include README.md with usage
3. Follow naming conventions
4. Test thoroughly
5. Update this index

---

**Last Updated**: November 2025
**Total Examples**: 71 files
**Categories**: 6 features
**Ready to Use**: ✅ All examples

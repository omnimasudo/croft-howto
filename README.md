<img src="claude-ai-icon.webp" alt="Claude Logo" width="13%"/>

# Claude How To

Complete collection of examples for some important Claude Code features and concepts.

## Quick Navigation

| Feature | Description | Folder |
|---------|-------------|--------|
| **Slash Commands** | User-invoked shortcuts | [01-slash-commands/](01-slash-commands/) |
| **Subagents** | Specialized AI assistants | [02-subagents/](02-subagents/) |
| **Memory** | Persistent context | [03-memory/](03-memory/) |
| **MCP Protocol** | External tool access | [04-mcp/](04-mcp/) |
| **Skills** | Reusable capabilities | [05-skills/](05-skills/) |
| **Plugins** | Bundled features | [06-plugins/](06-plugins/) |

---

## 01. Slash Commands

**Location**: [01-slash-commands/](01-slash-commands/)

**What**: User-invoked shortcuts stored as Markdown files

**Examples**:
- `optimize.md` - Code optimization analysis
- `pr.md` - Pull request preparation
- `generate-api-docs.md` - API documentation generator

**Installation**:
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**Usage**:
```
/optimize
/pr
/generate-api-docs
```

---

## 02. Subagents

**Location**: [02-subagents/](02-subagents/)

**What**: Specialized AI assistants with isolated contexts and custom prompts

**Examples**:
- `code-reviewer.md` - Comprehensive code quality analysis
- `test-engineer.md` - Test strategy and coverage
- `documentation-writer.md` - Technical documentation
- `secure-reviewer.md` - Security-focused review (read-only)
- `implementation-agent.md` - Full feature implementation

**Installation**:
```bash
cp 02-subagents/*.md /path/to/project/.claude/agents/
```

**Usage**: Automatically delegated by main agent

---

## 03. Memory

**Location**: [03-memory/](03-memory/)

**What**: Persistent context across sessions

**Examples**:
- `project-CLAUDE.md` - Team-wide project standards
- `directory-api-CLAUDE.md` - Directory-specific rules
- `personal-CLAUDE.md` - Personal preferences

**Installation**:
```bash
# Project memory
cp 03-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# Directory memory
cp 03-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# Personal memory
cp 03-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**Usage**: Automatically loaded by Claude

---

## 04. MCP Protocol

**Location**: [04-mcp/](04-mcp/)

**What**: Model Context Protocol for accessing external tools and APIs

**Examples**:
- `github-mcp.json` - GitHub integration
- `database-mcp.json` - Database queries
- `filesystem-mcp.json` - File operations
- `multi-mcp.json` - Multiple MCP servers

**Installation**:
```bash
# Set environment variables
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Copy configuration
cp 04-mcp/github-mcp.json ~/.claude/mcp.json
```

**Usage**:
```
/mcp__github__list_prs
/mcp__github__get_pr 456
```

---

## 05. Skills

**Location**: [05-skills/](05-skills/)

**What**: Reusable, auto-invoked capabilities with instructions and scripts

**Examples**:
- `code-review/` - Comprehensive code review with scripts
- `brand-voice/` - Brand voice consistency checker
- `doc-generator/` - API documentation generator

**Installation**:
```bash
# Personal skills
cp -r 05-skills/code-review ~/.claude/skills/

# Project skills
cp -r 05-skills/code-review /path/to/project/.claude/skills/
```

**Usage**: Automatically invoked when relevant

---

## 06. Plugins

**Location**: [06-plugins/](06-plugins/)

**What**: Bundled collections of commands, agents, MCP, and hooks

**Examples**:
- `pr-review/` - Complete PR review workflow
- `devops-automation/` - Deployment and monitoring
- `documentation/` - Documentation generation

**Installation**:
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**Usage**: Use bundled slash commands and features

---

## Feature Comparison

| Feature | Invocation | Persistence | Best For |
|---------|-----------|------------|----------|
| **Slash Commands** | Manual (`/cmd`) | Session only | Quick shortcuts |
| **Subagents** | Auto-delegated | Isolated context | Task distribution |
| **Memory** | Auto-loaded | Cross-session | Long-term learning |
| **MCP Protocol** | Auto-queried | Real-time | Live data access |
| **Skills** | Auto-invoked | Filesystem | Automated workflows |
| **Plugins** | One command | All features | Complete solutions |

---

## Getting Started

### Week 1: Basics
1. Copy slash commands to `.claude/commands/`
2. Try `/optimize` and `/pr` commands
3. Create project memory in `CLAUDE.md`

### Week 2: Real-time Access
1. Set up GitHub MCP
2. Query PRs and issues
3. Try multi-MCP configuration

### Week 3: Distribution
1. Create first subagent
2. Test with complex task
3. Delegate work to specialists

### Week 4: Automation
1. Install a skill
2. Let Claude auto-invoke it
3. Create custom skill

### Week 5: Complete Solution
1. Install a plugin
2. Use bundled features
3. Consider creating your own

---

## Directory Structure

```

├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 03-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 04-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 05-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 06-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
└── README.md (this file)
```

---

## Example Workflows

### 1. Complete Code Review Workflow

```markdown
# Uses: Slash Commands + Subagents + Memory + MCP

User: /review-pr

Claude:
1. Loads project memory (coding standards)
2. Fetches PR via GitHub MCP
3. Delegates to code-reviewer subagent
4. Delegates to test-engineer subagent
5. Synthesizes findings
6. Provides comprehensive review
```

### 2. Automated Documentation

```markdown
# Uses: Skills + Subagents + Memory

User: "Generate API documentation for the auth module"

Claude:
1. Loads project memory (doc standards)
2. Detects doc generation request
3. Auto-invokes doc-generator skill
4. Delegates to api-documenter subagent
5. Creates comprehensive docs with examples
```

### 3. DevOps Deployment

```markdown
# Uses: Plugins + MCP + Hooks

User: /deploy production

Claude:
1. Runs pre-deploy hook (validates environment)
2. Delegates to deployment-specialist subagent
3. Executes deployment via Kubernetes MCP
4. Monitors progress
5. Runs post-deploy hook (health checks)
6. Reports status
```

---

## Installation Quick Reference

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Subagents
cp 02-subagents/*.md .claude/agents/

# Memory
cp 03-memory/project-CLAUDE.md ./CLAUDE.md

# MCP
export GITHUB_TOKEN="token"
cp 04-mcp/github-mcp.json .claude/mcp.json

# Skills
cp -r 05-skills/code-review ~/.claude/skills/

# Plugins
/plugin install pr-review
```

---

## Use Case Matrix

| Use Case | Recommended Features |
|----------|---------------------|
| **Team Onboarding** | Memory + Slash Commands + Plugins |
| **Code Quality** | Subagents + Skills + Memory |
| **Documentation** | Skills + Subagents + Plugins |
| **DevOps** | Plugins + MCP + Hooks |
| **Security Review** | Subagents + Skills |
| **API Integration** | MCP + Memory |
| **Quick Tasks** | Slash Commands |
| **Complex Projects** | All Features |

---

## Best Practices

### Do's ✅
- Start simple with slash commands
- Add features incrementally
- Use memory for team standards
- Test configurations locally first
- Document custom implementations
- Version control project configurations
- Share plugins with team

### Don'ts ❌
- Don't create redundant features
- Don't hardcode credentials
- Don't skip documentation
- Don't over-complicate simple tasks
- Don't ignore security best practices
- Don't commit sensitive data

---

## Troubleshooting

### Feature Not Loading
1. Check file location and naming
2. Verify YAML frontmatter syntax
3. Check file permissions
4. Review Claude Code version compatibility

### MCP Connection Failed
1. Verify environment variables
2. Check MCP server installation
3. Test credentials
4. Review network connectivity

### Subagent Not Delegating
1. Check tool permissions
2. Verify agent description clarity
3. Review task complexity
6. Test agent independently

---

## Additional Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Plugin Marketplace](https://plugins.claude.com)
- [Community Examples](https://github.com/anthropic/claude-examples)

---

## Contributing

Found an issue or want to contribute an example?

1. Create an issue describing the example
2. Follow existing structure and patterns
3. Include comprehensive README
4. Test thoroughly
5. Submit pull request

---

## License

These examples are provided as-is for educational purposes. Adapt and use them freely in your projects.

---

**Last Updated**: November 2025
**Claude Code Version**: 1.0+
**Compatible Models**: Sonnet 4.5, Opus 4.1, Haiku 4.5

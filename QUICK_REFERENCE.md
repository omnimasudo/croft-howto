# Claude Code Examples - Quick Reference Card

## 🚀 Installation Quick Commands

### Slash Commands
```bash
# Install all
cp 01-slash-commands/*.md .claude/commands/

# Install specific
cp 01-slash-commands/optimize.md .claude/commands/
```

### Subagents
```bash
# Install all
cp 02-subagents/*.md .claude/agents/

# Install specific
cp 02-subagents/code-reviewer.md .claude/agents/
```

### Memory
```bash
# Project memory
cp 03-memory/project-CLAUDE.md ./CLAUDE.md

# Personal memory
cp 03-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### MCP
```bash
# Set credentials
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Install config
cp 04-mcp/github-mcp.json ~/.claude/mcp.json
```

### Skills
```bash
# Personal skills
cp -r 05-skills/code-review ~/.claude/skills/

# Project skills
cp -r 05-skills/code-review .claude/skills/
```

### Plugins
```bash
# Install from examples (if published)
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

---

## 📋 Feature Cheat Sheet

| Feature | Install Path | Usage |
|---------|-------------|-------|
| **Slash Commands** | `.claude/commands/*.md` | `/command-name` |
| **Subagents** | `.claude/agents/*.md` | Auto-delegated |
| **Memory** | `./CLAUDE.md` | Auto-loaded |
| **MCP** | `.claude/mcp.json` | `/mcp__server__action` |
| **Skills** | `.claude/skills/*/SKILL.md` | Auto-invoked |
| **Plugins** | Via `/plugin install` | Bundles all |

---

## 🎯 Common Use Cases

### Code Review
```bash
# Method 1: Slash command
cp 01-slash-commands/optimize.md .claude/commands/
# Use: /optimize

# Method 2: Subagent
cp 02-subagents/code-reviewer.md .claude/agents/
# Use: Auto-delegated

# Method 3: Skill
cp -r 05-skills/code-review ~/.claude/skills/
# Use: Auto-invoked

# Method 4: Plugin (best)
/plugin install pr-review
# Use: /review-pr
```

### Documentation
```bash
# Slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Subagent
cp 02-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 05-skills/doc-generator ~/.claude/skills/

# Plugin (complete solution)
/plugin install documentation
```

### DevOps
```bash
# Complete plugin
/plugin install devops-automation

# Commands: /deploy, /rollback, /status, /incident
```

### Team Standards
```bash
# Project memory
cp 03-memory/project-CLAUDE.md ./CLAUDE.md

# Edit for your team
vim CLAUDE.md
```

---

## 📁 File Locations Reference

```
Your Project/
├── .claude/
│   ├── commands/        # Slash commands go here
│   ├── agents/          # Subagents go here
│   ├── skills/          # Project skills go here
│   └── mcp.json         # MCP configuration
├── CLAUDE.md            # Project memory
└── src/
    └── api/
        └── CLAUDE.md    # Directory-specific memory

User Home/
└── .claude/
    ├── commands/        # Personal commands
    ├── skills/          # Personal skills
    ├── mcp.json         # Personal MCP config
    └── CLAUDE.md        # Personal memory
```

---

## 🔍 Finding Examples

### By Category
- **Slash Commands**: `01-slash-commands/`
- **Subagents**: `02-subagents/`
- **Memory**: `03-memory/`
- **MCP**: `04-mcp/`
- **Skills**: `05-skills/`
- **Plugins**: `06-plugins/`

### By Use Case
- **Performance**: `01-slash-commands/optimize.md`
- **Security**: `02-subagents/secure-reviewer.md`
- **Testing**: `02-subagents/test-engineer.md`
- **Docs**: `05-skills/doc-generator/`
- **DevOps**: `06-plugins/devops-automation/`

### By Complexity
- **Simple**: Slash commands
- **Medium**: Subagents, Memory
- **Advanced**: Skills
- **Complete**: Plugins

---

## 🎓 Learning Path

### Day 1
```bash
# Read overview
cat README.md

# Install a command
cp 01-slash-commands/optimize.md .claude/commands/

# Try it
/optimize
```

### Day 2-3
```bash
# Set up memory
cp 03-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# Install subagent
cp 02-subagents/code-reviewer.md .claude/agents/
```

### Day 4-5
```bash
# Set up MCP
export GITHUB_TOKEN="your_token"
cp 04-mcp/github-mcp.json .claude/mcp.json

# Try MCP commands
/mcp__github__list_prs
```

### Week 2
```bash
# Install skill
cp -r 05-skills/code-review ~/.claude/skills/

# Let it auto-invoke
# Just say: "Review this code for issues"
```

### Week 3+
```bash
# Install complete plugin
/plugin install pr-review

# Use bundled features
/review-pr
/check-security
/check-tests
```

---

## 💡 Tips & Tricks

### Customization
- Start with examples as-is
- Modify to fit your needs
- Test before sharing with team
- Version control your configurations

### Best Practices
- Use memory for team standards
- Use plugins for complete workflows
- Use subagents for complex tasks
- Use slash commands for quick tasks

### Troubleshooting
```bash
# Check file locations
ls -la .claude/commands/
ls -la .claude/agents/

# Verify YAML syntax
head -20 .claude/agents/code-reviewer.md

# Test MCP connection
echo $GITHUB_TOKEN
```

---

## 📊 Feature Matrix

| Need | Use This | Example |
|------|----------|---------|
| Quick shortcut | Slash Command | `01-slash-commands/optimize.md` |
| Specialized task | Subagent | `02-subagents/code-reviewer.md` |
| Team standards | Memory | `03-memory/project-CLAUDE.md` |
| External data | MCP | `04-mcp/github-mcp.json` |
| Auto workflow | Skill | `05-skills/code-review/` |
| Complete solution | Plugin | `06-plugins/pr-review/` |

---

## 🔗 Quick Links

- **Main Guide**: `README.md`
- **Complete Index**: `INDEX.md`
- **Summary**: `EXAMPLES_SUMMARY.md`
- **Original Guide**: `claude_concepts_guide.md`

---

## 📞 Common Questions

**Q: Which should I use?**
A: Start with slash commands, add features as needed.

**Q: Can I mix features?**
A: Yes! They work together. Memory + Commands + MCP = powerful.

**Q: How do I share with team?**
A: Commit `.claude/` directory to git.

**Q: What about secrets?**
A: Use environment variables, never hardcode.

**Q: Can I modify examples?**
A: Absolutely! They're templates to customize.

---

## ✅ Checklist

Getting started checklist:

- [ ] Read `README.md`
- [ ] Install 1 slash command
- [ ] Try the command
- [ ] Create project `CLAUDE.md`
- [ ] Install 1 subagent
- [ ] Set up 1 MCP integration
- [ ] Install 1 skill
- [ ] Try a complete plugin
- [ ] Customize for your needs
- [ ] Share with team

---

**Quick Start**: `cat README.md`

**Full Index**: `cat INDEX.md`

**This Card**: Keep it handy for quick reference!

# Claude Code Plugins Examples

This folder contains complete plugin examples that bundle multiple Claude Code features into cohesive, installable packages.

## What Are Plugins?

Plugins are bundled collections of:
- Slash commands
- Subagents
- MCP servers
- Hooks
- Scripts and templates

All installable with a single command.

## Available Plugins

### 1. PR Review Plugin
**Location**: [pr-review/](pr-review/)

**Purpose**: Complete PR review workflow with security, testing, and documentation checks

**Features**:
- 3 slash commands (`/review-pr`, `/check-security`, `/check-tests`)
- 3 specialized subagents
- GitHub MCP integration
- Pre-review validation hook

**Installation**:
```bash
/plugin install pr-review
```

**Use Case**: Automated code reviews for pull requests

---

### 2. DevOps Automation Plugin
**Location**: [devops-automation/](devops-automation/)

**Purpose**: Complete DevOps automation for deployment, monitoring, and incident response

**Features**:
- 4 slash commands (`/deploy`, `/rollback`, `/status`, `/incident`)
- 3 specialized subagents
- Kubernetes MCP integration
- Pre/post-deployment hooks
- Deployment scripts

**Installation**:
```bash
/plugin install devops-automation
```

**Use Case**: Kubernetes deployment automation and incident management

---

### 3. Documentation Plugin
**Location**: [documentation/](documentation/)

**Purpose**: Comprehensive documentation generation and maintenance

**Features**:
- 4 slash commands
- 3 documentation subagents
- GitHub MCP integration
- Documentation templates (API, function, ADR)

**Installation**:
```bash
/plugin install documentation
```

**Use Case**: Automated documentation generation and maintenance

---

## Plugin Structure

```
plugin-name/
├── plugin.yaml           # Plugin manifest
├── commands/             # Slash commands
│   ├── command-1.md
│   └── command-2.md
├── agents/               # Subagents
│   ├── agent-1.md
│   └── agent-2.md
├── mcp/                  # MCP configurations
│   └── config.json
├── hooks/                # Event hooks
│   ├── pre-hook.js
│   └── post-hook.js
├── scripts/              # Helper scripts
│   └── script.sh
├── templates/            # Document templates
│   └── template.md
└── README.md             # Plugin documentation
```

## Plugin Manifest (plugin.yaml)

```yaml
---
name: plugin-name
version: "1.0.0"
description: What this plugin does
author: Your Name
license: MIT
tags:
  - category
  - use-case

requires:
  - claude-code: ">=1.0.0"

components:
  - type: commands
    path: commands/
  - type: agents
    path: agents/
  - type: mcp
    path: mcp/
  - type: hooks
    path: hooks/

config:
  auto_load: true
  enabled_by_default: true
---
```

## Installation Methods

### Official Plugin
```bash
/plugin install plugin-name
```

### Local Plugin (for development)
```bash
/plugin install ./path/to/plugin
```

### From Git Repository
```bash
/plugin install github:username/repo
```

## When to Create a Plugin

Create a plugin when:

✅ You have multiple related commands/agents
✅ You want one-command installation
✅ You're sharing with a team
✅ You need version control
✅ You want marketplace distribution
✅ Complex setup requires automation

Don't create a plugin when:

❌ Single slash command is sufficient
❌ One-time use case
❌ Personal preference (use individual features)
❌ Very simple functionality

## Plugin vs Individual Features

| Aspect | Plugin | Individual Features |
|--------|--------|-------------------|
| **Installation** | One command | Manual copy per feature |
| **Setup Time** | 2 minutes | 15-30 minutes |
| **Components** | Multiple bundled | One at a time |
| **Versioning** | Automatic | Manual |
| **Team Sharing** | Plugin ID | Copy files |
| **Updates** | Auto-available | Manual |
| **Marketplace** | Yes | No |

## Creating Your Own Plugin

### Step 1: Create Structure
```bash
mkdir my-plugin
cd my-plugin
mkdir commands agents mcp hooks scripts templates
```

### Step 2: Create plugin.yaml
```yaml
---
name: my-plugin
version: "1.0.0"
description: My custom plugin
author: Your Name
---
```

### Step 3: Add Components
- Add slash commands to `commands/`
- Add subagents to `agents/`
- Add MCP configs to `mcp/`
- Add hooks to `hooks/`
- Add helper scripts to `scripts/`

### Step 4: Test Locally
```bash
/plugin install ./my-plugin
```

### Step 5: Publish
Submit to plugin marketplace or share via git repository.

## Best Practices

### Do's ✅
- Use clear, descriptive plugin names
- Include comprehensive README
- Version your plugin properly
- Test all components together
- Document requirements clearly
- Provide usage examples
- Include error handling
- Tag appropriately for discovery

### Don'ts ❌
- Don't bundle unrelated features
- Don't hardcode credentials
- Don't skip testing
- Don't forget documentation
- Don't create redundant plugins
- Don't ignore versioning

## Plugin Lifecycle

```
Discover → Install → Configure → Use → Update → Disable/Remove
```

### Discovery
Browse plugin marketplace or search by tags

### Installation
```bash
/plugin install plugin-name
```

### Configuration
Set up required environment variables and credentials

### Usage
Use slash commands, subagents work automatically

### Updates
```bash
/plugin update plugin-name
```

### Disable
```bash
/plugin disable plugin-name
```

### Remove
```bash
/plugin uninstall plugin-name
```

## Example: Complete Workflow

### PR Review Plugin Workflow

```
1. User: /review-pr

2. Plugin executes:
   ├── pre-review.js hook validates git repo
   ├── GitHub MCP fetches PR data
   ├── security-reviewer subagent analyzes security
   ├── test-checker subagent verifies coverage
   └── performance-analyzer subagent checks performance

3. Results synthesized and presented:
   ✅ Security: No critical issues
   ⚠️  Testing: Coverage 65% (recommend 80%+)
   ✅ Performance: No significant impact
   📝 12 recommendations provided
```

## Troubleshooting

### Plugin Won't Install
- Check Claude Code version compatibility
- Verify plugin.yaml syntax
- Check internet connection (for remote plugins)

### Components Not Loading
- Verify paths in plugin.yaml
- Check file permissions
- Review component file syntax

### MCP Connection Failed
- Verify environment variables are set
- Check MCP server installation
- Test MCP connection independently

## Additional Resources

- [Plugin Development Guide](https://docs.claude.com/plugins)
- [Plugin Marketplace](https://plugins.claude.com)
- [Example Plugins Repository](https://github.com/anthropic/claude-plugins)
- [Plugin API Reference](https://docs.claude.com/api/plugins)

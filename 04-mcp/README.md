# MCP (Model Context Protocol) Examples

This folder contains example MCP server configurations for Claude Code.

## What is MCP?

MCP (Model Context Protocol) enables Claude to access external tools, APIs, and real-time data sources. Unlike Memory, MCP provides live access to changing data.

## Installation

Copy the appropriate configuration to your project's `.claude/` directory:

```bash
cp github-mcp.json /path/to/your/project/.claude/mcp.json
```

## Available MCP Configurations

### 1. GitHub MCP (`github-mcp.json`)
Access GitHub repositories, PRs, issues, and commits.

**Setup**:
```bash
export GITHUB_TOKEN="your_github_token"
cp github-mcp.json ~/.claude/mcp.json
```

**Available Tools**:
- `list_prs` - List all PRs in repository
- `get_pr` - Get PR details including diff
- `create_pr` - Create new PR
- `list_issues` - List all issues
- `create_issue` - Create new issue
- `get_commit` - Get commit details
- `search_code` - Search across codebase

**Usage**:
```
/mcp__github__list_prs completed:true last:7days
/mcp__github__get_pr 456
/mcp__github__create_issue "Bug in login form"
```

### 2. Database MCP (`database-mcp.json`)
Query PostgreSQL/MySQL databases.

**Setup**:
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
cp database-mcp.json ~/.claude/mcp.json
```

**Usage**:
```
User: Fetch all users with more than 10 orders

Claude: I'll query your database:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
```

### 3. Filesystem MCP (`filesystem-mcp.json`)
File operations on local filesystem.

**Setup**:
```bash
cp filesystem-mcp.json ~/.claude/mcp.json
```

**Available Operations**:
- List files
- Read file contents
- Write files
- Search in files
- Delete files

### 4. Multi-MCP (`multi-mcp.json`)
Configure multiple MCP servers simultaneously.

**Setup**:
```bash
export GITHUB_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="your_slack_token"
cp multi-mcp.json ~/.claude/mcp.json
```

## Available MCP Servers

| MCP Server | Purpose | Auth | Real-time |
|------------|---------|------|-----------|
| **Filesystem** | File operations | OS permissions | ✅ Yes |
| **GitHub** | Repository management | OAuth | ✅ Yes |
| **Slack** | Team communication | Token | ✅ Yes |
| **Database** | SQL queries | Credentials | ✅ Yes |
| **Google Docs** | Document access | OAuth | ✅ Yes |
| **Asana** | Project management | API Key | ✅ Yes |
| **Stripe** | Payment data | API Key | ✅ Yes |

## Configuration Format

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-name"],
      "env": {
        "ENV_VAR": "${ENV_VAR}"
      }
    }
  }
}
```

## Multi-MCP Workflow Example

### Daily Report Generation

```markdown
# Uses: GitHub MCP + Database MCP + Slack MCP + Filesystem MCP

## Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days
→ Output: 42 PRs merged

## Step 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders WHERE created_at > NOW() - INTERVAL '1 day'
→ Output: 247 sales, $12,450 revenue

## Step 3: Generate Report
Combine data into HTML report

## Step 4: Save to Filesystem
Write report.html to /reports/

## Step 5: Post to Slack
Send summary to #daily-reports channel

✅ Report generated and posted
```

## MCP vs Memory

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]
```

## Environment Variables

Store sensitive credentials in environment variables:

```bash
# ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

Then reference them in MCP config:

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Security Best Practices

### Do's ✅
- Use environment variables for credentials
- Rotate tokens regularly
- Use read-only tokens when possible
- Limit MCP server access scope
- Monitor MCP server usage

### Don'ts ❌
- Don't hardcode credentials in config files
- Don't commit tokens to git
- Don't share tokens in team chats
- Don't use personal tokens for team projects
- Don't grant unnecessary permissions

## Troubleshooting

### MCP Server Not Found
```bash
# Install MCP server globally
npm install -g @modelcontextprotocol/server-github
```

### Authentication Failed
```bash
# Verify environment variable is set
echo $GITHUB_TOKEN

# Re-export if needed
export GITHUB_TOKEN="your_token"
```

### Connection Timeout
- Check network connectivity
- Verify API endpoint is accessible
- Check rate limits on API
- Try increasing timeout in config

## Additional Resources

- [MCP GitHub Repository](https://github.com/modelcontextprotocol/servers)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Claude Code MCP Guide](https://docs.claude.com/en/docs/claude-code/mcp)

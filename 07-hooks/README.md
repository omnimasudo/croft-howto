# Hooks

Hooks are shell commands that execute automatically in response to specific events in Claude Code. They enable custom workflows, validation, and automation.

## What Are Hooks?

Hooks are event-driven scripts that run at specific points during Claude Code's operation:
- **Pre-hooks**: Run before an action
- **Post-hooks**: Run after an action
- **Validation hooks**: Check conditions before proceeding

## Available Hook Types

### 1. Tool Hooks
Execute before/after tool usage:
- `PreToolUse:{ToolName}` - Before a tool is used
- `PostToolUse:{ToolName}` - After a tool completes
- Examples: `PreToolUse:Edit`, `PostToolUse:Bash`, `PreToolUse:Write`

### 2. Session Hooks
Execute during session lifecycle:
- `UserPromptSubmit` - Before processing user input
- `SessionStart` - When a new session begins
- `SessionEnd` - When a session ends

### 3. Git Hooks
Execute during git operations:
- `PreCommit` - Before creating a commit
- `PostCommit` - After commit completes
- `PrePush` - Before pushing to remote

## Configuration

Hooks are configured in Claude Code settings:

```json
{
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Bash": "echo 'Command completed' >> /tmp/bash.log",
    "UserPromptSubmit": "~/.claude/hooks/validate-prompt.sh",
    "PreCommit": "npm test"
  }
}
```

## Hook Variables

Available variables in hook commands:
- `${file_path}` - Path to file being edited/written
- `${command}` - Command being executed (Bash hooks)
- `${tool_name}` - Name of the tool being used
- `${session_id}` - Current session identifier

## Examples

### Example 1: Auto-format Code on Edit

**Hook**: `PreToolUse:Write`

```bash
#!/bin/bash
# ~/.claude/hooks/format-code.sh

FILE=$1

# Detect file type and format accordingly
case "$FILE" in
  *.js|*.jsx|*.ts|*.tsx)
    prettier --write "$FILE"
    ;;
  *.py)
    black "$FILE"
    ;;
  *.go)
    gofmt -w "$FILE"
    ;;
esac
```

**Configuration**:
```json
{
  "hooks": {
    "PreToolUse:Write": "~/.claude/hooks/format-code.sh ${file_path}"
  }
}
```

### Example 2: Run Tests Before Commit

**Hook**: `PreCommit`

```bash
#!/bin/bash
# ~/.claude/hooks/pre-commit.sh

echo "Running tests before commit..."

# Run tests
npm test

# Check exit code
if [ $? -ne 0 ]; then
  echo "❌ Tests failed! Commit blocked."
  exit 1
fi

echo "✅ Tests passed! Proceeding with commit."
exit 0
```

**Configuration**:
```json
{
  "hooks": {
    "PreCommit": "~/.claude/hooks/pre-commit.sh"
  }
}
```

### Example 3: Security Scan on File Write

**Hook**: `PostToolUse:Write`

```bash
#!/bin/bash
# ~/.claude/hooks/security-scan.sh

FILE=$1

# Check for common security issues
if grep -q "password\s*=\s*['\"]" "$FILE"; then
  echo "⚠️  WARNING: Potential hardcoded password detected in $FILE"
fi

if grep -q "api[_-]key\s*=\s*['\"]" "$FILE"; then
  echo "⚠️  WARNING: Potential hardcoded API key detected in $FILE"
fi

# Scan with semgrep if available
if command -v semgrep &> /dev/null; then
  semgrep --config=auto "$FILE" --quiet
fi
```

**Configuration**:
```json
{
  "hooks": {
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh ${file_path}"
  }
}
```

### Example 4: Log All Bash Commands

**Hook**: `PostToolUse:Bash`

```bash
#!/bin/bash
# ~/.claude/hooks/log-bash.sh

COMMAND=$1
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
LOGFILE="$HOME/.claude/bash-commands.log"

echo "[$TIMESTAMP] $COMMAND" >> "$LOGFILE"
```

**Configuration**:
```json
{
  "hooks": {
    "PostToolUse:Bash": "~/.claude/hooks/log-bash.sh '${command}'"
  }
}
```

### Example 5: Validate User Prompts

**Hook**: `UserPromptSubmit`

```bash
#!/bin/bash
# ~/.claude/hooks/validate-prompt.sh

# Read prompt from stdin
PROMPT=$(cat)

# Check for prohibited patterns
if echo "$PROMPT" | grep -qi "delete database"; then
  echo "❌ Blocked: Dangerous operation detected"
  exit 1
fi

# Check for required context
if echo "$PROMPT" | grep -qi "deploy to production"; then
  if [ ! -f ".deployment-approved" ]; then
    echo "❌ Blocked: Production deployment requires approval file"
    exit 1
  fi
fi

exit 0
```

**Configuration**:
```json
{
  "hooks": {
    "UserPromptSubmit": "~/.claude/hooks/validate-prompt.sh"
  }
}
```

## Hook Exit Codes

Hooks communicate results via exit codes:
- `0` - Success, continue operation
- `1` - Failure, block operation (for pre-hooks)
- Other codes - Treated as warnings

## Best Practices

### Do's ✅
- Keep hooks fast (< 1 second when possible)
- Use hooks for validation and automation
- Log important events
- Make hooks idempotent
- Handle errors gracefully
- Use absolute paths in hooks

### Don'ts ❌
- Don't make hooks interactive (no user input)
- Don't use hooks for long-running tasks
- Don't hardcode credentials in hooks
- Don't ignore hook failures silently
- Don't modify files unexpectedly

## Common Use Cases

### Code Quality
```json
{
  "hooks": {
    "PreToolUse:Write": "eslint --fix ${file_path}",
    "PostToolUse:Write": "prettier --check ${file_path}"
  }
}
```

### Security
```json
{
  "hooks": {
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh ${file_path}",
    "PreCommit": "git secrets --scan"
  }
}
```

### Testing
```json
{
  "hooks": {
    "PreCommit": "npm test",
    "PostToolUse:Edit": "jest --findRelatedTests ${file_path}"
  }
}
```

### Deployment
```json
{
  "hooks": {
    "PrePush": "npm run build && npm run test:e2e",
    "PostPush": "~/.claude/hooks/notify-team.sh"
  }
}
```

## Debugging Hooks

Enable hook debugging:
```json
{
  "hooks": {
    "debug": true
  }
}
```

View hook execution logs:
```bash
tail -f ~/.claude/hooks.log
```

## Installation

1. Create hooks directory:
```bash
mkdir -p ~/.claude/hooks
```

2. Copy example hooks:
```bash
cp 07-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

3. Configure in settings:
Edit `~/.claude/settings.json` to add hook configurations.

## Troubleshooting

### Hook Not Executing
1. Check hook path is correct
2. Verify file has execute permissions
3. Check hook name matches event exactly
4. Enable debug mode

### Hook Blocking Operations
1. Check hook exit code
2. Review hook output/logs
3. Test hook independently
4. Add error handling

### Performance Issues
1. Profile hook execution time
2. Optimize slow operations
3. Consider async execution
4. Cache results when possible

## Advanced Examples

See the example files in this directory:
- `format-code.sh` - Auto-format code before writing
- `pre-commit.sh` - Run tests before commits
- `security-scan.sh` - Scan for security issues
- `log-bash.sh` - Log all bash commands
- `validate-prompt.sh` - Validate user prompts
- `notify-team.sh` - Send notifications on events

# Slash Commands Examples

This folder contains example slash commands that can be used with Claude Code.

## Installation

Copy these files to your project's `.claude/commands/` directory:

```bash
cp *.md /path/to/your/project/.claude/commands/
```

## Available Commands

### 1. `/optimize` - Code Optimization
Analyzes code for performance issues, memory leaks, and optimization opportunities.

**Usage:**
```
/optimize
[Paste your code]
```

### 2. `/pr` - Pull Request Preparation
Guides you through PR preparation checklist including linting, testing, and commit message formatting.

**Usage:**
```
/pr
```

### 3. `/generate-api-docs` - API Documentation Generator
Generates comprehensive API documentation from source code.

**Usage:**
```
/generate-api-docs
```

## File Structure

Place commands in your project:
```
project/
├── .claude/
│   └── commands/
│       ├── optimize.md
│       ├── pr.md
│       └── docs/
│           └── generate-api-docs.md
```

## Best Practices

- Use clear, action-oriented names
- Document trigger words in description
- Keep commands focused on single task
- Version control project commands
- Organize in subdirectories for categories

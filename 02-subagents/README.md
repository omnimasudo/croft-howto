# Subagents Examples

This folder contains example subagent configurations for Claude Code.

## Installation

Copy these files to your project's `.claude/agents/` directory:

```bash
cp *.md /path/to/your/project/.claude/agents/
```

## Available Subagents

### 1. Code Reviewer (`code-reviewer`)
Comprehensive code quality and maintainability analysis.

**Tools**: read, grep, diff, lint_runner

**Use Case**: Automated code reviews focusing on security, performance, and quality.

### 2. Test Engineer (`test-engineer`)
Test strategy, coverage analysis, and automated testing.

**Tools**: read, write, bash, grep

**Use Case**: Creating comprehensive test suites with high coverage.

### 3. Documentation Writer (`documentation-writer`)
Technical documentation, API docs, and user guides.

**Tools**: read, write, grep

**Use Case**: Generating and maintaining project documentation.

### 4. Secure Reviewer (`secure-reviewer`)
Security-focused code review with minimal permissions.

**Tools**: read, grep (read-only)

**Use Case**: Security audits without modification capabilities.

### 5. Implementation Agent (`implementation-agent`)
Full implementation capabilities for feature development.

**Tools**: read, write, bash, grep, edit, glob

**Use Case**: End-to-end feature implementation.

## How Subagents Work

Subagents are specialized AI assistants with:
- **Isolated context windows** - Clean slate for each task
- **Customized system prompts** - Specialized expertise
- **Tool access control** - Only necessary capabilities

## Usage Example

Main agent delegates work to subagents:

```markdown
User: "Build a new authentication feature"

Main Agent:
1. Delegates implementation to implementation-agent
2. Delegates security review to secure-reviewer
3. Delegates testing to test-engineer
4. Delegates documentation to documentation-writer
5. Synthesizes all results
```

## File Structure

```
project/
├── .claude/
│   └── agents/
│       ├── code-reviewer.md
│       ├── test-engineer.md
│       ├── documentation-writer.md
│       ├── secure-reviewer.md
│       └── implementation-agent.md
```

## When to Use Subagents

| Scenario | Use Subagent | Why |
|----------|--------------|-----|
| Complex feature with many steps | ✅ Yes | Separate concerns |
| Quick code review | ❌ No | Unnecessary overhead |
| Parallel task execution | ✅ Yes | Independent contexts |
| Specialized expertise needed | ✅ Yes | Custom prompts |
| Long-running analysis | ✅ Yes | Prevent context exhaustion |
| Single simple task | ❌ No | Adds latency |

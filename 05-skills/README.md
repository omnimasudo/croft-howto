# Skills Examples

This folder contains example skills for Claude Code. Skills are reusable, model-invoked capabilities that Claude automatically detects and uses.

## Installation

Copy skill folders to your skills directory:

```bash
# For personal skills
cp -r code-review ~/.claude/skills/

# For project skills
cp -r code-review /path/to/project/.claude/skills/
```

## Available Skills

### 1. Code Review Skill
**Location**: `code-review/`

**Purpose**: Comprehensive code review with security, performance, and quality analysis

**Contents**:
- `SKILL.md` - Main skill definition
- `scripts/analyze-metrics.py` - Code metrics analyzer
- `scripts/compare-complexity.py` - Complexity comparison tool
- `templates/review-checklist.md` - Review checklist
- `templates/finding-template.md` - Finding documentation template

**Usage**: Automatically invoked when user asks to review code

```
User: "Review this React component"

Claude: [Automatically loads Code Review Skill]
        [Analyzes code against checklist]
        [Runs metrics scripts]
        [Provides comprehensive review]
```

### 2. Brand Voice Skill
**Location**: `brand-voice/`

**Purpose**: Ensure consistent brand voice in all communications

**Contents**:
- `SKILL.md` - Brand guidelines and tone rules
- `templates/email-template.txt` - Email format
- `templates/social-post-template.txt` - Social media format
- `tone-examples.md` - Example messages in brand voice

**Usage**: Automatically invoked when creating marketing copy or customer communications

### 3. Documentation Generator Skill
**Location**: `doc-generator/`

**Purpose**: Generate comprehensive API documentation from source code

**Contents**:
- `SKILL.md` - Documentation standards and structure
- `generate-docs.py` - Python script to extract API docs from code

**Usage**: Automatically invoked when creating or updating API documentation

## How Skills Work

Skills are:
- **Auto-invoked** - Claude detects when to use them based on user request
- **Reusable** - Define once, use across projects
- **Packaged** - Include instructions, scripts, and templates
- **Metadata-driven** - YAML frontmatter defines when to use

## Skill Structure

```
skill-name/
├── SKILL.md          # Main skill definition (required)
├── scripts/          # Helper scripts (optional)
│   └── helper.py
├── templates/        # Document templates (optional)
│   └── template.md
└── README.md         # Usage documentation (optional)
```

## SKILL.md Format

```yaml
---
name: Skill Name
description: What this skill does
version: "1.0.0"
tags:
  - category
  - use-case
when_to_use: When users ask to...
---

# Skill Instructions

Detailed instructions for Claude on how to execute this skill.
```

## Skill Discovery

Claude automatically:
1. Scans available skills
2. Matches user request to skill metadata
3. Loads relevant skill instructions
4. Executes skill with full context

## When to Use Skills

| Scenario | Use Skill | Why |
|----------|-----------|-----|
| Repeated workflow | ✅ Yes | Standardize process |
| Domain expertise | ✅ Yes | Package knowledge |
| Quality standards | ✅ Yes | Ensure consistency |
| One-time task | ❌ No | Not worth packaging |
| Simple request | ❌ No | Use slash command |

## Skills vs Other Features

| Feature | Invocation | Best For |
|---------|-----------|----------|
| **Skills** | Auto-invoked | Automated workflows |
| **Slash Commands** | Manual (`/cmd`) | Quick shortcuts |
| **Subagents** | Auto-delegated | Task distribution |
| **Memory** | Auto-loaded | Long-term context |

## Creating Custom Skills

1. Create skill directory structure
2. Write SKILL.md with metadata and instructions
3. Add scripts and templates as needed
4. Test by copying to skills directory
5. Refine based on usage

## Best Practices

### Do's ✅
- Use clear, descriptive names
- Include comprehensive instructions
- Add concrete examples
- Document when to use the skill
- Package related scripts and templates
- Test with real scenarios

### Don'ts ❌
- Don't create skills for one-time tasks
- Don't duplicate existing functionality
- Don't make skills too broad
- Don't forget metadata in SKILL.md
- Don't skip examples

## Making Scripts Executable

```bash
chmod +x code-review/scripts/*.py
chmod +x doc-generator/*.py
```

## Example Usage Scenarios

### Code Review Workflow
```
User: "Review this authentication module for security issues"

Claude:
1. Detects "review" + "security" keywords
2. Loads Code Review Skill
3. Runs security checklist
4. Executes analyze-metrics.py
5. Provides detailed review with finding template
```

### Brand Voice Check
```
User: "Write an email announcing our new feature"

Claude:
1. Detects marketing/communication request
2. Loads Brand Voice Skill
3. Applies brand guidelines
4. Uses email template
5. Ensures consistent tone
```

### API Documentation
```
User: "Generate API docs for this endpoint"

Claude:
1. Detects API documentation request
2. Loads Documentation Generator Skill
3. Runs generate-docs.py if needed
4. Follows documentation structure
5. Creates comprehensive docs with examples
```

## Additional Resources

- [Skills Cookbook](https://github.com/anthropic-ai/skills)
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Skill Development Best Practices](https://docs.claude.com)

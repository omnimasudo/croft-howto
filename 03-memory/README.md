# Memory Examples

This folder contains example CLAUDE.md files for different memory scopes in Claude Code.

## Memory Types

### 1. Project Memory (`project-CLAUDE.md`)
**Location**: `./CLAUDE.md` or `./.claude/CLAUDE.md`

**Purpose**: Team-wide project standards and configurations

**Installation**:
```bash
cp project-CLAUDE.md /path/to/your/project/CLAUDE.md
```

**Contains**:
- Project overview and tech stack
- Development standards
- Naming conventions
- Git workflow
- Testing requirements
- API standards
- Common commands
- Team contacts

### 2. Directory-Specific Memory (`directory-api-CLAUDE.md`)
**Location**: `./src/api/CLAUDE.md`

**Purpose**: Override or extend project memory for specific directories

**Installation**:
```bash
cp directory-api-CLAUDE.md /path/to/your/project/src/api/CLAUDE.md
```

**Contains**:
- API-specific standards
- Request validation rules
- Authentication requirements
- Response formats
- Pagination standards
- Rate limiting
- Caching strategy

### 3. Personal Memory (`personal-CLAUDE.md`)
**Location**: `~/.claude/CLAUDE.md`

**Purpose**: Personal preferences across all projects

**Installation**:
```bash
cp personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**Contains**:
- Personal coding preferences
- Communication style
- Debugging preferences
- Project organization
- Tooling preferences

## Memory Hierarchy

Claude searches for memory in this order:

1. **Project Root** (`./CLAUDE.md`) - Highest priority
2. **Subdirectory** (`./subdir/CLAUDE.md`) - Directory-specific
3. **Personal** (`~/.claude/CLAUDE.md`) - Lowest priority

## Usage

Memory is automatically loaded by Claude Code when starting a session.

### Updating Memory During Session

```markdown
User: Remember that I prefer using async/await instead of promises

Claude: I'll add that to your memory. Which memory file?
1. Project memory (./CLAUDE.md)
2. Personal memory (~/.claude/CLAUDE.md)

User: Project memory

Claude: ✅ Memory saved!
```

## File Imports

You can import other markdown files in your CLAUDE.md:

```markdown
## Architecture
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md
```

## Best Practices

### Do's ✅
- Keep memory files organized and up-to-date
- Use project memory for team standards
- Use personal memory for individual preferences
- Version control project memory with git
- Import large docs instead of duplicating

### Don'ts ❌
- Don't store secrets or credentials
- Don't duplicate content across memory files
- Don't create too many subdirectory overrides
- Don't make memory files too long (>500 lines)

## Memory vs Other Features

| Feature | Persistence | Scope | Best For |
|---------|------------|-------|----------|
| **Memory** | Cross-session | User/Project | Long-term context |
| **Slash Commands** | Session only | Command | Quick shortcuts |
| **MCP** | Real-time | External data | Live information |
| **Skills** | Filesystem | Reusable | Automated workflows |

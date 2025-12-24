# Project Context

## Purpose

**Claude How To** is a comprehensive educational repository providing examples and documentation for Claude Code features and concepts. The project serves as:

- A learning resource for developers new to Claude Code
- A reference collection of example configurations (slash commands, memory, skills, subagents, MCP, hooks, plugins, checkpoints, advanced features)
- A tool for generating offline documentation (EPUB format)

**Goals:**
1. Provide clear, numbered learning paths (01-09) for Claude Code features
2. Include ready-to-use example configurations users can copy to their projects
3. Generate an EPUB ebook from the documentation for offline reading
4. Maintain high-quality Python tooling with CI/CD automation

## Tech Stack

### Primary Technologies
- **Python 3.10+** - EPUB builder script and tooling
- **Markdown** - Documentation content (all guides and examples)
- **JSON/YAML** - Configuration files (MCP configs, plugin definitions)
- **Shell Scripts** - Hook examples in `06-hooks/`

### Python Dependencies
- `ebooklib` - EPUB generation
- `markdown` - Markdown to HTML conversion
- `beautifulsoup4` - HTML parsing/manipulation
- `httpx` - HTTP client (for Mermaid diagram rendering)
- `pillow` - Image processing
- `tenacity` - Retry logic for external API calls

### Development Tools
- `uv` - Python package manager and virtual environment
- `ruff` - Linting and formatting (replaces black, isort, flake8)
- `bandit` - Security scanning
- `pytest` / `pytest-asyncio` - Testing framework
- `pre-commit` - Git hooks for code quality

### CI/CD
- **GitHub Actions** - Automated linting, security scanning, testing, and EPUB builds
- Workflows in `.github/workflows/ci.yml` and `.github/workflows/release.yml`

## Project Conventions

### Code Style
- **Python**: Ruff for linting and formatting
  - Line length: 88 characters
  - Target: Python 3.10
  - Double quotes, space indentation
  - Import sorting: isort rules via Ruff
- **Markdown**: Standard GitHub-Flavored Markdown
- **YAML/JSON**: Validated via pre-commit hooks

### Architecture Patterns
- **Numbered directories** (01-09) for learning progression
- **Each feature folder** contains:
  - Example files demonstrating the feature
  - `README.md` with detailed explanations
- **Scripts directory** contains Python tooling:
  - `build_epub.py` - Main EPUB builder with async Mermaid rendering
  - `tests/` - pytest test suite

### Testing Strategy
- **Unit tests** in `scripts/tests/`
- **Pytest** with `pytest-asyncio` for async code
- **CI runs tests** on every push/PR to `main`
- **Test coverage** focused on EPUB builder functionality

### Git Workflow
- **Main branch**: `main`
- **PRs required** for contributions
- **Pre-commit hooks** enforce:
  - Ruff lint and format
  - Bandit security scan
  - YAML/TOML validation
  - Trailing whitespace and EOF fixes
- **Commit messages**: Descriptive, no co-author attribution required
- **No time estimates** in commits or PRs

## Domain Context

### Claude Code Concepts
This repository covers nine major Claude Code features:

1. **Slash Commands** - User-invoked shortcuts (`/optimize`, `/pr`)
2. **Memory** - Persistent context via `CLAUDE.md` files
3. **Skills** - Auto-invoked reusable capabilities
4. **Subagents** - Specialized AI assistants with isolated contexts
5. **MCP Protocol** - External tool/API access
6. **Hooks** - Event-driven shell command automation
7. **Plugins** - Bundled feature collections
8. **Checkpoints** - Session snapshots and rewind
9. **Advanced Features** - Planning mode, extended thinking, background tasks

### Installation Targets
Examples are designed to be copied to:
- `~/.claude/` - Personal/global configurations
- `.claude/` - Project-specific configurations
- Root project directory - For `CLAUDE.md` memory files

## Important Constraints

- **Python 3.10+** required for all scripts
- **Virtual environment** must be activated before running Python (configured in `~/.claude/CLAUDE.md`)
- **No Claude co-author** in commit messages (per user preferences)
- **No auto-commits/pushes** without explicit user request
- **Large files** limited to 1MB (pre-commit hook)
- **Security scans** must pass (Bandit)

## External Dependencies

### External Services
- **Mermaid.ink API** - Renders Mermaid diagrams to images for EPUB
  - Used in `build_epub.py` with retry logic via `tenacity`
  - Rate limiting handled with exponential backoff

### GitHub Integration
- **GitHub Actions** for CI/CD
- **GitHub Releases** for versioned EPUB distribution
- Example MCP configurations reference GitHub API tokens

### No Runtime External Dependencies
- Documentation is static markdown
- EPUB can be built offline (diagrams cached or skip rendering)

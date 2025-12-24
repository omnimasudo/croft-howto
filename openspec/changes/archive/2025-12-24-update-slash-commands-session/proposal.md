# Change: Update Slash Commands Documentation

## Why

The current slash commands documentation in `01-slash-commands/README.md` is outdated compared to the official Claude Code documentation at https://code.claude.com/docs/en/slash-commands. Several new features, built-in commands, and capabilities have been added that users should know about.

## What Changes

### Documentation Updates

- **Add comprehensive built-in commands table** - Document all 40+ built-in slash commands with their purposes
- **Update custom command features** - Document new argument handling (`$ARGUMENTS`, `$1`, `$2`, etc.)
- **Add bash execution syntax** - Document the `!` prefix for executing bash commands within slash commands
- **Update frontmatter fields** - Document `allowed-tools`, `argument-hint`, `description`, `model`, `disable-model-invocation`
- **Add file reference syntax** - Document the `@` prefix for including file contents
- **Add Plugin commands section** - Document `/plugin-name:command-name` pattern
- **Add MCP slash commands section** - Document `/mcp__<server-name>__<prompt-name>` pattern
- **Add SlashCommand Tool section** - Document programmatic invocation from Claude
- **Add Skills vs Slash Commands comparison** - Help users choose the right tool

### Example Updates

- Add example command with bash execution (`!git status`)
- Add example with file references (`@src/utils/helpers.js`)
- Add example with complete frontmatter
- Update existing examples to use official syntax

## Impact

- Affected specs: `slash-commands` (new capability spec to be created)
- Affected code: `01-slash-commands/README.md`, potentially new example files
- No breaking changes - additive documentation improvements
- Benefits all users learning about Claude Code slash commands

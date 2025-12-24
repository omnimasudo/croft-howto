## 1. Documentation Structure Updates

- [x] 1.1 Add "Types of Slash Commands" section with overview of built-in, custom, plugin, and MCP commands
- [x] 1.2 Create comprehensive built-in commands reference table (40+ commands)
- [x] 1.3 Update custom commands section with new features

## 2. Custom Command Features

- [x] 2.1 Document `$ARGUMENTS` placeholder for all arguments
- [x] 2.2 Document individual argument placeholders (`$1`, `$2`, `$3`, etc.)
- [x] 2.3 Document bash execution with `!` prefix (e.g., `!git status`)
- [x] 2.4 Document file references with `@` prefix (e.g., `@src/file.js`)
- [x] 2.5 Document thinking mode trigger via keywords

## 3. Frontmatter Updates

- [x] 3.1 Update frontmatter section with official fields
- [x] 3.2 Document `allowed-tools` field with examples
- [x] 3.3 Document `argument-hint` field for auto-completion
- [x] 3.4 Document `description` field
- [x] 3.5 Document `model` field for specific model selection
- [x] 3.6 Document `disable-model-invocation` field

## 4. New Sections

- [x] 4.1 Add "Plugin Commands" section with `/plugin-name:command-name` pattern
- [x] 4.2 Add "MCP Slash Commands" section with `/mcp__<server-name>__<prompt-name>` pattern
- [x] 4.3 Add "SlashCommand Tool" section for programmatic invocation
- [x] 4.4 Add "Skills vs Slash Commands" comparison table

## 5. Example Files

- [x] 5.1 Create new example showing bash execution feature (commit.md)
- [x] 5.2 Create new example showing file references (commit.md includes @package.json example in README)
- [x] 5.3 Update existing examples to use official frontmatter format (removed name/tags, added allowed-tools)
- [x] 5.4 Add commit command example (from official docs)

## 6. Validation

- [x] 6.1 Verify all links work correctly
- [x] 6.2 Test example commands format
- [x] 6.3 Review for consistency with official documentation

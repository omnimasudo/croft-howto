## ADDED Requirements

### Requirement: Slash Command Types Documentation

The documentation SHALL describe the four types of slash commands:
1. Built-in commands provided by Claude Code
2. Custom user-defined commands (project and personal)
3. Plugin commands
4. MCP (Model Context Protocol) slash commands

#### Scenario: User learns about command types
- **WHEN** a user reads the slash commands documentation
- **THEN** they understand the different types of slash commands available
- **AND** they know when to use each type

---

### Requirement: Built-in Commands Reference

The documentation SHALL include a comprehensive reference table of all built-in slash commands with their purposes, including but not limited to:
- `/add-dir` - Add additional working directories
- `/agents` - Manage custom AI subagents
- `/clear` - Clear conversation history
- `/compact` - Compact conversation with optional focus instructions
- `/config` - Open Settings interface
- `/context` - Visualize current context usage
- `/cost` - Show token usage statistics
- `/doctor` - Check installation health
- `/export` - Export conversation to file or clipboard
- `/help` - Get usage help
- `/hooks` - Manage hook configurations
- `/init` - Initialize project with CLAUDE.md
- `/mcp` - Manage MCP server connections
- `/memory` - Edit CLAUDE.md memory files
- `/model` - Select or change AI model
- `/permissions` - View or update permissions
- `/resume` - Resume conversation by ID or name
- `/review` - Request code review
- `/sandbox` - Enable sandboxed bash tool
- `/vim` - Enter vim mode

#### Scenario: User finds built-in command
- **WHEN** a user needs to perform a common operation
- **THEN** they can find the appropriate built-in command in the reference table
- **AND** they understand what the command does

---

### Requirement: Argument Handling

The documentation SHALL explain both argument handling methods:
1. `$ARGUMENTS` - Receives all arguments as a single string
2. `$1`, `$2`, `$3`, etc. - Individual positional arguments

#### Scenario: User uses $ARGUMENTS placeholder
- **WHEN** a user creates a command with `$ARGUMENTS` placeholder
- **AND** invokes it with `/fix-issue 123 high-priority`
- **THEN** `$ARGUMENTS` contains "123 high-priority"

#### Scenario: User uses positional arguments
- **WHEN** a user creates a command with `$1`, `$2`, `$3` placeholders
- **AND** invokes it with `/review-pr 456 high alice`
- **THEN** `$1` is "456", `$2` is "high", `$3` is "alice"

---

### Requirement: Bash Command Execution

The documentation SHALL explain the `!` prefix for executing bash commands within slash command files before the command runs.

#### Scenario: User includes dynamic context
- **WHEN** a user adds `!git status` in their command file
- **THEN** the git status output is included in the command context
- **AND** Claude receives the current repository state

---

### Requirement: File Reference Syntax

The documentation SHALL explain the `@` prefix for including file contents in slash commands.

#### Scenario: User references a file
- **WHEN** a user adds `@src/utils/helpers.js` in their command file
- **THEN** the contents of that file are included in the command context

---

### Requirement: Frontmatter Fields

The documentation SHALL document all supported frontmatter fields:
- `allowed-tools` - List of tools the command can use
- `argument-hint` - Expected arguments for auto-completion
- `description` - Brief description of the command
- `model` - Specific model to use for this command
- `disable-model-invocation` - Prevent SlashCommand tool from calling this command

#### Scenario: User creates command with frontmatter
- **WHEN** a user creates a command with frontmatter fields
- **THEN** Claude Code respects those configuration options
- **AND** the command behaves according to the specified settings

---

### Requirement: Plugin Commands Documentation

The documentation SHALL explain the plugin command format: `/plugin-name:command-name` or simply `/command-name` when there are no naming conflicts.

#### Scenario: User invokes plugin command
- **WHEN** a user types `/frontend-design:frontend-design`
- **THEN** the corresponding plugin command executes

---

### Requirement: MCP Slash Commands Documentation

The documentation SHALL explain the MCP slash command format: `/mcp__<server-name>__<prompt-name> [arguments]`

#### Scenario: User invokes MCP command
- **WHEN** a user types `/mcp__github__list_prs`
- **THEN** the MCP server's prompt is executed

---

### Requirement: SlashCommand Tool Documentation

The documentation SHALL explain how Claude can programmatically invoke slash commands using the SlashCommand tool, including:
- How to enable this via prompt or CLAUDE.md references
- How to disable via permissions
- The character budget limit (default 15,000, configurable via `SLASH_COMMAND_TOOL_CHAR_BUDGET`)

#### Scenario: User enables programmatic invocation
- **WHEN** a user adds "Run /write-unit-test when writing tests" to CLAUDE.md
- **THEN** Claude can automatically invoke that command when appropriate

---

### Requirement: Skills vs Slash Commands Comparison

The documentation SHALL include a comparison table helping users choose between Skills and Slash Commands based on:
- Best use cases for each
- File structure differences
- Invocation method (explicit vs automatic)
- Complexity level

#### Scenario: User decides between skill and command
- **WHEN** a user needs to create a reusable capability
- **THEN** they can use the comparison to decide whether a slash command or skill is more appropriate

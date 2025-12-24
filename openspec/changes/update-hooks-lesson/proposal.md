# Change: Update Hooks Lesson Based on Official Documentation

## Why

The current hooks lesson (`blog-posts/06-hooks.md`) contains outdated and inaccurate information that doesn't match the official Claude Code hooks documentation. Key issues include:

1. **Incorrect hook event names**: Uses `PreToolUse:Write`, `PreCommit`, `PostCommit`, `PrePush` which don't exist
2. **Missing hook events**: Doesn't cover `PermissionRequest`, `Stop`, `SubagentStop`, `PreCompact`, `SessionStart` (with matchers), `SessionEnd`
3. **Wrong configuration format**: Shows string-based hook commands instead of the array-based matcher/hooks structure
4. **Missing hook input/output**: Doesn't explain JSON stdin input or structured JSON output
5. **Missing exit code semantics**: Exit code 2 for blocking vs other non-zero codes
6. **Missing prompt-based hooks**: No coverage of `type: "prompt"` hooks for LLM-based evaluation
7. **Missing security considerations**: No disclaimer or security best practices from official docs
8. **Incorrect variable references**: Uses `${file_path}`, `${command}` instead of JSON stdin input

## What Changes

- **BREAKING**: Complete rewrite of hook event types and configuration format
- Update all code examples to use correct array-based configuration structure
- Add coverage of all 9 hook events: `PreToolUse`, `PermissionRequest`, `PostToolUse`, `Notification`, `UserPromptSubmit`, `Stop`, `SubagentStop`, `PreCompact`, `SessionStart`, `SessionEnd`
- Add JSON hook input/output documentation with examples
- Add hook matchers (tool patterns, regex support)
- Add prompt-based hooks for `Stop`/`SubagentStop`
- Add security considerations section with official disclaimer
- Add environment variables section (`CLAUDE_PROJECT_DIR`, `CLAUDE_ENV_FILE`, `CLAUDE_CODE_REMOTE`)
- Add plugin hooks documentation
- Add MCP tool hook patterns (`mcp__<server>__<tool>`)
- Update debugging section with `claude --debug` and verbose mode
- Remove incorrect/non-existent hook types (`PreCommit`, `PostCommit`, `PrePush`)

## Impact

- **Affected specs**: hooks-documentation (new capability)
- **Affected code**: `blog-posts/06-hooks.md` (complete rewrite)
- **Affected examples**: Any example hook scripts in the repo need updating to use JSON stdin
- **User impact**: Users following the current guide will have non-functional hooks; this update provides correct, working examples

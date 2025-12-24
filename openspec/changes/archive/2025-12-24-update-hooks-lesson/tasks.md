# Tasks: Update Hooks Lesson

## 1. Content Structure Update
- [x] 1.1 Update introduction to explain hooks as event-driven automation scripts
- [x] 1.2 Replace hook architecture diagram with correct event flow
- [x] 1.3 Update hook types table with all 9 official hook events

## 2. Configuration Format
- [x] 2.1 Rewrite configuration section with array-based matcher/hooks structure
- [x] 2.2 Add hook matcher documentation (exact match, regex patterns, wildcards)
- [x] 2.3 Add timeout configuration examples

## 3. Hook Events Documentation
- [x] 3.1 Document PreToolUse event (matchers, decision control, updatedInput)
- [x] 3.2 Document PermissionRequest event (decision behavior, messages)
- [x] 3.3 Document PostToolUse event (block decision, additionalContext)
- [x] 3.4 Document Notification event (matchers: permission_prompt, idle_prompt, etc.)
- [x] 3.5 Document UserPromptSubmit event (block decision, context addition)
- [x] 3.6 Document Stop event (block continuation, stop_hook_active)
- [x] 3.7 Document SubagentStop event (subagent completion handling)
- [x] 3.8 Document PreCompact event (manual vs auto matchers)
- [x] 3.9 Document SessionStart event (startup/resume/clear/compact matchers, CLAUDE_ENV_FILE)
- [x] 3.10 Document SessionEnd event (reason field)

## 4. Hook Input/Output
- [x] 4.1 Document JSON stdin input structure (session_id, transcript_path, cwd, etc.)
- [x] 4.2 Document exit code semantics (0=success, 2=blocking error, other=non-blocking)
- [x] 4.3 Document JSON stdout output structure (continue, stopReason, hookSpecificOutput)
- [x] 4.4 Add examples for each hook event's specific output format

## 5. Prompt-Based Hooks
- [x] 5.1 Add section on type="prompt" hooks for Stop/SubagentStop
- [x] 5.2 Document LLM response schema (decision, reason, continue, stopReason)
- [x] 5.3 Add practical examples of intelligent stop hooks

## 6. Environment Variables
- [x] 6.1 Document CLAUDE_PROJECT_DIR usage
- [x] 6.2 Document CLAUDE_ENV_FILE for SessionStart env persistence
- [x] 6.3 Document CLAUDE_CODE_REMOTE for web environment detection
- [x] 6.4 Document plugin hook variables (${CLAUDE_PLUGIN_ROOT})

## 7. Security Section
- [x] 7.1 Add official security disclaimer (USE AT YOUR OWN RISK)
- [x] 7.2 Document security best practices (input validation, quoting, path traversal)
- [x] 7.3 Add configuration safety notes (snapshot at startup, modification warnings)

## 8. Advanced Features
- [x] 8.1 Add MCP tool hook patterns (mcp__<server>__<tool>)
- [x] 8.2 Add plugin hooks documentation
- [x] 8.3 Add project-specific hook script examples

## 9. Debugging and Troubleshooting
- [x] 9.1 Update debugging section with claude --debug flag
- [x] 9.2 Add verbose mode (ctrl+o) documentation
- [x] 9.3 Update troubleshooting with correct error scenarios

## 10. Example Scripts
- [x] 10.1 Rewrite format-code hook to use JSON stdin
- [x] 10.2 Rewrite security-scan hook with proper JSON input parsing
- [x] 10.3 Rewrite bash command validator example from official docs
- [x] 10.4 Add intelligent stop hook example with prompt type
- [x] 10.5 Remove non-existent PreCommit/PostCommit/PrePush examples

## 11. Final Cleanup
- [x] 11.1 Update Mermaid diagrams for accuracy
- [x] 11.2 Update variable reference table to reflect JSON input
- [x] 11.3 Update best practices table
- [x] 11.4 Update directory structure section
- [x] 11.5 Verify all links and references

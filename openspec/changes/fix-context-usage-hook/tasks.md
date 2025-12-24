# Tasks: Fix Context Usage Hook Token Calculation

## Implementation Tasks

### 1. Fix the bug in 06-hooks/README.md example
- [ ] Update line 564 in the context-usage.py example: change `estimate_tokens(str(total_chars))` to `total_chars // 4`
- [ ] Remove the now-unused `estimate_tokens()` function from the example

### 2. Update user's local hook file
- [ ] Fix `~/.claude/hooks/context-usage.py` with the same correction

### 3. Verification
- [ ] Test the hook by running Claude Code and confirming non-zero token count is displayed
- [ ] Verify the percentage calculation is reasonable (should show usage increasing during conversation)

## Acceptance Criteria

- [ ] After Claude responds, the Stop hook displays a non-zero token estimate
- [ ] The displayed percentage decreases as conversation grows
- [ ] Example in README.md matches the corrected implementation

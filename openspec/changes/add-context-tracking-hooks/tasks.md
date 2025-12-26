# Tasks: Add Context Usage Tracking Documentation

## 1. Documentation Updates

- [x] 1.1 Add "Context Tracking Hook Pairs" section to README explaining pre-message/post-response concept
- [x] 1.2 Document how UserPromptSubmit serves as pre-message hook
- [x] 1.3 Document how Stop serves as post-response hook
- [x] 1.4 Explain token delta calculation methodology

## 2. Example Scripts

- [x] 2.1 Create `context-tracker.py` example script with character estimation (zero dependencies)
- [x] 2.2 Create `context-tracker-tiktoken.py` example script with tiktoken method (more accurate)
- [x] 2.3 Implement UserPromptSubmit handler (save pre-message count)
- [x] 2.4 Implement Stop handler (calculate and report delta)
- [x] 2.5 Add clear inline comments explaining both approaches

## 3. Configuration Examples

- [x] 3.1 Add hook configuration example for UserPromptSubmit event
- [x] 3.2 Add hook configuration example for Stop event
- [x] 3.3 Provide combined configuration showing both hooks together

## 4. Token Counting Methods Documentation

- [x] 4.1 Document tiktoken with p50k_base method (more accurate, ~90-95%)
- [x] 4.2 Document character-based estimation method (simple, ~80-90%)
- [x] 4.3 Create comparison table of both offline methods
- [x] 4.4 Explain what's included/excluded from transcript
- [x] 4.5 Add caveat that no official Claude offline tokenizer exists

## 5. Validation

- [x] 5.1 Test example script with sample JSON input
- [x] 5.2 Verify configuration examples have valid JSON syntax
- [x] 5.3 Run openspec validate to confirm proposal is complete

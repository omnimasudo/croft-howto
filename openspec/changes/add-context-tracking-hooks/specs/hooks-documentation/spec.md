# hooks-documentation Spec Delta

## ADDED Requirements

### Requirement: Pre-Message and Post-Response Hook Pairs Documentation
The hooks lesson SHALL document how to use `UserPromptSubmit` and `Stop` hooks together for context/token usage tracking.

#### Scenario: Understanding hook event timing for context tracking
- **WHEN** a user wants to track per-request token consumption
- **THEN** they find documentation explaining that `UserPromptSubmit` fires before the prompt is processed (pre-message)
- **AND** they find documentation explaining that `Stop` fires after Claude completes its response (post-response)
- **AND** they understand how to calculate the delta between these two points

#### Scenario: Token delta calculation methodology
- **WHEN** a user implements a context tracking hook pair
- **THEN** they find documentation explaining how to:
  - Record token count at `UserPromptSubmit` time
  - Calculate new token count at `Stop` time
  - Compute the delta representing per-request consumption

### Requirement: Context Tracking Hook Pair Example
The hooks lesson SHALL provide a working example script that tracks context usage using pre-message and post-response hooks.

#### Scenario: Single script handles both hook events
- **WHEN** a user copies the context-tracker.py example
- **THEN** the script detects the hook event type via `hook_event_name`
- **AND** handles `UserPromptSubmit` by saving current token estimate to a temp file
- **AND** handles `Stop` by loading the saved count, calculating delta, and reporting usage

#### Scenario: Complete configuration for hook pair
- **WHEN** a user wants to configure both hooks
- **THEN** they find a complete settings.json example showing:
  - `UserPromptSubmit` hook configuration pointing to the context tracker script
  - `Stop` hook configuration pointing to the same script
  - Both hooks using the same script for consistent token calculation

#### Scenario: Per-request usage reporting
- **WHEN** the context tracking hooks execute
- **THEN** the Stop hook outputs a report showing:
  - Total estimated tokens used in session
  - Tokens consumed by the current request (delta)
  - Remaining capacity estimate

### Requirement: Token Counting Methods Documentation
The hooks lesson SHALL document two offline token counting methods that require no API key.

#### Scenario: tiktoken-based token counting documented
- **WHEN** a user wants more accurate offline token counts
- **THEN** they find documentation for using `tiktoken` with `p50k_base` encoding
- **AND** they see a Python example using `tiktoken.get_encoding("p50k_base")`
- **AND** they understand it provides ~90-95% accuracy compared to Claude's tokenizer
- **AND** they learn it requires the `tiktoken` dependency

#### Scenario: Character estimation token counting documented
- **WHEN** a user wants zero-dependency token estimation
- **THEN** they find documentation for the ~4 characters per token estimation ratio
- **AND** they understand this provides ~80-90% accuracy for English text
- **AND** they learn it works with no external dependencies

#### Scenario: Method comparison provided
- **WHEN** a user needs to choose between token counting methods
- **THEN** they find a comparison showing:
  - tiktoken method: ~90-95% accuracy, requires tiktoken, <10ms latency
  - Estimation method: ~80-90% accuracy, no dependencies, <1ms latency
- **AND** both methods work completely offline without API keys

#### Scenario: Transcript contents explained
- **WHEN** a user wants to understand what's included in token counts
- **THEN** they find documentation explaining that the transcript includes:
  - User prompts
  - Claude's responses
  - Tool inputs and outputs
- **AND** they understand that system prompts and internal context are NOT included

#### Scenario: No official Claude tokenizer caveat
- **WHEN** a user reads about token counting accuracy
- **THEN** they understand that Anthropic hasn't released an official offline tokenizer
- **AND** they understand both methods are approximations based on similar BPE tokenizers

## MODIFIED Requirements

### Requirement: Context Usage Reporting Hook Example
The hooks lesson SHALL include a correct, working example showing how to create a hook that reports context/token usage after each Claude response.

#### Scenario: Token calculation is correct
- **WHEN** a user copies the context-usage.py example
- **AND** runs it as a Stop hook
- **THEN** the hook correctly calculates estimated tokens from total character count
- **AND** displays a non-zero token count proportional to conversation length

#### Scenario: User learns to create context monitoring hook
- **WHEN** a user reads the context usage reporter example
- **THEN** they find a complete Python script that reads the transcript file
- **AND** they understand how to estimate token usage from conversation history
- **AND** they see the configuration for Stop hooks
- **AND** they understand the limitations of token estimation

#### Scenario: Hook output format is documented
- **WHEN** a user implements the context usage hook
- **THEN** they can generate a one-line report showing used tokens and remaining capacity
- **AND** the output shows realistic token counts based on conversation size

#### Scenario: Delta-based tracking is documented
- **WHEN** a user wants per-request token consumption
- **THEN** they find documentation pointing to the pre-message/post-response hook pair approach
- **AND** they understand how to use `UserPromptSubmit` + `Stop` for delta calculation

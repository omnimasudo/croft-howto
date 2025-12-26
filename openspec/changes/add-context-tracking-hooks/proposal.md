# Change: Add Context Usage Tracking Documentation via Pre-Message and Post-Response Hooks

## Why

Users want to monitor token consumption per request and overall context usage throughout a Claude Code session. Currently, the hooks documentation shows a basic context-usage example using the Stop hook, but it doesn't demonstrate how to track **per-request** token consumption by comparing measurements at two points in time.

By documenting how to use `UserPromptSubmit` as a "pre-message" hook and `Stop` as a "post-response" hook, users can calculate the delta in token usage for each request, enabling accurate per-request consumption metrics.

## What Changes

- **ADDED**: Documentation for using `UserPromptSubmit` and `Stop` hooks together for context tracking
- **ADDED**: A new example demonstrating token delta calculation between pre-message and post-response
- **MODIFIED**: Enhance the existing context usage reporting requirement with delta-based tracking approach
- **ADDED**: Detailed explanation of token estimation methodology and its limitations

## Impact

- Affected specs: `hooks-documentation`
- Affected code: `06-hooks/README.md` (documentation updates)
- No breaking changes - purely additive documentation

## Technical Analysis

### Current Hook Events Mapping

| Desired Hook | Claude Code Event | Trigger Point |
|--------------|-------------------|---------------|
| Pre-Message Hook | `UserPromptSubmit` | Before user prompt is processed by the model |
| Post-Response Hook | `Stop` | After model completes its full response |

### Token Counting Methods (Offline, No API Key)

Since we need offline token counting without an API key, we offer **two local approaches**:

#### Method 1: tiktoken with p50k_base (More Accurate)

Use OpenAI's `tiktoken` library with the `p50k_base` encoding as an approximation for Claude's tokenizer:

```python
import tiktoken

enc = tiktoken.get_encoding("p50k_base")
tokens = enc.encode(text)
token_count = len(tokens)
```

**Pros:**
- More accurate than character estimation (~90-95% accuracy)
- Works completely offline
- No API key required
- Fast execution

**Cons:**
- Requires `tiktoken` dependency (`pip install tiktoken`)
- Not Claude's exact tokenizer (approximation)

#### Method 2: Character-Based Estimation (Simplest)

For zero-dependency estimation:

```python
estimated_tokens = len(text) // 4
```

**Pros:**
- No dependencies at all
- Works offline
- Extremely fast

**Cons:**
- Less accurate (~80-90% for English text)
- Varies more with code and non-English text

### Token Delta Calculation Approach

1. **Pre-Message (UserPromptSubmit)**: Read transcript, count tokens (via tiktoken or estimation)
2. **Post-Response (Stop)**: Read transcript again, calculate new total, compute delta

**Accuracy Evaluation:**

| Factor | tiktoken Method | Character Estimation |
|--------|-----------------|---------------------|
| Token accuracy | ~90-95% | ~80-90% |
| Dependencies | tiktoken | None |
| Speed | Fast (<10ms) | Very fast (<1ms) |
| Offline | Yes | Yes |

### Limitations

- **No official offline Claude tokenizer exists** - Anthropic hasn't released their tokenizer publicly
- System prompts and internal Claude Code context are NOT in the transcript
- The delta includes: user prompt + Claude's response + any tool outputs
- Both methods are approximations; actual API token counts may differ slightly

## Open Questions

1. Should we persist the pre-message count to a file, or can we rely on the hook's transient state?
   - **Recommendation**: Use a simple temp file in the session directory for reliability
2. Should the example be a single Python script handling both hooks, or two separate scripts?
   - **Recommendation**: Single script with mode detection based on `hook_event_name`

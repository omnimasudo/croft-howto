# Design: Context Usage Tracking via Hook Pairs

## Context

Users need visibility into token consumption during Claude Code sessions. While Claude Code provides internal context management, users lack tools to:
- Track token usage per request
- Monitor cumulative context growth
- Understand when they're approaching context limits

The existing `Stop` hook example provides cumulative usage but not per-request deltas.

## Goals / Non-Goals

### Goals
- Document a reliable method to track per-request token consumption
- Provide a working example users can copy and modify
- Explain the methodology and its limitations clearly
- Use existing hook events (`UserPromptSubmit`, `Stop`) without requiring new capabilities

### Non-Goals
- Implement actual token counting (we use character-based estimation)
- Access internal Claude Code context metrics
- Modify Claude Code's behavior or internal state
- Track system prompt tokens (not in transcript)

## Decisions

### Decision 1: Use UserPromptSubmit + Stop Hook Pair
**What**: Use `UserPromptSubmit` as the "pre-message" hook and `Stop` as the "post-response" hook.

**Why**: These are the natural lifecycle points:
- `UserPromptSubmit` fires before the prompt is sent to the model
- `Stop` fires after Claude completes its response

**Alternatives Considered**:
| Option | Pros | Cons |
|--------|------|------|
| SessionStart + Stop | Captures full session | No per-request granularity |
| PreToolUse + PostToolUse | Captures tool overhead | Missing prompt/response tokens |
| UserPromptSubmit + Stop | Natural request boundaries | Requires temp file for state |

### Decision 2: Use Temp File for State Persistence
**What**: Store pre-message token count in a temp file keyed by session ID.

**Why**: Hooks are stateless processes; we need persistence between the two hook invocations.

**Implementation**:
```python
import tempfile
import os

def get_state_file(session_id: str) -> str:
    return os.path.join(tempfile.gettempdir(), f"claude-tokens-{session_id}.json")
```

### Decision 3: Single Script with Mode Detection
**What**: One Python script handles both hooks, detecting mode via `hook_event_name`.

**Why**:
- Reduces file count and complexity
- Ensures consistent token calculation logic
- Easier for users to understand and modify

**Structure**:
```python
def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name")

    if event == "UserPromptSubmit":
        record_pre_message_count(data)
    elif event == "Stop":
        report_delta(data)
```

### Decision 4: Two Offline Token Counting Methods (No API Key)
**What**: Provide two offline methods - tiktoken-based and simple character estimation.

**Why**:
- No API key should be required for context tracking hooks
- Anthropic hasn't released an official offline tokenizer
- Users have different dependency tolerance levels

#### Method A: tiktoken with p50k_base (Recommended)

```python
import tiktoken

def count_tokens_tiktoken(text: str) -> int:
    enc = tiktoken.get_encoding("p50k_base")
    return len(enc.encode(text))
```

**Characteristics**:
- ~90-95% accuracy compared to Claude's actual tokenizer
- Works completely offline
- Requires `tiktoken` dependency
- Fast execution (<10ms)

#### Method B: Character-Based Estimation (Zero Dependencies)

```python
def count_tokens_estimate(text: str) -> int:
    return len(text) // 4
```

**Characteristics**:
- ~80-90% accuracy for English text
- No dependencies at all
- Sub-millisecond latency
- Less accurate for code and non-English text

**Trade-off Matrix**:

| Factor | tiktoken | Estimation |
|--------|----------|------------|
| Accuracy | ~90-95% | ~80-90% |
| Speed | <10ms | <1ms |
| Dependencies | tiktoken | None |
| Offline | Yes | Yes |

**Note**: Anthropic hasn't released their official tokenizer publicly. The `tiktoken` approach uses OpenAI's tokenizer with `p50k_base` encoding as a reasonable approximation since both use BPE (byte-pair encoding).

## Token Delta Calculation Flow

```
UserPromptSubmit                    Stop
     |                               |
     v                               v
Read transcript               Read transcript
     |                               |
     v                               v
Count characters             Count characters
     |                               |
     v                               v
Estimate tokens (T1)         Estimate tokens (T2)
     |                               |
     v                               v
Save T1 to temp file         Calculate delta = T2 - T1
                                     |
                                     v
                             Report: "Request used ~X tokens"
```

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| Temp file not found (hook failures) | Graceful fallback to cumulative-only reporting |
| Inaccurate token estimates | Clear documentation of limitations |
| Race conditions (concurrent sessions) | Session ID in filename for isolation |
| Temp file cleanup | Use system temp directory (auto-cleaned) |

## Example Output Format

```
Context Usage: ~12,500 tokens used (~125,000 remaining)
This request: ~850 tokens (+6.8% of total)
```

## Open Questions

None - design is straightforward given existing hook capabilities.

# subagents-lesson Specification

## Purpose
TBD - created by archiving change update-subagents-lesson. Update Purpose after archive.
## Requirements
### Requirement: Example Subagent - Debugger

The lesson MUST include a debugger subagent example.

#### Scenario: User needs debugging specialist
- **Given**: A user wants a debugging-focused subagent
- **When**: They view the examples
- **Then**: They find a complete debugger.md example with root cause analysis approach

### Requirement: Example Subagent - Data Scientist

The lesson MUST include a data scientist subagent example.

#### Scenario: User needs data analysis specialist
- **Given**: A user wants a data analysis subagent
- **When**: They view the examples
- **Then**: They find a complete data-scientist.md example with SQL/BigQuery focus

### Requirement: File Location Documentation

The lesson MUST document where subagent files can be stored.

#### Scenario: User learns storage locations
- **Given**: A user wants to know where to put subagent files
- **When**: They read the file locations section
- **Then**: They learn about project (.claude/agents/), user (~/.claude/agents/), plugin, and CLI locations with priority order

### Requirement: Proactive Invocation Guidance

The lesson MUST explain how to encourage automatic subagent use.

#### Scenario: User wants subagent used automatically
- **Given**: A user wants Claude to proactively use their subagent
- **When**: They read the usage section
- **Then**: They learn to include "use PROACTIVELY" or "MUST BE USED" in the description field

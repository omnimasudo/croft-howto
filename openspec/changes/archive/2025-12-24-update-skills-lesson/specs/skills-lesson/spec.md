## ADDED Requirements

### Requirement: Managing Skills Documentation
The skills lesson SHALL provide comprehensive guidance for managing skills including viewing available skills, testing skills, updating skills with restart requirements, and removing skills.

#### Scenario: User wants to view available skills
- **WHEN** a user wants to see what skills are available
- **THEN** the documentation provides both CLI method (asking Claude "What Skills are available?") and filesystem method (ls ~/.claude/skills/ and ls .claude/skills/)

#### Scenario: User wants to test a skill
- **WHEN** a user wants to test if their skill works
- **THEN** the documentation explains that skills activate automatically based on matching descriptions, with example test queries

#### Scenario: User wants to update a skill
- **WHEN** a user modifies a SKILL.md file
- **THEN** the documentation explains that changes take effect on next Claude Code startup and restart is required if already running

#### Scenario: User wants to remove a skill
- **WHEN** a user wants to remove a skill
- **THEN** the documentation provides rm -rf commands for both personal and project skills, with git commit for project skills

### Requirement: Enhanced Debugging Guidance
The skills lesson SHALL provide detailed debugging guidance for common skill issues including skipped skills, YAML errors, script permissions, and path formats.

#### Scenario: Skill not being discovered
- **WHEN** Claude doesn't use a user's skill
- **THEN** the documentation explains to check: description specificity, YAML syntax validity (opening/closing ---, no tabs), and correct file path location

#### Scenario: Skill has errors
- **WHEN** a skill has runtime errors
- **THEN** the documentation explains to check: dependency installation, script execute permissions (chmod +x), and forward slash usage in paths

#### Scenario: Multiple skills conflict
- **WHEN** multiple skills are activated unexpectedly
- **THEN** the documentation explains using distinct trigger terms in descriptions to help Claude choose the right skill

### Requirement: Version History Documentation
The skills lesson SHALL include a best practice example for documenting skill version history in SKILL.md files.

#### Scenario: User wants to track skill versions
- **WHEN** a user maintains a skill over time
- **THEN** the documentation provides a version history markdown template with date and description format

### Requirement: Enhanced Tool Access Control Documentation
The skills lesson SHALL provide expanded documentation for the allowed-tools feature including use cases, security examples, and behavior when not specified.

#### Scenario: User wants a read-only skill
- **WHEN** a user wants to create a skill that cannot modify files
- **THEN** the documentation provides an example with allowed-tools: Read, Grep, Glob

#### Scenario: User wants security-sensitive workflow
- **WHEN** a user has a security-sensitive skill
- **THEN** the documentation explains how allowed-tools restricts Claude's capabilities within that skill context

#### Scenario: allowed-tools not specified
- **WHEN** a user doesn't specify allowed-tools
- **THEN** the documentation explains that Claude will ask for permission as normal

### Requirement: Multi-File Skill Example
The skills lesson SHALL include a comprehensive example of a multi-file skill showing directory structure with multiple reference files, scripts, and templates.

#### Scenario: User wants to create complex skill
- **WHEN** a user needs a skill with supporting files
- **THEN** the documentation provides a complete directory structure example showing SKILL.md, reference files (FORMS.md, REFERENCE.md), scripts subdirectory, and progressive disclosure explanation

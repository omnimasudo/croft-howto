## 1. Update Memory Hierarchy Section
- [ ] 1.1 Update the memory hierarchy table to include 5 levels (Enterprise, Project, Project Rules, User, Project Local)
- [ ] 1.2 Update the mermaid diagram to show the complete hierarchy
- [ ] 1.3 Fix Windows Enterprise Policy path from `C:\ProgramData\ClaudeCode\CLAUDE.md` to `C:\Program Files\ClaudeCode\CLAUDE.md`
- [ ] 1.4 Add explanation of precedence and loading order

## 2. Add Modular Rules Section
- [ ] 2.1 Create new section "Modular Rules with `.claude/rules/`"
- [ ] 2.2 Add directory structure example showing `.claude/rules/` organization
- [ ] 2.3 Explain benefits of topic-specific rule files
- [ ] 2.4 Add examples of modular rule filenames (code-style.md, testing.md, security.md)

## 3. Add Path-Specific Rules Section
- [ ] 3.1 Create new section "Path-Specific Rules with Glob Patterns"
- [ ] 3.2 Explain YAML frontmatter with `paths:` directive
- [ ] 3.3 Add table of glob pattern examples (`**/*.ts`, `src/**/*`, etc.)
- [ ] 3.4 Include practical example of path-scoped API rules

## 4. Add Project Local Memory Section
- [ ] 4.1 Add explanation of `CLAUDE.local.md` file
- [ ] 4.2 Explain auto-gitignore behavior
- [ ] 4.3 Add use case examples (personal preferences on shared projects)

## 5. Add Symlink Support Section
- [ ] 5.1 Add section on sharing rules across projects using symlinks
- [ ] 5.2 Include bash examples for creating symlinks to shared rules

## 6. Update Memory Lookup Algorithm
- [ ] 6.1 Add detailed explanation of recursive upward search
- [ ] 6.2 Explain subtree discovery behavior
- [ ] 6.3 Add example of which files are loaded from different directories

## 7. Update Best Practices
- [ ] 7.1 Add best practices for `.claude/rules/` organization
- [ ] 7.2 Add guidelines for using path-specific rules sparingly
- [ ] 7.3 Add tips for symlink-based rule sharing

## 8. Update Directory Structure Example
- [ ] 8.1 Update the directory structure to show `.claude/rules/` hierarchy
- [ ] 8.2 Include subdirectory examples (frontend/, backend/)

## 9. Review and Polish
- [ ] 9.1 Ensure all mermaid diagrams are updated
- [ ] 9.2 Review table formatting consistency
- [ ] 9.3 Update "Official Documentation" links if needed
- [ ] 9.4 Verify all code examples are accurate

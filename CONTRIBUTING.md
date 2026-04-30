# Contributing to OSCP PEN-200 Preparation System

Thank you for your interest in improving this OSCP preparation system! This document provides guidelines for contributing.

## 🎯 How You Can Contribute

### 1. **Report Broken Links or Errors**
- Found a dead link in the notes?
- Discovered a command that doesn't work?
- Open an issue with:
  - Which file/note has the problem
  - What's broken
  - Suggested fix (if you have one)

### 2. **Submit New Techniques or Vectors**
- Discovered a new exploitation technique?
- Found a better privilege escalation method?
- Create a pull request with:
  - Detailed explanation
  - Working example/command
  - Links to reference material
  - Tested environment (Linux distro, Windows version, etc.)

### 3. **Improve Existing Notes**
- Reorganize content for clarity
- Add missing examples
- Improve formatting
- Fix typos

### 4. **Add New Practice Machines**
- Know of a great OSCP-like machine?
- Update `OSCP-Machine-List.md` with:
  - Machine name and platform (HTB, TryHackMe, etc.)
  - Difficulty level
  - Primary vulnerabilities
  - Why it's OSCP-relevant

### 5. **Community Feedback Integration**
- Have insights from your exam experience?
- Found success patterns or common mistakes not covered?
- Submit as issue or discussion with:
  - What worked for you
  - What didn't work
  - Recommendations for the system

## 📋 Contribution Process

### For Bug Fixes or Small Improvements
1. Fork the repository
2. Create a feature branch: `git checkout -b fix/issue-description`
3. Make your changes
4. Commit with clear message: `git commit -m "fix: Brief description"`
5. Push to your fork
6. Create Pull Request with description of changes

### For New Content (Notes, Scenarios)
1. Follow the existing note format
2. Include [[wikilinks]] to related notes
3. Use Mermaid diagrams for complex flows
4. Add copy-paste ready code blocks
5. Include references/sources
6. Test any commands you include

### For Large Changes or New Features
1. Open an issue first to discuss the idea
2. Get feedback before starting work
3. Follow the same PR process above

## 🏗️ Note Format Guidelines

All Obsidian notes should follow this structure:

```markdown
---
tags: [oscp, topic-tags]
aliases: [Alternative Names]
category: Category-Name
difficulty: ★★☆☆☆
last-updated: 2026-04-30
---

# 📌 Note Title

> [!info] Context Box
> Brief explanation of what this note covers

---

## 🎯 Main Section

Content with:
- Clear headings
- Code blocks with syntax highlighting
- [[wikilinks]] to related notes
- Practical examples

---

## 📚 References
- [Link](url)
- [[Related-Note]]
```

## ✅ Quality Checklist Before Submitting

- [ ] All links are tested and working
- [ ] All commands have been tested in a lab environment
- [ ] Notes follow existing formatting style
- [ ] [[wikilinks]] added to related notes
- [ ] Code blocks include syntax highlighting
- [ ] No sensitive information (API keys, passwords)
- [ ] Spelling and grammar checked
- [ ] Follows the 50% enumeration rule emphasis where relevant
- [ ] Includes references/sources

## 🚫 What We Don't Accept

- Malware, exploits for unauthorized access
- Instructions for illegal activities
- Plagiarized content without attribution
- Unverified techniques (must work in lab)
- Spam or off-topic content

## 💬 Discussion & Ideas

Have ideas but not ready to contribute code?
- Open a GitHub Discussion
- Propose the idea
- Get community feedback
- Iterate together

## 📊 Code Review Process

Pull requests will be reviewed for:
1. **Accuracy** - Do the commands/techniques actually work?
2. **Relevance** - Does it help OSCP exam preparation?
3. **Quality** - Clear, well-formatted, complete?
4. **Alignment** - Matches existing system structure?

Reviewers may ask for changes. Please respond to feedback constructively.

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md (if PR accepted)
- Credited in commit messages
- Recognized for significant contributions

## 📝 Commit Message Guidelines

Use conventional commits format:
```
type(scope): description

[optional body]
```

Types:
- `feat:` New note, feature, or technique
- `fix:` Bug fix, broken command, dead link
- `docs:` Documentation improvements
- `refactor:` Reorganize content
- `test:` Test additions (lab verification)
- `chore:` Maintenance, tool updates

Examples:
```
feat(linux-privesc): Add AppArmor bypass technique
fix(sql-injection): Update sqlmap syntax for mysql 8.0
docs(exam-strategy): Clarify report template sections
```

## 🤝 Code of Conduct

- Be respectful and constructive
- Assume good intent
- Help each other learn
- No harassment or discrimination
- Remember: This is an educational community

## 📞 Questions?

- Open an issue with label `question`
- Check existing issues/discussions first
- Be specific about what you need help with

---

**Thank you for helping improve OSCP preparation for the community!** 🎓

Last updated: April 30, 2026

---
tags: [oscp, dashboard, moc]
aliases: [OSCP Study Dashboard, Main Hub]
category: Dashboard
status: active
last-updated: 2025-04-30
---

# 📊 OSCP PEN-200 Study Dashboard

> [!info] Welcome to Your Exam Prep Hub
> This is your **Map of Content (MOC)** for the complete OSCP PEN-200 certification journey. Use this as your north star for systematic study and exam preparation.

---

## 🎯 Exam Overview

| Aspect | Details |
|--------|---------|
| **Exam Name** | Offensive Security Certified Professional (OSCP) |
| **Course** | PEN-200 (Penetration Testing with Kali Linux) |
| **Duration** | 23 hours 45 minutes |
| **Machines** | 3 independent + 1 network compromise |
| **Pass Score** | 70+ points (100 total) |
| **Study Time** | 40-60 weeks (PWK course is 90 days) |

> [!warning] Exam Reality Check
> The exam is **extremely challenging**. You'll face 3 independent machines (25 pts each) + 1 multi-machine network (25 pts). No hints, no hints flag, partial credit only on proof.txt/local.txt.

---

## 📚 Study Modules (Click to Navigate)

### Foundation & Methodology
- [[01-Methodology/Professional-Pentest-Kill-Chain|⚔️ Professional Pentest Kill Chain]] — Complete cyber kill chain with Mermaid diagrams (START HERE!)
- [[01-Methodology/Pentest-Methodology|🗺️ Pentest Methodology]] — Complete attack chain with flowcharts
- [[01-Methodology/Recon-and-Enumeration|🔍 Recon & Enumeration]] — Information gathering playbook
- [[01-Methodology/Port-Service-Checklist|🔌 Port Service Checklist]] — Service-by-service exploitation guide

### Linux (40% of exam weight)
- [[02-Linux/Linux-Privesc|🐧 Linux Privilege Escalation]] — All major privilege escalation vectors
- [[02-Linux/Shells-and-Payloads|💀 Shells & Payloads]] — Reverse shells in every language
- [[02-Linux/File-Transfer-Linux|📁 File Transfer (Linux)]] — Data exfiltration techniques

### Windows (40% of exam weight)
- [[03-Windows/Windows-Privesc|🪟 Windows Privilege Escalation]] — Token abuse, services, exploits
- [[03-Windows/Active-Directory|👑 Active Directory Attacks]] — Domain exploitation chain
- [[03-Windows/File-Transfer-Windows|📁 File Transfer (Windows)]] — Lateral movement and exfil

### Web Applications (15% of exam weight)
- [[04-Web/Web-Vulnerabilities|🌐 Web Vulnerabilities]] — OWASP top 10 + OSCP specifics
- [[04-Web/SQL-Injection|💉 SQL Injection]] — Manual exploitation + sqlmap automation
- [[04-Web/LFI-RFI-to-RCE|🔗 LFI/RFI to RCE]] — Chaining file inclusion to code execution
- [[04-Web/File-Upload-Bypass|📤 File Upload Bypass]] — Image magic, MIME, double extension
- [[04-Web/Command-Injection|⚙️ Command Injection]] — OS command execution techniques

### Tools & Utilities (5% of exam weight)
- [[05-Tools/Nmap-Cheatsheet|🎯 Nmap Cheatsheet]] — Network scanning bible
- [[05-Tools/MSFvenom-Payloads|💣 MSFvenom Payloads]] — Meterpreter + shell payload generation
- [[05-Tools/Reverse-Shells|🐚 Reverse Shells]] — Bash, Python, PHP, PowerShell, C# payloads
- [[05-Tools/Pivoting-Tunneling|🌉 Pivoting & Tunneling]] — Chisel, Ligolo-ng, SSH tunnels
- [[05-Tools/Wordlists-Reference|📋 Wordlists Reference]] — SecLists paths & custom wordlist generation

### Advanced Topics
- [[06-Buffer-Overflow/BOF-x86-Windows|💥 Buffer Overflow (x86 Windows)]] — Step-by-step BOF methodology

### Resources & Practice
- [[07-Resources/OSCP-Machine-List|🎮 OSCP Machine List]] — Curated practice machines by category
- [[07-Resources/Useful-Links|🔗 Useful Links]] — Tools, exploits, communities

### Latest Research (Community Validated)
- [[13-Latest-Research/GitHub-Research-Findings|🔍 GitHub Research]] — Latest repos, CVEs, trending techniques (April 2026)
- [[13-Latest-Research/Reddit-Research-Findings|💬 Reddit Community Feedback]] — Real student experiences, success patterns, failure analysis (April 2026)

---

## 📈 Study Progress Tracker

### Methodology Foundation
- [ ] Read complete pentest methodology
- [ ] Understand recon phases
- [ ] Create personal port scanning template

### Linux Privilege Escalation
- [ ] Study SUID/GTFOBins exploitation
- [ ] Practice sudo misconfigurations
- [ ] Complete 5 Linux privesc machines

### Windows Privilege Escalation  
- [ ] Learn Windows token model
- [ ] Practice SeImpersonate abuse
- [ ] Complete 5 Windows privesc machines

### Web Vulnerabilities
- [ ] Master SQL injection (manual + sqlmap)
- [ ] Learn LFI to RCE chains
- [ ] Practice file upload bypasses

### Active Directory
- [ ] Study Kerberos fundamentals
- [ ] Practice Kerberoasting / AS-REP
- [ ] Complete AD domain compromise

### Buffer Overflow
- [ ] Understand x86 assembly basics
- [ ] Complete 3 BOF exercises
- [ ] Create mona.py script templates

### Full Machine Exploitation
- [ ] Complete 10 OSCP-like machines
- [ ] Practice report writing (proof.txt)
- [ ] Time yourself (< 4 hours per machine)

---

## 🎓 Time Management Strategy

```
Phase 1: Foundation (Weeks 1-4)
├─ Understand OSCP exam format
├─ Master reconnaissance methodology
└─ Set up lab environment (Kali + VPN)

Phase 2: Linux Mastery (Weeks 5-12)
├─ Deep dive: Linux privilege escalation
├─ Complete 10+ Linux-focused machines
└─ Build your personal cheatsheet

Phase 3: Windows & AD (Weeks 13-20)
├─ Windows priv escalation techniques
├─ Active Directory attack chains
└─ Practice domain-based scenarios

Phase 4: Web & Advanced (Weeks 21-28)
├─ Web application vulnerabilities
├─ Buffer overflow practice
└─ Integrate all attack vectors

Phase 5: Full Integration (Weeks 29-36)
├─ Complete full-network machines
├─ Timed practice exams (4 hours/machine)
├─ Report writing perfection
└─ Sleep & recovery week

Phase 6: Final Polish (Weeks 37-40)
├─ Review weak areas
├─ Practice high-difficulty machines
├─ Exam day preparation
└─ Ready to sit!
```

---

## 🚀 Pre-Exam Checklist (1 Week Before)

- [ ] Lab environment fully functional
- [ ] All tools installed and tested
- [ ] Reverse shell payloads ready to go
- [ ] Wordlists and SecLists downloaded
- [ ] Report template prepared
- [ ] Proof collection screenshots understood
- [ ] Sleep schedule normalized
- [ ] No changes to tools/environment (lock it down)

---

## 💡 Critical Success Factors

> [!danger] Common Failures
> **Don't rush the recon phase** — 50% of exam time should be enumeration. Speed kills.

> [!tip] Key Mindset
> **"I will enumerate, escalate, then pivot."** Stick to methodology. Trust the process.

> [!info] Exam Day
> - Reboot often
> - Document EVERYTHING (screenshots)
> - No tunnel vision on one machine
> - Take breaks every 2 hours
> - Read error messages carefully

---

## 🔗 Quick Links

### Official Resources
- [OSCP Certification](https://www.offensive-security.com/pwk-oscp/)
- [Exam Rules & Format](https://www.offensive-security.com/pwk-oscp/)
- [Student Workspace](https://www.offensive-security.com/labs)

### Community Resources
- [TryHackMe OSCP Path](https://tryhackme.com/paths/OSCP)
- [HackTheBox OSCP-like machines](https://www.hackthebox.com/)
- [PentesterLab OSCP prep](https://pentesterlab.com/)

### Helpful Communities
- [r/oscp](https://reddit.com/r/oscp) — Community support
- [OSCP Discord Servers](https://discord.com) — Real-time help
- [Offensive Security Forums](https://forums.offensive-security.com)

---

## 📝 Note Types in This Vault

- **🗺️ Methodology** → Complete attack chains and workflows
- **🐧 / 🪟** → OS-specific exploitation techniques
- **🌐** → Web application vulnerabilities
- **💀** → Payload and shell references
- **🎯** → Tool-specific cheatsheets
- **🔗** → Cross-cutting concerns (pivoting, AD)

---

## ⚡ How to Use This Vault

1. **Navigate by module** — Click topics above to dive into each area
2. **Use graph view** — See relationships between concepts (Ctrl/Cmd + Shift + G)
3. **Dataview queries** — Filter notes by tag, difficulty, category
4. **Copy commands** — All code blocks have copy buttons
5. **Track progress** — Check boxes mark your learning journey
6. **Search** — Use Obsidian search (Ctrl/Cmd + F) for quick reference

---

**Last Updated:** 2025-04-30  
**Status:** 🟢 Ready for active study  
**Next Update:** When new exam patterns emerge

---

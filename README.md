# 🎯 OSCP PEN-200 Comprehensive Preparation System

**The Ultimate All-in-One OSCP Study & Reference Platform**

## 🗺️ **INTERACTIVE CYBER KILL CHAINS**

### [>> PROFESSIONAL PENETRATION TESTING KILL CHAIN <<](https://cdn.jsdelivr.net/gh/digitalcomposer/oscp-pen200-prep@main/professional-pentest-kill-chain.html)
**General-purpose framework for real-world penetration testing**
- 7 main phases: Reconnaissance → Lateral Movement
- 30+ attack nodes covering all engagement types
- Multi-vector attacks (web, network, social, cloud)
- Risk ratings and detailed techniques per node
- Professional methodology for legitimate assessments

### [>> OSCP EXAM CYBER KILL CHAIN <<](https://cdn.jsdelivr.net/gh/digitalcomposer/oscp-pen200-prep@main/cyber-kill-chain-interactive.html)
**OSCP PEN-200 specific attack flow optimization**
- 40+ nodes focused on exam machine exploitation
- Timing budgets and phase breakdowns
- Decision trees for preventing common failures
- Command examples with copy-to-clipboard
- 50% enumeration rule enforcement

---

## 📦 What You Get

### ✅ Interactive Cyber Kill Chain Maps (2 Versions)
- **Professional Pentest Version** - 7 phases, 30+ nodes for real-world engagements
- **OSCP Exam Version** - 40+ nodes optimized for certification exam
- **Visual attack flows** with multiple exploitation paths
- **Click for details** - Commands, tools, risk ratings, techniques
- **Works offline** - Download & open in any browser
- **[>>> PROFESSIONAL KILL CHAIN <<<](https://cdn.jsdelivr.net/gh/digitalcomposer/oscp-pen200-prep@main/professional-pentest-kill-chain.html)** | **[>>> OSCP KILL CHAIN <<<](https://cdn.jsdelivr.net/gh/digitalcomposer/oscp-pen200-prep@main/cyber-kill-chain-interactive.html)**

### ✅ Phase 1: Obsidian Vault (Complete!)
- **31 beautifully formatted markdown notes**
- **Cross-linked wiki structure**
- **Mermaid diagrams & flowcharts**
- **Copy-paste ready commands**
- **Offline-ready**: Works completely offline after initial setup

### ✅ Phase 2: Python Research Scrapers
- **GitHub harvester** - Tracks new OSCP repos, CVEs, tools (weekly)
- **Reddit monitor** - Community feedback & success patterns (monthly)
- **Automated updates** - AI agent infrastructure for continuous improvement

---

## 🚀 Quick Start (3 Steps)

### Step 1: Create Obsidian Vault

```bash
cd /path/to/oscpmaster
bash setup.sh
```

This creates `OSCP-PEN200-Vault/` folder structure with all notes.

### Step 2: Open in Obsidian

1. Download [Obsidian](https://obsidian.md/)
2. **Create new vault** → Select `OSCP-PEN200-Vault` folder
3. **Enable plugins:**
   - Dataview
   - Templater
   - Calendar
   - Kanban

---

## 📚 Vault Structure

```
OSCP-PEN200-Vault/
├── 00-Dashboard.md              ← MOC (START HERE)
├── 01-Methodology/
│   ├── Pentest-Methodology.md   ← 7-phase attack chain
│   ├── Recon-and-Enumeration.md ← Service-by-service guide
│   └── Port-Service-Checklist.md ← Port 21-9200 reference
├── 02-Linux/
│   ├── Linux-Privesc.md         ← 8 escalation vectors
│   ├── Shells-and-Payloads.md   ← 40+ shell payloads
│   └── File-Transfer-Linux.md
├── 03-Windows/
│   ├── Windows-Privesc.md       ← Token abuse, DLL hijack
│   ├── Active-Directory.md      ← Kerberoasting, DCSync
│   └── File-Transfer-Windows.md
├── 04-Web/
│   ├── Web-Vulnerabilities.md   ← OWASP Top 10
│   ├── SQL-Injection.md         ← Manual + sqlmap
│   ├── LFI-RFI-to-RCE.md       ← Chaining guide
│   ├── File-Upload-Bypass.md    ← MIME, polyglot, htaccess
│   └── Command-Injection.md
├── 05-Tools/
│   ├── Nmap-Cheatsheet.md
│   ├── MSFvenom-Payloads.md
│   ├── Reverse-Shells.md
│   ├── Pivoting-Tunneling.md    ← Chisel, Ligolo, proxychains
│   └── Wordlists-Reference.md
├── 06-Buffer-Overflow/
│   └── BOF-x86-Windows.md       ← 7-step methodology
├── 07-Resources/
│   ├── OSCP-Machine-List.md     ← HTB/THM/VulnHub curated
│   └── Useful-Links.md          ← Official links + tools
└── .obsidian/                   ← Graph view config
```

---

## 🛠️ Using the Python Scraper

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Scraper

```bash
python3 scraper.py
```

**This automatically:**
- Searches GitHub for latest OSCP repos and CVEs
- Monitors Reddit for community success patterns
- Tracks tool updates (linPEAS, winPEAS, Chisel, etc.)
- Generates markdown findings integrated into vault

---

## 📋 Complete Vault Contents at a Glance

| Module | Notes | Focus |
|--------|-------|-------|
| **Methodology** | 4 | 7-phase attack framework, enumeration strategy |
| **Linux** | 4 | 8 privesc vectors, post-exploitation, shells |
| **Windows** | 3 | Token abuse, AD attacks, service exploitation |
| **Web** | 5 | OWASP Top 10, SQLi, upload bypass, command injection |
| **Tools** | 5 | Nmap, MSFvenom, shells, pivoting, wordlists |
| **Buffer Overflow** | 1 | 7-step x86 Windows BOF methodology |
| **Advanced** | 1 | Advanced exploitation techniques |
| **Exam Strategy** | 4 | Common mistakes, scenarios, checklist, template |
| **Decision Trees** | 1 | Vulnerability prioritization framework |
| **Progress Tracking** | 1 | Self-assessment & weakness analyzer |
| **Mock Exams** | 1 | Full 23h 45m exam simulation |
| **Community Research** | 2 | GitHub findings + Reddit insights |
| **Resources** | 2 | Machine lists, useful links |

**Total: 31 comprehensive, community-validated, exam-ready notes**

---

## 💡 Study Strategy

### Week 1-2: Foundation
- Read: 00-Dashboard, Pentest-Methodology
- Complete: Recon-and-Enumeration, Port-Service-Checklist
- Practice: Linux-Privesc vectors (top 5)

### Week 3-4: Linux Mastery
- Deep dive: Linux-Privesc (all 8 vectors)
- Practice: 5 Linux machines (goal: 4h each)
- Memorize: Shells-and-Payloads

### Week 5-6: Windows & AD
- Study: Windows-Privesc, Active-Directory
- Practice: 5 Windows machines
- Time goal: Get to < 3.5 hours per machine

### Week 7-8: Web Vulnerabilities
- Cover: All Web notes (SQLi through Command Injection)
- Practice: DVWA, Juice Shop, HackTheBox web machines
- Master: LFI to RCE chaining

### Week 9-10: Buffer Overflow
- Study: BOF-x86-Windows (multiple times)
- Complete: 5+ BOF machines
- Goal: Complete BOF in < 2 hours

### Week 11-12: Mixed & Speed
- Timed runs: 4-hour machine challenges
- Speed practice: Try to complete in 3h
- Document: Screenshot everything for report

### Week 13-14: Final Polish
- Review weak areas
- Practice high-difficulty machines
- Sleep schedule normalization

---

## 🎓 Using Obsidian Features

### Graph View
- **Ctrl+Shift+G** → See relationship between concepts
- Identify missing knowledge gaps
- Navigate by clicking nodes

### Search
- **Ctrl+F** → Find commands, CVEs, techniques
- **Ctrl+Shift+F** → Global search across all notes

### Backlinks
- Bottom of each note shows related pages
- Follow chains of related concepts

### Tags
- Filter notes by tag: `#oscp`, `#linux`, `#privesc`
- Dataview plugin creates dynamic queries

---

## 🔒 Offline Usage

**Everything works offline after setup:**

1. ✅ Obsidian vault (all markdown files local)
2. ✅ Python research scrapers (automated updates)
3. ✅ All commands and payloads (hard-coded)
4. ❌ Scraper (requires internet, but runs once)

**Just open the vault folder locally after initial setup!**

---

## 📝 File Structure

```
oscpmaster/
├── setup.sh                     ← Create vault
├── advanced_scraper.py          ← GitHub research harvester
├── reddit_scraper.py            ← Community feedback monitor
├── requirements.txt             ← Python dependencies
├── OSCP-PEN200-Vault/           ← Complete vault (31 markdown notes)
│   ├── 00-Dashboard.md          ← Map of Content (MOC)
│   ├── 01-Methodology/          ← 7-phase attack framework
│   ├── 02-Linux/                ← 8 privilege escalation vectors
│   ├── 03-Windows/              ← Token abuse, AD, services
│   ├── 04-Web/                  ← OWASP Top 10 vulnerabilities
│   ├── 05-Tools/                ← Nmap, MSFvenom, shells, pivoting
│   ├── 06-Buffer-Overflow/      ← x86 Windows BOF methodology
│   ├── 07-Resources/            ← Machine lists, useful links
│   ├── 08-Exam-Strategy/        ← Mistakes prevention, checklist
│   ├── 09-Exam-Day/             ← Hour-by-hour timeline
│   ├── 10-Decision-Trees/       ← Vulnerability prioritization
│   ├── 11-Progress-Tracking/    ← Self-assessment tools
│   ├── 12-Mock-Exams/           ← 23h 45m simulation
│   ├── 13-Latest-Research/      ← GitHub + Reddit findings
│   └── .obsidian/               ← Graph view config
├── README.md                    ← This file
└── AI-AGENT-INFRASTRUCTURE.md   ← Future automation setup
```

---

## 🚨 Important Notes

### Before Exam
- [ ] Test setup in VM
- [ ] Verify all tools work
- [ ] Download wordlists
- [ ] Ensure VPN connection
- [ ] Have backup notes printed/ready

### During Exam
- 📝 Follow methodology religiously
- ⏱️ 50% time on enumeration
- 📸 Screenshot EVERYTHING
- 🎯 Document failed attempts (partial credit!)
- 🌉 Don't tunnel-vision - try all 3 machines first

### After Exam
- 📋 Write report from screenshots
- 🎓 Include complete methodology walkthrough
- ✅ Proof file evidence
- 💯 Aim for 70+ points

---

## 🎯 Success Metrics

**By Week 4:** Linux privesc expertise  
**By Week 8:** Windows & AD confidence  
**By Week 10:** Web vuln mastery + BOF complete  
**By Week 12:** Speed runs < 4 hours/machine  
**By Week 14:** Ready for exam!  

---

## 💬 Getting Help

- **OSCP Forum:** https://forums.offensive-security.com/
- **r/oscp:** https://reddit.com/r/oscp
- **TryHackMe Community:** https://tryhackme.com/discord
- **ippsec Walkthroughs:** https://youtube.com/@ippsec

---

## 🎁 Bonus: Quick Copy-Paste Guide

**For quick access, most-used commands are in dashboard:**

1. Open `index.html`
2. Go to **Payloads tab**
3. Click **Copy** on any payload
4. Paste into exploit

---

## 🏆 You Got This!

> "The worst way to predict the future is to think it will be just like the past." - Peter Drucker

This system is built for **comprehensive coverage** + **quick reference** + **exam timing practice**.

- **Slow is smooth, smooth is fast.** 
- **Trust the methodology.**
- **Document everything.**

**You will root the exam. 💪**

---

**Last Updated:** 2025-04-30  
**Status:** 🟢 Production Ready  
**Version:** 1.0 (OSCP PEN-200)

---

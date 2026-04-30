---
tags: [oscp, exam, checklist, exam-day]
aliases: [Exam Day Guide, Last Minute Prep]
category: Exam-Day
difficulty: ★★★★★
last-updated: 2025-04-30
---

# ✅ OSCP Exam Day Checklist (MUST READ)

> [!danger] CRITICAL
> Follow this checklist EXACTLY. Most failures are preventable mistakes.

---

## 📅 Day Before Exam

### Night Before (NOT Day Of!)
- [ ] **Sleep 8 hours** (DO NOT cram or all-nighter!)
- [ ] Lay out all equipment
- [ ] Test VPN connection at home
- [ ] Verify Kali is fully updated
- [ ] Verify all tools working:
  ```bash
  which nmap gobuster sqlmap msfvenom nc python3
  ```

### Morning of Exam (3 hours before)
- [ ] Eat good breakfast (protein + carbs)
- [ ] Drink water (stay hydrated)
- [ ] Use bathroom (no interruptions!)
- [ ] Close all notifications (Slack, email, phone)
- [ ] Have workspace clean and ready
- [ ] Test internet connection
- [ ] Connect to VPN 30 minutes early

---

## ⏱️ EXAM START (0:00:00)

### First 5 Minutes (Before Touching Anything)

- [ ] Read exam email completely
- [ ] Verify 3 machines and network map
- [ ] Verify your IP address assigned
- [ ] Verify you can connect to first machine
- [ ] Open screenshot tool (ready)
- [ ] Open text editor for notes
- [ ] Verify audio/proctoring working

**DO NOT START ATTACKING YET**

---

## 🎯 MACHINE 1 (First 4.5 hours)

### Strategy
Choose EASIEST machine first (psychological win)

### Reconnaissance (First 10 min)
```bash
# Passive enumeration only
- Review machine info
- Plan attack approach
- Estimate difficulty
```

### Enumeration Phase (Next 45 min MINIMUM)

```bash
# START WITH NMAP
[ ] nmap -sS -p- -sV -T4 --open 10.10.10.X

# DOCUMENT OUTPUT
[ ] Save output: nmap_machine1.txt

# FOR EACH OPEN PORT
[ ] HTTP/HTTPS: nikto, gobuster, whatweb
[ ] SMB: enum4linux, smbclient, smbmap
[ ] SSH: ssh-audit, banner grab
[ ] FTP: anonymous login test
[ ] LDAP: ldapsearch
[ ] Custom ports: searchsploit for version

# CRITICAL CHECKS
[ ] Default credentials tried?
[ ] CVE searched for each version?
[ ] Low-hanging fruit checked? (anonymous shares, null sessions)
```

> [!warning] Enumeration Rule
> If you move to exploitation in < 30 min, YOU WILL FAIL. More time here = less time stuck later.

### Vulnerability Identification (10 min)
```bash
[ ] Easiest vector identified
[ ] Exploit researched (searchsploit)
[ ] Confirmed working in lab
```

### Exploitation Phase (30 min)
```bash
[ ] Initial shell obtained (screenshot)
[ ] Shell type confirmed (bash/cmd)
[ ] Stabilize shell (PTY on Linux)
```

**🎯 ACTION: SCREENSHOT of initial shell**

### Post-Exploitation (10 min)
```bash
Linux:
[ ] whoami
[ ] id
[ ] uname -a
[ ] sudo -l (CHECK FIRST!)

Windows:
[ ] whoami
[ ] whoami /all (privileges critical!)
[ ] systeminfo
```

**IF SUDO/TOKEN PRIVILEGE FOUND: Exploit immediately!**

### Privilege Escalation (60 min)
```bash
[ ] Automated script run (linPEAS or winPEAS)
[ ] Output saved for analysis
[ ] Easy vectors checked first (sudo, SUID, DLL)
[ ] Exploit identified and tested
[ ] ROOT/SYSTEM shell obtained

[ ] SCREENSHOT: proof.txt content
[ ] SCREENSHOT: whoami output
[ ] SCREENSHOT: hostname output
```

**🎯 ACTION: Proof screenshots taken**

### TOTAL: ~1h 50m | Time remaining: 21h 55m

---

## 🎯 MACHINE 2 (Next 4.5 hours, TOTAL: 6h 40m)

**Repeat exact same process as Machine 1**

**Timing:**
- Enumeration: 45 min
- Exploitation: 30 min
- Post-Exploit: 10 min
- Privesc: 60 min
- Total: ~2h 25m
- **Time remaining: 19h 30m**

---

## 🎯 MACHINE 3 (Next 4.5 hours, TOTAL: 11h 10m)

**Repeat exact same process**

**Timing:**
- Enumeration: 45 min
- Exploitation: 30 min
- Post-Exploit: 10 min
- Privesc: 60 min (might be harder)
- Total: ~2h 25m
- **Time remaining: 17h 05m**

---

## 🌐 NETWORK MACHINE (5-8 hours, TOTAL: 16h-19h)

### Strategy
- Multiple machines to compromise
- Likely requires pivoting
- Save for when you have time/energy

### Enumeration (Deep)
```bash
[ ] Map entire network topology
[ ] Identify 4-5 hosts
[ ] Port scan each host
[ ] Document all services
[ ] Identify pivot point (easiest to compromise first)
```

### Pivot Setup
```bash
[ ] Compromise first host (web server typical)
[ ] Setup tunnel (SSH, chisel, ligolo)
[ ] Test pivot to internal network
[ ] Confirm 172.16.0.0/24 network accessible
```

### Internal Exploitation
```bash
[ ] Scan internal servers
[ ] Compromise database server OR file server
[ ] Escalate to admin on internal host
[ ] Enumerate further (domain creds, etc.)
```

### Domain Controller
```bash
[ ] Kerberoasting OR DCSync
[ ] Domain admin credentials obtained
[ ] DC compromised
[ ] PROOF screenshots taken
```

---

## 📊 TOTAL TIME ALLOCATION

```
Machine 1:  1h 50m  (cumulative: 1h 50m)
Machine 2:  2h 25m  (cumulative: 4h 15m)
Machine 3:  2h 25m  (cumulative: 6h 40m)
Breaks:     1h 45m  (cumulative: 8h 25m)
Network:    6-8h    (cumulative: 14-16h)
Margins:    7h 25m  (for contingency, documentation)
─────────────────────
TOTAL:      23h 45m
```

---

## 🚨 RED FLAGS - STOP & REASSESS

| Flag | Action |
|------|--------|
| **Stuck 90+ min on 1 machine** | Switch machines NOW |
| **No screenshot in 45 min** | Take one immediately |
| **Enum < 30 min** | You missed ports/services |
| **Report not started by hour 15** | Start writing NOW |
| **3 machines not compromised by hour 14** | Network machine is bonus |

---

## 📝 DOCUMENTATION RULES

### Screenshots MUST Include
```
For EACH compromise:
[ ] Proof file content (full path visible)
[ ] whoami/whoami /all output
[ ] hostname output
[ ] ipconfig (windows) / ifconfig (linux)
[ ] First successful command after shell
[ ] Privesc moment (root prompt visible)
```

### NO Screenshots needed for
- ❌ Nmap output (save file instead)
- ❌ Gobuster results (save file instead)
- ❌ General enumeration (document in report)

---

## ⏰ TIME MANAGEMENT RULES

- **NEVER** spend > 90 minutes on single machine
- **ALWAYS** enumerate for minimum 45 minutes
- **ALWAYS** document as you go
- **BREAK** every 2-3 hours (15 min minimum)
- **NEVER** skip post-exploitation enum
- **NEVER** attempt machine without thorough enum

---

## 💡 During Exam: Mindset

### ✅ DO
- Trust methodology (enumeration > exploitation)
- Document everything (think about report)
- Take breaks (mental fatigue = mistakes)
- Switch machines if stuck
- Communicate with proctor if issues
- Stay hydrated and fed

### ❌ DON'T
- Rush enumeration ("I found port 80, let's exploit")
- Panic if first exploit doesn't work
- Try every known exploit (test 1-2, move on)
- Use exploits you haven't tested
- Go 4+ hours without break
- All-nighter mindset (sleep is part of strategy)

---

## 📋 Report Writing Timeline

| Time | Action |
|------|--------|
| **Hour 0-6** | Focus 100% on exploitation |
| **Hour 6-8** | Start basic report structure |
| **Hour 8-15** | Continuously add findings |
| **Hour 15-20** | Finish report (all screenshots) |
| **Hour 20-23h45m** | Polish, format, proofread |

**Rule: Report due at 23h 45m mark. Not 1 second late.**

---

## 🎯 PASSING SCORE ANALYSIS

```
Easy wins (3 machines):         75 points minimum
Network machine (if time):      25 points (bonus)
Report quality (if complete):   20 points (bonus)
─────────────────────────────
MINIMUM PASS:                   70 points
```

**To pass, you MUST compromise 3 machines.**

---

## 🚪 Exam Ending (Last Hour)

### With 1 Hour Left
- [ ] Stop exploitation (no new machines)
- [ ] Finalize all screenshots
- [ ] Complete report writing
- [ ] Proofread everything
- [ ] Verify all 3 machines documented

### With 15 Min Left
- [ ] Do final report check
- [ ] Verify submission email address
- [ ] Prepare report for submission

### Last 5 Minutes
- [ ] SUBMIT REPORT (early is better)
- [ ] Confirm receipt email
- [ ] Disconnect from exam

---

## 📊 Success Metrics at Exam End

You should have:
- ✅ 3 machines fully compromised
- ✅ 12+ proof screenshots
- ✅ Complete report with methodology
- ✅ Clear attack chains documented
- ✅ 70+ points (minimum passing)

---

## 🏆 Exam Result Expectations

| Machines | Points | Status |
|----------|--------|--------|
| 1/4 | 25 | ❌ FAIL |
| 2/4 | 50 | ❌ FAIL |
| 3/4 | 75 | ✅ PASS |
| 3/4 + report | 95 | ✅ PASS (excellent) |
| 4/4 | 100 | ✅ PASS (perfect) |

**To pass: 3 machines minimum**

---

## 🎓 Post-Exam

- [ ] Don't discuss exam details (NDA)
- [ ] Results arrive in 4 weeks
- [ ] Wait for official certificate
- [ ] Celebrate your achievement! 🎉

---

**Related Notes:**
- [[08-Exam-Strategy/Common-OSCP-Mistakes|❌ Common Mistakes]]
- [[08-Exam-Strategy/Exam-Report-Template|📋 Report Template]]

---

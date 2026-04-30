---
tags: [oscp, exam, mistakes, anti-patterns]
aliases: [Why Students Fail, OSCP Failures]
category: Exam-Strategy
difficulty: ★★★★★
last-updated: 2025-04-30
---

# ❌ Common OSCP Exam Mistakes (Why 70% Fail)

> [!danger] CRITICAL
> Most failures are NOT due to technical inability. They're preventable mistakes.

---

## 🎯 The Top 5 Exam Killers

### 1. ❌ **ENUMERATION TOO FAST** (40% of failures)

**What Happens:**
```
Student: "I found port 80, let me exploit it immediately"
Reality: Missed 5 other open ports that are easier to exploit
Result: 3 hours wasted on hard path when easy path existed
```

**The Fix:**
- [ ] Run `nmap -sS -p- -sV -T4 --open` (ALL ports)
- [ ] Run `nmap -sU -p 53,123,161,389` (UDP too!)
- [ ] For EACH port, run service-specific enum
- [ ] Document EVERYTHING
- [ ] **Wait at least 45 minutes before exploiting**

> [!warning] Red Flag
> If you've started exploitation in < 30 minutes, STOP. You've missed something.

---

### 2. ❌ **NO SCREENSHOTS TAKEN** (30% fail this)

**Exam Reality:**
```
You: "I got root! I can see the proof.txt file"
Proctor: "Where's your screenshot?"
You: [Has none]
Result: ZERO POINTS even though you rooted it
```

**The Fix:**
```bash
MANDATORY SCREENSHOTS:
✅ proof.txt content (full path visible)
✅ whoami output (proving you're root/SYSTEM)
✅ hostname command output
✅ date/time proof
✅ First successful command after initial shell
✅ Each privilege escalation step
```

**Screenshot Strategy:**
- [ ] Take screenshot IMMEDIATELY after success
- [ ] Use keyboard shortcut: `PrintScreen`
- [ ] Save with timestamp: `Machine_RootShell_2025-04-30_14-32.png`
- [ ] Don't screenshot, continue... screenshot BEFORE pivoting

> [!danger] Exam Day Rule
> Screenshot = Proof. No screenshot = No points.

---

### 3. ❌ **TUNNEL VISION ON ONE MACHINE** (25% fail)

**What Happens:**
```
Student stuck on Machine 1 for 8 hours
Reality: Wasted all time. Should have moved to Machine 2
Exam ends: 0/75 points (only got 1st machine partially)
```

**The Fix:**
```
TIME BUDGET PER MACHINE:
Machine 1 (Easy):  4.5 hours max
Machine 2 (Medium): 4.5 hours max
Machine 3 (Hard):  4.5 hours max
Network Machine:   6-8 hours

IF STUCK > 90 MINUTES ON ONE MACHINE:
→ Move to next machine immediately
→ Try different machine (fresh mindset)
→ Return to stuck machine with new perspective
```

**Decision Tree:**
```
On same machine 90+ min?
├─ Tried all 5 enumeration vectors? YES → Switch machines
├─ Tried all 5 enumeration vectors? NO → Enumerate more
└─ No progress visible? → Document & switch
```

> [!warning] The 90-Minute Rule
> Stuck = stuck. Switch. Momentum > Persistence.

---

### 4. ❌ **MISSING POST-EXPLOITATION ENUMERATION** (35% fail)

**What Happens:**
```
Student: "I got a user shell, let me try privilege escalation immediately"
Reality: Missed 3 easy vectors because no enumeration
Result: Can't escalate, gives up (had privesc nearby but didn't look)
```

**Post-Exploitation MUST-DO:**
```bash
NEVER skip this:

1. Stabilize Shell
   python -c 'import pty; pty.spawn("/bin/bash")'
   export TERM=xterm

2. System Reconnaissance
   uname -a
   cat /etc/os-release
   whoami
   id
   hostname

3. Sudo Check (FIRST!)
   sudo -l              ← If anything shows, exploit immediately

4. SUID Binaries
   find / -perm -4000 2>/dev/null

5. Cron Jobs (CRITICAL!)
   crontab -l
   cat /etc/cron.d/*
   cat /etc/crontab

6. Running Processes (pspy)
   ./pspy64 -p -f -i 1000

7. Automated Scripts
   ./linPEAS.sh
   ./LinEnum.sh
```

**If you skip this, you WILL miss the privesc path.**

> [!danger] Exam Killer
> 80% of machines are rooted by proper post-exploit enum. Don't skip it.

---

### 5. ❌ **NO DOCUMENTATION / WEAK REPORTS** (20% fail)

**Exam Reality:**
```
You: "I compromised all 3 machines, I'll get full points"
Proctor: [Reviews weak report with no methodology]
Result: 50 points instead of 100 (report = 20 points!)
```

**Report Killer Mistakes:**
- ❌ No screenshots
- ❌ No clear attack chain
- ❌ No methodology explanation
- ❌ Poor formatting/spelling
- ❌ Missing proof files
- ❌ No command explanations

**Report Must-Have:**
```
For EACH Machine:

1. Initial Enumeration
   - Nmap output (with explanation)
   - Services found
   - Versions detected

2. Vulnerability Identification
   - CVE found
   - Exploit used
   - Why this vector chosen

3. Exploitation
   - Commands run
   - Screenshots of success
   - Clear step-by-step

4. Post-Exploitation & Privesc
   - Enumeration scripts run
   - Vectors tested
   - Privesc method used
   - Screenshots of root access

5. Proof Files
   - /root/proof.txt content
   - /root/local.txt content
   - whoami output
   - hostname output
```

---

## 🚨 Critical "Red Flags" - STOP & FIX IMMEDIATELY

| Red Flag | What It Means | Fix |
|----------|---|---|
| **No screenshot in 45 min** | Forgetting exam requirement | Screenshot NOW |
| **Enum phase < 30 min** | Too fast, missing ports | Re-enumerate thoroughly |
| **Stuck 90+ min same machine** | Wrong vector or misconfiguration | Switch machines |
| **No sudo -l output** | Didn't check for easy wins | Run it immediately |
| **linPEAS not run** | Missing 80% of vulns | Run automated tools first |
| **Can't explain attack chain** | Don't understand what you're doing | Back up, understand first |
| **Report empty** | Exam ending soon, no documentation | Write basic report NOW |

---

## 📋 Pre-Exploitation Checklist (What to Check FIRST)

```
BEFORE attempting any exploit, verify:

Linux Machines:
☐ All TCP ports scanned (-sS -p-)
☐ UDP ports scanned (53, 123, 389)
☐ Service versions identified (-sV)
☐ Web directories enumerated (gobuster)
☐ SMB shares enumerated (if 445 open)
☐ LDAP enumerated (if 389 open)
☐ FTP anonymous access tested (if 21 open)
☐ SSH version checked for exploits
☐ Kernel version for known exploits
☐ Default credentials tried (FIRST!)

Windows Machines:
☐ All TCP ports scanned
☐ SMB enumeration (enum4linux, smbmap)
☐ RDP version check
☐ Web enumeration (if 80/443 open)
☐ LDAP domain info (if 389 open)
☐ Default credentials (tomcat, admin, etc.)
☐ Kerberos check (if DC)
```

> [!warning] Pre-Exploit Rule
> If you haven't thoroughly enumerated, you will waste hours.

---

## ⏱️ Time Management Mistakes

### ❌ WRONG Approach
```
Machine 1: 12 hours (tunnel vision)
Machine 2: 5 hours (rushed)
Machine 3: 3 hours (didn't try)
Network: 3h 45m (no time left)
= 0 machines rooted (FAIL)
```

### ✅ CORRECT Approach
```
Machine 1: 4h (easy, should be quick)
Machine 2: 4h (medium, standard)
Machine 3: 4h (hard, might get partial)
Network: 6h (complex, multiple hosts)
Break: 1h 45m (rest, food, clear head)
= 3-4 machines rooted (PASS: 75-100 pts)
```

---

## 🎯 Machine-Specific Anti-Patterns

### Linux Machines
- ❌ Not running linPEAS first
- ❌ Not checking sudo -l immediately
- ❌ Not looking for SUID binaries
- ❌ Kernel exploit as first attempt (last resort!)

### Windows Machines
- ❌ Not checking privileges (whoami /all)
- ❌ Not looking for unquoted service paths
- ❌ Kernel exploit first (try token impersonation!)
- ❌ Not looking for writable service executables

### Web Applications
- ❌ Not testing for SQLi in LOGIN first
- ❌ Skipping LFI/RFI in file parameters
- ❌ Not trying file upload bypass
- ❌ Missing command injection in ping/tracert functions

### Active Directory
- ❌ Not enumerating domain users first
- ❌ Not trying Kerberoasting immediately
- ❌ Missing user descriptions (passwords in text!)
- ❌ Not checking for AS-REP roastable users

---

## 📊 Success Metrics (What Top 30% Do Right)

✅ **Enumeration:** 50% of time (minimum)
✅ **Screenshots:** After EVERY major success
✅ **Post-Exploit:** Never skipped (automated scripts first)
✅ **Machine Switching:** If stuck > 90 min
✅ **Documentation:** Constant (helps with report)
✅ **Time Management:** Strict per-machine budgets
✅ **Sleep:** Last night before exam (NOT night-before cramming)

---

## 💡 Exam Day Mindset

> [!info] The Winning Formula
> **Slow enumeration + Smart exploitation + Good documentation = PASS**

**Not:**
- Speed (fast = tunnel vision)
- Flashy exploits (standard RCE > exotic)
- Perfection (partial points = pass)

---

**Related Notes:**
- [[01-Methodology/Pentest-Methodology|🗺️ Pentest Methodology]]
- [[09-Exam-Day/Exam-Day-Checklist|✅ Exam Day Checklist]]

---

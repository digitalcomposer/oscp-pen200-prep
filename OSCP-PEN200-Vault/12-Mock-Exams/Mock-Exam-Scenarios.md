---
tags: [oscp, mock-exam, simulation, practice]
aliases: [Practice Exam, Simulated Exam]
category: Mock-Exams
difficulty: ★★★★★
last-updated: 2025-04-30
---

# 🎮 Complete Mock Exam Scenario (Full 23h 45m Simulation)

> [!danger] MUST COMPLETE
> Do at least ONE full mock exam before real exam.

---

## 📋 Mock Exam Brief

```
OSCP Mock Exam - Complete Scenario

Exam Start: 2025-05-07 10:00 UTC
Exam End:   2025-05-08 09:45 UTC
Duration:   23 hours 45 minutes

Machines:
1. MACHINE-1 (Easy, Linux web app)
2. MACHINE-2 (Medium, Windows privesc)
3. MACHINE-3 (Hard, Linux kernel/AD)
4. NETWORK (Complex, 4-host chain)

Scoring:
- Machine 1: 25 points
- Machine 2: 25 points
- Machine 3: 25 points
- Network:   25 points
- TOTAL:     100 points
- PASSING:   70 points (≥ 3 machines)
```

---

## 🎯 MACHINE 1: "WebVuln" (Easy - Linux)

### Target Information
```
IP: 10.10.10.101
Hostname: webvuln
Expected Time: 1h 45m
Difficulty: Easy
Primary Vector: Web RCE
```

### Discovery Phase (What You Should Find)

**Nmap Scan:**
```
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.4
80/tcp  open  http    Apache 2.4.6
443/tcp open  https   Apache 2.4.6 (SSL)
3306/tcp open mysql   MySQL 5.7.20
```

**Web Application:** Simple blog CMS (WordPress 4.9.8)

**Known Vulnerable Plugin:** "Social Sharing" plugin (unpatched)

### Exploitation Path
1. Identify WordPress 4.9.8
2. Find vulnerable plugin (Social Sharing v1.0)
3. Exploit plugin RCE
4. Get www-data shell
5. Run linPEAS
6. Find sudo -l: `(ALL) NOPASSWD: /usr/bin/python`
7. Exploit with: `sudo python -c 'import os; os.system("/bin/bash")'`
8. Root shell → capture proof.txt

### Proof Requirements
```
proof.txt content: 47919821fc4f2b67ad3fa52f0a7c2eef
whoami output: root
hostname output: webvuln
```

---

## 🎯 MACHINE 2: "WinPriv" (Medium - Windows)

### Target Information
```
IP: 10.10.10.102
Hostname: WINPRIV
Expected Time: 2h 20m
Difficulty: Medium
Primary Vector: Service misconfiguration → token abuse
```

### Discovery Phase

**Nmap Scan:**
```
PORT      STATE SERVICE
22/tcp    open  ssh
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server (RDP)
8080/tcp  open  http
```

**Initial Access:** (Assumed via web vulnerabilityon port 8080)  
Weak credentials: `iis_user:Password123`

### Exploitation Path
1. RDP login as iis_user
2. Run `whoami /all`
3. Find: `SeImpersonate` privilege enabled
4. Download JuicyPotato
5. Execute: `JuicyPotato.exe -t *` 
6. Get SYSTEM shell
7. Capture proof.txt

### Proof Requirements
```
proof.txt content: c49d1f3e2d7a8b5e9f2c4a7b1d3e5f8a
whoami output: nt authority\system
hostname output: WINPRIV
```

---

## 🎯 MACHINE 3: "HardTarget" (Hard - Linux)

### Target Information
```
IP: 10.10.10.103
Hostname: hardtarget
Expected Time: 3h 40m
Difficulty: Hard
Primary Vector: Custom application + kernel
```

### Discovery Phase

**Services Found:**
```
22/tcp open ssh
80/tcp open http (custom Python app)
9999/tcp open unknown (binary app)
```

**Web App:** Custom Python application with file read vuln  
**Binary App:** Custom service with buffer overflow

### Attack Chain (Choose One)

**Option 1: Web Exploit (Faster)**
1. Find file read vulnerability
2. Read /etc/passwd
3. Extract password hashes
4. Crack one user password
5. SSH login
6. Run linPEAS
7. Find binary SUID vulnerability
8. Exploit → root

**Option 2: BOF (More Complex)**
1. Fuzz 9999 port service
2. Identify buffer overflow
3. Find ROP gadgets
4. Build exploit
5. Execute → get shell
6. Continue with privesc

### Proof Requirements
```
proof.txt content: 2e9c5d1f8a3b7e4c6a1f9d3e2c5b7a4f
whoami output: root
hostname output: hardtarget
```

---

## 🌐 NETWORK MACHINE: "DomainComplex"

### Topology
```
Internet Facing: 10.10.10.150 (Apache web server)
    ↓ Internal Access
Internal Network: 192.168.100.0/24
    ├─ 192.168.100.10 (Database MySQL)
    ├─ 192.168.100.20 (File Server Samba)
    └─ 192.168.100.1 (Domain Controller)
```

### Host 1: 10.10.10.150 (Web Server - Entry Point)

**Vulnerability:** LFI in file parameter  
**Time to Compromise:** 1h 30m

```
1. Enumerate web app
2. Find LFI in ?file= parameter
3. Read /etc/passwd
4. Find SSH keys in /home/user/.ssh/id_rsa
5. SSH login as user
6. User has sudo /usr/bin/wget
7. Setup SSH tunnel to internal network
```

### Host 2: 192.168.100.10 (MySQL Server)

**Vulnerability:** Weak root password  
**Time to Compromise:** 45m (from host 1 via tunnel)

```
1. Port forward 3306 through SSH tunnel
2. Connect: mysql -h localhost -u root -p'' 
3. Enumerate databases
4. Find credentials in "config" table
5. Domain user: admin / AdminPass123
```

### Host 3: 192.168.100.20 (Samba File Server)

**Vulnerability:** Share misconfiguration  
**Time to Compromise:** 30m

```
1. Enumerate SMB with credentials
2. Find writable share
3. Upload reverse shell script
4. Trigger execution somehow (cron, scheduled task)
5. Get host compromised
```

### Host 4: 192.168.100.1 (Domain Controller - Final)

**Vulnerability:** Weak domain admin password  
**Time to Compromise:** 2h

```
Attack Chain:
1. Enumerate domain users
2. Extract KRBTGT hash (if DCSync possible)
3. Kerberoasting to crack service account
4. Use service account to enumerate AD
5. Find path to domain admin
6. Compromise domain controller
7. Capture proof.txt from DC
```

---

## ⏱️ Mock Exam Timeline

### Hour 0-4: Machines 1 & 2
- 1h 50m: Machine 1 (DONE)
- 2h 20m: Machine 2 (DONE)
- Time remaining: 19h 35m

### Hour 4-8: Machine 3
- 3h 40m: Machine 3 (DONE)
- Time remaining: 16h 15m

### Hour 8-16: Network Machine
- 6-8h: Network compromise (goal: full compromise)
- Time remaining: 8h 15m

### Hour 16-23h45m: Report Writing & Buffer
- 2h: Report writing (all 4 machines)
- 6h 15m: Buffer (contingency, polishing)

---

## 📋 Scoring Your Mock Exam

```
Machine 1 rooted? [ ] YES (25 pts)
Machine 2 rooted? [ ] YES (25 pts)
Machine 3 rooted? [ ] YES (25 pts)
Network complete? [ ] YES (25 pts)

TOTAL: ___ / 100 points

Passing: ≥ 70 points
```

---

## 🎯 Mock Exam Success Criteria

- ✅ All 4 machines compromised (100 pts)
- ✅ Or minimum 3 machines (75 pts)
- ✅ Complete professional report
- ✅ All screenshots included
- ✅ Attack chain documented
- ✅ Total time ≤ 23h 45m
- ✅ No cheating (no walkthroughs!)

---

## 📊 Analysis After Mock Exam

### What Went Well?
```
- [ ] Enumeration was thorough
- [ ] Time management was good
- [ ] Found vulnerabilities efficiently
- [ ] Privilege escalation worked
- [ ] Report was complete
```

### What Could Improve?
```
- [ ] Enumeration speed
- [ ] Exploitation speed
- [ ] Time allocation
- [ ] Machine prioritization
- [ ] Report quality
```

### Score vs Reality
```
Mock Exam Score: ___ / 100
Expected Exam Score: ___ / 100 (should be similar)

If mock < 70: NOT READY FOR EXAM YET
If mock 70-85: Ready, some risk
If mock 85+: Very confident
```

---

## 🚀 Pro Tips for Mock Exam

1. **No Walkthroughs** - Don't use writeups (defeats purpose)
2. **Time Tracking** - Track each phase timing
3. **Screenshots** - Take them as you go
4. **Notes** - Document attack chain
5. **Report** - Write as you progress
6. **Real Conditions** - Start early morning, take breaks like real exam

---

## 📈 Repeat Schedule

- **First Mock:** 2 weeks before exam
- **Second Mock:** 1 week before exam
- **Third Mock:** 3 days before exam (final confidence check)

**Target Progression:**
- Mock 1: 70-75 pts (borderline pass)
- Mock 2: 85-90 pts (confident)
- Mock 3: 95-100 pts (very confident)

---

**Related Notes:**
- [[09-Exam-Day/Exam-Day-Checklist|✅ Exam Day Checklist]]
- [[08-Exam-Strategy/Common-OSCP-Mistakes|❌ Common Mistakes]]

---

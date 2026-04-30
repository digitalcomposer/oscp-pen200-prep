---
tags: [oscp, resources, machines, practice]
aliases: [Exam Machines, Practice Labs]
category: Resources
difficulty: ★★☆☆☆
last-updated: 2025-04-30
---

# 🎮 OSCP-Like Machine Collections

> [!info] Practice Machines
> Curated collections matching OSCP exam difficulty & pattern.

---

## 🎖️ Official OSCP PWK Course

- **AccessDenied machines** (included in course)
- Difficulty: Medium → Hard
- Requirement: Active enrollment

---

## 🎯 TryHackMe OSCP Path

**Path:** Intrusion -> OSCP Preparation

| Machine | Difficulty | Category | Key Concept |
|---------|-----------|----------|------------|
| Network Services | Easy | Recon | Port enumeration |
| Pickle Rick | Easy | Web | RCE via injection |
| Relevant | Medium | Windows | Exploitation |
| Brainstorm | Medium | Buffer Overflow | BOF methodology |
| Wgelftpd | Easy | FTP | Anonymous access |
| Tomcat | Easy | Web | Default creds |

**Access:** https://tryhackme.com/paths/OSCP

---

## 🏴‍☠️ HackTheBox OSCP Machines

### Easy Tier

| Machine | OS | Focus |
|---------|----|----|
| Blue | Windows | EternalBlue, privesc |
| Legacy | Windows | Samba, privesc |
| Lame | Linux | VSFTPd, Samba |
| Beep | Linux | Elastix, LFI |
| Popcorn | Linux | Upload bypass, kernel |

### Medium Tier

| Machine | OS | Focus |
|---------|----|----|
| Devel | Windows | Upload bypass, kernel |
| Jerry | Windows | Tomcat, RCE |
| Granny | Windows | WebDAV, privesc |
| Shocker | Linux | ShellShock, privesc |
| Bashed | Linux | Web shell, privesc |

### Hard Tier

| Machine | OS | Focus |
|---------|----|----|
| Sense | Linux | Pfsense, priv esc |
| Optimum | Windows | HFS RCE, privesc |
| Bastard | Windows | Drupal RCE, privesc |
| Curling | Linux | Curling-enabled exploit |
| Irked | Linux | UnrealIRCd, privesc |

---

## 🔬 PentesterLab OSCP Path

- **Duration:** 60+ hours
- **Difficulty:** Beginner → Intermediate
- **Format:** Guided labs + machines
- **Access:** https://pentesterlab.com/paths/oscp

---

## 🎯 VulnHub OSCP-Like Machines

### Easy Collection

```
Boot2Root
DC: 1-9 (entire series!)
Kioptrix 1-5 (classic progression)
HackLAB: Vulnix
```

### Medium Collection

```
HA: Joker
HA: Frenzy
HA: Blind
HA: Aenigma
```

---

## 📚 Buffer Overflow Practice

```
TryHackMe: Brainstorm
HackTheBox: Brainstorm (similar)
OverTheWire: Narnia, Behemoth
```

---

## 🌐 Web Application Focus

```
DVWA (Damn Vulnerable Web App)
WebGoat
OWASP Juice Shop
HackTheBox: Irked, Unbalanced
```

---

## 🔐 Windows Privilege Escalation

```
HackTheBox: Devel, Granny, Jerry
TryHackMe: Relevant
VulnHub: HA: Joker
```

---

## 🐧 Linux Privilege Escalation

```
HackTheBox: Lame, Beep, Shocker
TryHackMe: Linux Privilege Escalation
VulnHub: Kioptrix series
```

---

## 🎯 AD/Kerberos (Bonus)

```
HackTheBox: Active, Resolute, Forest
TryHackMe: Anthem, Attacktive Directory
```

---

## 📊 Suggested Study Path

### Week 1-2: Linux Basics
- TryHackMe: Linux Privilege Escalation
- HackTheBox: Lame, Legacy
- VulnHub: Kioptrix 1

### Week 3-4: Web Exploitations
- HackTheBox: Beep (LFI), Popcorn (upload)
- TryHackMe: Pickle Rick, Wgelftpd
- DVWA: All vulnerabilities

### Week 5-6: Windows Basics
- HackTheBox: Blue (EternalBlue)
- HackTheBox: Devel, Jerry
- TryHackMe: Relevant

### Week 7-8: Mixed & Hard
- HackTheBox: Granny, Bastard
- VulnHub: HA series
- Practice speed runs (4-hour challenges)

### Week 9-10: Buffer Overflow
- TryHackMe: Brainstorm
- Complete 5+ BOF machines
- Timing: get under 2 hours per machine

---

## 💡 Practice Strategy

> [!tip] Speed Matters
> Aim for 4-5 hours per machine by exam time.

> [!tip] Document Everything
> Take screenshots during practice → use in report writing.

> [!tip] Timed Runs
> Do speed runs: set 4-hour timer, exploit machine fully.

> [!tip] Mix Difficulties
> Don't only do easy machines. Practice hard ones.

---

## 📊 Success Metrics

```
Week 1-2: 1-2 machines/week
Week 3-6: 2-3 machines/week
Week 7+:  3-4 machines/week + speed runs
```

---

**Related Notes:**
- [[00-Dashboard|📊 Study Dashboard]]
- [[01-Methodology/Pentest-Methodology|🗺️ Pentest Methodology]]

---

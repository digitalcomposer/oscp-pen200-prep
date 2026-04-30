#!/bin/bash

# OSCP PEN-200 Obsidian Vault Setup
# Creates folder structure and initializes vault with comprehensive notes

set -e

VAULT_DIR="OSCP-PEN200-Vault"

echo "🎯 Creating OSCP PEN-200 Study Vault..."

# Create folder structure
mkdir -p "$VAULT_DIR"/{01-Methodology,02-Linux,03-Windows,04-Web,05-Tools,06-Buffer-Overflow,07-Resources,.obsidian}

echo "✅ Folder structure created"

# Initialize .obsidian configuration
cat > "$VAULT_DIR/.obsidian/graph.json" << 'EOF'
{
  "showOrphans": true,
  "showTags": true,
  "showAttachments": false,
  "hideUnresolved": false,
  "showAllFileTypes": true,
  "showLinksOnHover": true,
  "colorGroups": [
    {
      "query": "tag:oscp",
      "color": {
        "a": 1,
        "rgb": 16711680
      }
    },
    {
      "query": "tag:linux",
      "color": {
        "a": 1,
        "rgb": 65280
      }
    },
    {
      "query": "tag:windows",
      "color": {
        "a": 1,
        "rgb": 255
      }
    }
  ],
  "forces": {
    "linksLength": 30,
    "repelLength": 300,
    "centralForce": 0.1
  },
  "scale": 1,
  "close": false
}
EOF

cat > "$VAULT_DIR/.obsidian/community-plugins.json" << 'EOF'
[
  "dataview",
  "templater-obsidian",
  "calendar",
  "kanban",
  "excalidraw-plugin",
  "obsidian-git",
  "checklist-plugin"
]
EOF

echo "✅ Obsidian configuration created"

# Create all markdown files (this script will be populated by the main generation)
touch "$VAULT_DIR"/00-Dashboard.md
touch "$VAULT_DIR"/01-Methodology/{Pentest-Methodology.md,Recon-and-Enumeration.md,Port-Service-Checklist.md}
touch "$VAULT_DIR"/02-Linux/{Linux-Privesc.md,Shells-and-Payloads.md,File-Transfer-Linux.md}
touch "$VAULT_DIR"/03-Windows/{Windows-Privesc.md,Active-Directory.md,File-Transfer-Windows.md}
touch "$VAULT_DIR"/04-Web/{Web-Vulnerabilities.md,SQL-Injection.md,LFI-RFI-to-RCE.md,File-Upload-Bypass.md,Command-Injection.md}
touch "$VAULT_DIR"/05-Tools/{Nmap-Cheatsheet.md,MSFvenom-Payloads.md,Reverse-Shells.md,Pivoting-Tunneling.md,Wordlists-Reference.md}
touch "$VAULT_DIR"/06-Buffer-Overflow/BOF-x86-Windows.md
touch "$VAULT_DIR"/07-Resources/{OSCP-Machine-List.md,Useful-Links.md}

echo "✅ Vault structure initialized with $(find "$VAULT_DIR" -type f | wc -l) note files"

# Instructions
echo ""
echo "════════════════════════════════════════════════════════"
echo "📚 OSCP Vault Ready!"
echo "════════════════════════════════════════════════════════"
echo ""
echo "Vault location: $VAULT_DIR/"
echo ""
echo "Next steps:"
echo "1. Open Obsidian and create new vault → select '$VAULT_DIR'"
echo "2. Notes are ready to be populated with content"
echo "3. Enable community plugins (Settings → Community Plugins)"
echo ""
echo "📖 Recommended plugins:"
echo "   - Dataview (dynamic queries)"
echo "   - Templater (note automation)"
echo "   - Calendar (study tracking)"
echo "   - Kanban (progress board)"
echo "   - Excalidraw (diagram creation)"
echo ""

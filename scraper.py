#!/usr/bin/env python3
"""
OSCP Research Scraper & Aggregator
Gathers OSCP-relevant content from multiple sources
"""

import os
import json
import requests
from datetime import datetime
from pathlib import Path
import re

class OSCPScraper:
    def __init__(self, vault_path="OSCP-PEN200-Vault"):
        self.vault_path = Path(vault_path)
        self.resources = {
            "linux_privesc": [],
            "windows_privesc": [],
            "web_vulns": [],
            "ad_attacks": [],
            "tools": [],
            "payloads": []
        }

    def scrape_github(self):
        """Scrape GitHub for OSCP resources"""
        print("[*] Scraping GitHub for OSCP resources...")

        repos = [
            "0xsyr0/OSCP",
            "slyth11907/Cheatsheets",
            "carlospolop/PEASS-ng",
            "swisskyrepo/PayloadsAllTheThings",
            "PowerShellMafia/PowerSploit"
        ]

        for repo in repos:
            try:
                url = f"https://api.github.com/repos/{repo}/readme"
                headers = {"Accept": "application/vnd.github.v3.raw"}
                response = requests.get(url, headers=headers, timeout=5)

                if response.status_code == 200:
                    print(f"[+] Found: {repo}")
                    self.resources["tools"].append({
                        "source": repo,
                        "url": f"https://github.com/{repo}",
                        "fetched": datetime.now().isoformat()
                    })
            except Exception as e:
                print(f"[-] Error fetching {repo}: {e}")

    def scrape_hacktricks(self):
        """Fetch HackTricks content"""
        print("[*] Fetching from HackTricks...")

        sections = [
            "linux-privilege-escalation",
            "windows-hardening",
            "active-directory-methodology",
            "web-vulnerabilities"
        ]

        for section in sections:
            url = f"https://book.hacktricks.xyz/{section}/"
            try:
                response = requests.head(url, timeout=5)
                if response.status_code == 200:
                    print(f"[+] HackTricks: {section}")
                    self.resources["tools"].append({
                        "source": "HackTricks",
                        "title": section,
                        "url": url,
                        "fetched": datetime.now().isoformat()
                    })
            except Exception as e:
                print(f"[-] Error: {e}")

    def scrape_payloads_all_the_things(self):
        """Fetch PayloadsAllTheThings"""
        print("[*] Fetching from PayloadsAllTheThings...")

        url = "https://api.github.com/repos/swisskyrepo/PayloadsAllTheThings/contents"

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                for item in data:
                    if item['type'] == 'dir' and 'SQL' in item['name'] or 'Command' in item['name']:
                        print(f"[+] PayloadsAllTheThings: {item['name']}")
                        self.resources["payloads"].append({
                            "source": "PayloadsAllTheThings",
                            "category": item['name'],
                            "url": item['html_url'],
                            "fetched": datetime.now().isoformat()
                        })
        except Exception as e:
            print(f"[-] Error: {e}")

    def search_google(self, query):
        """Search Google for OSCP resources (requires googlesearch)"""
        print(f"[*] Searching Google: '{query}'...")
        try:
            # Note: googlesearch may be blocked. Use with caution.
            results = []
            print(f"[!] Google search requires 'pip install google-search-official'")
            return results
        except Exception as e:
            print(f"[-] Error: {e}")
            return []

    def generate_markdown(self):
        """Generate markdown files with aggregated content"""
        print("[*] Generating markdown files...")

        # Create Linux Privesc Resources file
        linux_md = self._create_resource_file(
            "02-Linux/Linux-Privesc-Resources.md",
            "🐧 Linux Privilege Escalation Resources",
            self.resources["linux_privesc"]
        )

        # Create Payload Collection
        payload_md = self._create_resource_file(
            "02-Linux/Payload-Collection.md",
            "💀 Payload Collection",
            self.resources["payloads"]
        )

        print(f"[+] Generated {linux_md}")
        print(f"[+] Generated {payload_md}")

    def _create_resource_file(self, filepath, title, resources):
        """Create a markdown file with resources"""
        content = f"""---
tags: [oscp, resources, automated]
generated: {datetime.now().isoformat()}
---

# {title}

> [!info] Auto-Generated
> This file was automatically generated from various sources.

## Resource List

"""

        for resource in resources:
            if isinstance(resource, dict) and 'url' in resource:
                name = resource.get('source', resource.get('title', 'Unknown'))
                url = resource['url']
                content += f"- [{name}]({url})\n"

        content += f"\n---\n\n**Generated:** {datetime.now().isoformat()}\n"

        filepath = self.vault_path / filepath
        filepath.parent.mkdir(parents=True, exist_ok=True)

        with open(filepath, 'w') as f:
            f.write(content)

        return str(filepath)

    def save_json(self):
        """Save resources as JSON for dashboard"""
        output_file = self.vault_path / "resources.json"

        with open(output_file, 'w') as f:
            json.dump(self.resources, f, indent=2)

        print(f"[+] Saved resources to {output_file}")

    def run(self):
        """Run full scraping workflow"""
        print("=" * 50)
        print("OSCP Research Scraper")
        print("=" * 50)

        self.scrape_github()
        self.scrape_hacktricks()
        self.scrape_payloads_all_the_things()

        self.generate_markdown()
        self.save_json()

        print("\n[+] Scraping complete!")
        print(f"[+] Resources saved to: {self.vault_path}")

if __name__ == "__main__":
    scraper = OSCPScraper()
    scraper.run()

#!/usr/bin/env python3
"""
Advanced OSCP GitHub Content Scraper
Finds latest repos, trending techniques, common issues, and integrates findings
"""

import requests
import json
from datetime import datetime, timedelta
from collections import defaultdict
import re

class AdvancedOSCPScraper:
    def __init__(self):
        self.github_api = "https://api.github.com"
        self.findings = {
            "new_repos": [],
            "trending_techniques": [],
            "common_issues": [],
            "cve_exploits": [],
            "tool_updates": [],
            "methodology_improvements": []
        }
        self.keywords = {
            "privesc": ["privilege escalation", "priv esc", "sudo", "suid", "kernel exploit"],
            "web": ["sql injection", "rce", "lfi", "rfi", "upload bypass", "xss", "csrf"],
            "windows": ["token abuse", "juicy potato", "unquoted service", "dll hijacking"],
            "ad": ["kerberoasting", "as-rep roasting", "dcsync", "golden ticket"],
            "tools": ["nmap", "metasploit", "linpeas", "winpeas", "chisel", "ligolo"],
            "mistakes": ["fail", "error", "common mistake", "gotcha", "beware", "trap"]
        }

    def search_latest_oscp_repos(self):
        """Find newest OSCP preparation repositories"""
        print("[*] Searching for latest OSCP repositories...")

        queries = [
            "OSCP PEN-200 pushed:>2025-01-01",
            "penetration testing methodology pushed:>2025-01-01",
            "privilege escalation cheatsheet stars:>100",
            "OSCP exam writeup stars:>50",
            "buffer overflow exploit x86 stars:>50"
        ]

        for query in queries:
            try:
                url = f"{self.github_api}/search/repositories"
                params = {
                    "q": query,
                    "sort": "stars",
                    "order": "desc",
                    "per_page": 10
                }
                headers = {"Accept": "application/vnd.github.v3+json"}

                response = requests.get(url, params=params, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    for repo in data.get("items", [])[:5]:
                        repo_info = {
                            "name": repo["name"],
                            "url": repo["html_url"],
                            "stars": repo["stargazers_count"],
                            "description": repo["description"],
                            "language": repo["language"],
                            "updated": repo["updated_at"],
                            "topics": repo.get("topics", [])
                        }
                        self.findings["new_repos"].append(repo_info)
                        print(f"[+] Found: {repo['name']} ({repo['stargazers_count']} stars)")
            except Exception as e:
                print(f"[-] Error searching: {e}")

    def extract_readme_content(self, repo_url):
        """Extract README from repo for valuable content"""
        print(f"[*] Extracting README from {repo_url.split('/')[-1]}...")

        try:
            api_url = repo_url.replace("github.com", "api.github.com/repos")
            readme_url = f"{api_url}/readme"

            headers = {
                "Accept": "application/vnd.github.v3.raw",
                "User-Agent": "OSCP-Scraper"
            }

            response = requests.get(readme_url, headers=headers, timeout=10)
            if response.status_code == 200:
                content = response.text

                # Extract key techniques
                for category, keywords in self.keywords.items():
                    for keyword in keywords:
                        if keyword.lower() in content.lower():
                            # Find surrounding context
                            matches = re.finditer(f'.{{0,100}}{keyword}.{{0,100}}', content, re.IGNORECASE)
                            for match in list(matches)[:2]:  # First 2 matches
                                self.findings["trending_techniques"].append({
                                    "repo": repo_url.split("/")[-1],
                                    "category": category,
                                    "technique": keyword,
                                    "context": match.group().strip()
                                })

                return content
        except Exception as e:
            print(f"[-] Error extracting README: {e}")

        return None

    def find_common_issues(self):
        """Find common problems/issues reported by OSCP students"""
        print("[*] Searching for common OSCP issues...")

        queries = [
            "OSCP exam failed issues",
            "OSCP privilege escalation stuck",
            "OSCP exam timeout",
            "OSCP report weak",
            "OSCP enumeration mistakes"
        ]

        for query in queries:
            try:
                url = f"{self.github_api}/search/issues"
                params = {
                    "q": query,
                    "sort": "reactions",
                    "order": "desc",
                    "per_page": 5
                }
                headers = {"Accept": "application/vnd.github.v3+json"}

                response = requests.get(url, params=params, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    for issue in data.get("items", []):
                        issue_info = {
                            "title": issue["title"],
                            "url": issue["html_url"],
                            "repo": issue["repository_url"].split("/")[-1],
                            "body": issue["body"][:200] if issue["body"] else "",
                            "reactions": issue.get("reactions", {}).get("total_count", 0)
                        }

                        # Categorize issue
                        if "privilege escalation" in issue["title"].lower():
                            issue_info["category"] = "privesc"
                        elif "enumeration" in issue["title"].lower():
                            issue_info["category"] = "enumeration"
                        elif "exam" in issue["title"].lower():
                            issue_info["category"] = "exam_strategy"
                        elif "report" in issue["title"].lower():
                            issue_info["category"] = "reporting"
                        else:
                            issue_info["category"] = "general"

                        self.findings["common_issues"].append(issue_info)
                        print(f"[+] Issue: {issue['title'][:60]}")
            except Exception as e:
                print(f"[-] Error searching issues: {e}")

    def find_cve_exploits(self):
        """Find latest CVE exploits relevant to OSCP machines"""
        print("[*] Searching for relevant CVE exploits...")

        cve_queries = [
            "CVE-2021 exploit github:true",
            "CVE-2022 exploit github:true",
            "CVE-2023 exploit github:true",
            "Tomcat RCE exploit",
            "WordPress privilege escalation",
            "Samba CVE exploit"
        ]

        oscp_cves = [
            "CVE-2019-9193",  # Drupal RCE
            "CVE-2019-0604",  # BlueKeep RDP
            "CVE-2016-5195",  # Dirty COW
            "CVE-2021-4034",  # PwnKit
            "CVE-2021-22555", # Netfilter
        ]

        for cve in oscp_cves:
            try:
                url = f"{self.github_api}/search/repositories"
                params = {
                    "q": cve,
                    "sort": "stars",
                    "per_page": 3
                }
                headers = {"Accept": "application/vnd.github.v3+json"}

                response = requests.get(url, params=params, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    for repo in data.get("items", []):
                        exploit_info = {
                            "cve": cve,
                            "repo": repo["name"],
                            "url": repo["html_url"],
                            "stars": repo["stargazers_count"],
                            "language": repo["language"]
                        }
                        self.findings["cve_exploits"].append(exploit_info)
                        print(f"[+] {cve}: {repo['name']} ({repo['stargazers_count']} stars)")
            except Exception as e:
                print(f"[-] Error searching CVE {cve}: {e}")

    def find_tool_updates(self):
        """Find updates to essential OSCP tools"""
        print("[*] Checking for tool updates...")

        tools = {
            "carlospolop/PEASS-ng": "linPEAS/winPEAS",
            "jpillora/chisel": "Chisel tunneling",
            "nicocha20/ligolo-ng": "Ligolo-ng pivoting",
            "swisskyrepo/PayloadsAllTheThings": "Payloads reference",
            "danielmiessler/SecLists": "WordLists",
            "PowerShellMafia/PowerSploit": "PowerShell exploits"
        }

        for repo_path, tool_name in tools.items():
            try:
                url = f"{self.github_api}/repos/{repo_path}"
                headers = {"Accept": "application/vnd.github.v3+json"}

                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()

                    # Check if updated recently
                    updated = datetime.fromisoformat(data["updated_at"].replace("Z", "+00:00"))
                    days_old = (datetime.now(updated.tzinfo) - updated).days

                    tool_info = {
                        "tool": tool_name,
                        "repo": repo_path,
                        "url": data["html_url"],
                        "stars": data["stargazers_count"],
                        "last_updated_days_ago": days_old,
                        "description": data["description"]
                    }

                    if days_old < 30:  # Recently updated
                        self.findings["tool_updates"].append(tool_info)
                        print(f"[+] Updated: {tool_name} ({days_old} days ago)")
                    else:
                        print(f"[~] {tool_name} (last updated {days_old} days ago)")
            except Exception as e:
                print(f"[-] Error checking {tool_name}: {e}")

    def find_methodology_improvements(self):
        """Find new methodology insights from OSCP blogs/writeups"""
        print("[*] Searching for methodology improvements...")

        queries = [
            "OSCP exam report writeup stars:>100",
            "penetration testing methodology best practices",
            "OSCP machine walkthrough detailed",
            "privilege escalation methodology tutorial"
        ]

        for query in queries:
            try:
                url = f"{self.github_api}/search/repositories"
                params = {
                    "q": query,
                    "sort": "stars",
                    "per_page": 3
                }
                headers = {"Accept": "application/vnd.github.v3+json"}

                response = requests.get(url, params=params, headers=headers, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    for repo in data.get("items", []):
                        methodology_info = {
                            "title": repo["name"],
                            "url": repo["html_url"],
                            "description": repo["description"],
                            "stars": repo["stargazers_count"]
                        }
                        self.findings["methodology_improvements"].append(methodology_info)
                        print(f"[+] Methodology: {repo['name']} ({repo['stargazers_count']} stars)")
            except Exception as e:
                print(f"[-] Error searching methodology: {e}")

    def generate_report(self):
        """Generate comprehensive findings report"""
        print("\n" + "="*60)
        print("OSCP GITHUB SCRAPING REPORT")
        print("="*60)

        report = f"""
# 🔍 OSCP GitHub Scraping & Analysis Report
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 Summary

Total Findings:
- New Repositories: {len(self.findings['new_repos'])}
- Trending Techniques: {len(self.findings['trending_techniques'])}
- Common Issues: {len(self.findings['common_issues'])}
- CVE Exploits: {len(self.findings['cve_exploits'])}
- Tool Updates: {len(self.findings['tool_updates'])}
- Methodology Improvements: {len(self.findings['methodology_improvements'])}

---

## 🆕 Latest OSCP Repositories

"""

        for repo in self.findings['new_repos'][:5]:
            report += f"""
### {repo['name']}
- **URL:** {repo['url']}
- **Stars:** {repo['stars']}
- **Language:** {repo['language']}
- **Description:** {repo['description']}
- **Topics:** {', '.join(repo['topics'][:5])}
- **Last Updated:** {repo['updated']}

"""

        report += """
---

## 🔥 Trending Techniques Found

"""

        # Group trending techniques by category
        by_category = defaultdict(list)
        for technique in self.findings['trending_techniques']:
            by_category[technique['category']].append(technique)

        for category, techniques in sorted(by_category.items()):
            report += f"### {category.upper()}\n"
            for tech in techniques[:3]:  # Top 3 per category
                report += f"- **{tech['technique']}** (from {tech['repo']})\n"
                report += f"  > {tech['context'][:100]}...\n\n"

        report += """
---

## ⚠️ Common OSCP Issues (From GitHub Issues)

"""

        by_cat = defaultdict(list)
        for issue in self.findings['common_issues']:
            by_cat[issue['category']].append(issue)

        for category, issues in sorted(by_cat.items()):
            report += f"### {category.replace('_', ' ').upper()}\n"
            for issue in issues[:2]:  # Top 2 per category
                report += f"- **{issue['title']}**\n"
                report += f"  - Repo: {issue['repo']}\n"
                report += f"  - Reactions: {issue['reactions']}\n"
                report += f"  - {issue['body']}\n\n"

        report += """
---

## 🛡️ Critical CVE Exploits

"""

        for exploit in self.findings['cve_exploits'][:10]:
            report += f"- **{exploit['cve']}** → {exploit['repo']} ({exploit['stars']} ⭐)\n"
            report += f"  {exploit['url']}\n\n"

        report += """
---

## 🔧 Tool Updates (Recent)

"""

        for tool in self.findings['tool_updates']:
            report += f"- **{tool['tool']}** (Updated {tool['last_updated_days_ago']} days ago)\n"
            report += f"  {tool['url']}\n\n"

        report += """
---

## 📚 Methodology Resources

"""

        for methodology in self.findings['methodology_improvements'][:5]:
            report += f"- **{methodology['title']}** ({methodology['stars']} ⭐)\n"
            report += f"  {methodology['url']}\n"
            report += f"  {methodology['description']}\n\n"

        report += f"""
---

## 💡 Key Insights & Recommendations

### What's New:
1. **Trending Techniques:** {len(self.findings['trending_techniques'])} new exploitation vectors discovered
2. **Common Failures:** {len(self.findings['common_issues'])} documented student problems to avoid
3. **Updated Tools:** {len(self.findings['tool_updates'])} essential tools have recent updates
4. **Relevant CVEs:** {len(self.findings['cve_exploits'])} exploitable vulnerabilities documented

### Action Items:
- Review all flagged common issues (many are exam-killers!)
- Check tool updates for new capabilities
- Study trending techniques not covered in base notes
- Follow newly updated methodology resources

---

**Report Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

        return report

    def save_findings(self, report):
        """Save findings to file"""
        with open("github_scraping_findings.md", "w") as f:
            f.write(report)

        with open("github_scraping_findings.json", "w") as f:
            json.dump(self.findings, f, indent=2)

        print("[+] Findings saved to github_scraping_findings.md")
        print("[+] JSON data saved to github_scraping_findings.json")

    def run(self):
        """Execute full scraping workflow"""
        print("="*60)
        print("🔍 ADVANCED OSCP GITHUB CONTENT SCRAPER")
        print("="*60)
        print()

        self.search_latest_oscp_repos()
        self.find_common_issues()
        self.find_cve_exploits()
        self.find_tool_updates()
        self.find_methodology_improvements()

        # Extract README from top repos
        for repo in self.findings['new_repos'][:3]:
            self.extract_readme_content(repo['url'])

        # Generate and save report
        report = self.generate_report()
        self.save_findings(report)

        print("\n" + report)
        print("\n[+] SCRAPING COMPLETE!")

if __name__ == "__main__":
    scraper = AdvancedOSCPScraper()
    scraper.run()

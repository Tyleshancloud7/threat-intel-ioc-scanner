<img width="514" height="504" alt="Image 3-11-26 at 7 41 PM" src="https://github.com/user-attachments/assets/2307a843-fd6c-4395-9578-0f63283d5d5a" />


# Threat Intelligence IOC Scanner

A Python-based security tool that scans log files for **Indicators of Compromise (IOCs)** using a threat intelligence feed.
The scanner detects malicious **IP addresses, domains, and file hashes** that may indicate suspicious or compromised activity.

---

## Overview

Threat intelligence feeds provide lists of known malicious indicators collected from security research, incident response investigations, and threat monitoring.

Security teams use these feeds to identify threats hidden inside system logs and network activity.

This project simulates a **SOC threat hunting workflow** by scanning logs and identifying:

* Malicious IP addresses
* Suspicious domains
* Known malware file hashes

---

## Features

* Detects malicious IP addresses in logs
* Identifies suspicious or malicious domains
* Flags known malware hashes
* Uses a structured threat intelligence feed
* Demonstrates automated IOC detection used in SOC environments

---

## Technologies Used

* Python
* JSON threat intelligence feeds
* Log file analysis
* Security automation

---

## Project Structure

```
threat-intel-ioc-scanner/
│
├── ioc_scanner.py        # Main scanning engine
├── threat_feed.json      # Threat intelligence feed
├── sample_logs.txt       # Example log file
└── README.md             # Project documentation
```

---

## How It Works

1. The scanner loads a **threat intelligence feed** containing known malicious indicators.
2. The tool reads a **log file** containing system or network activity.
3. Each log entry is scanned against the threat intelligence feed.
4. If a match is found, the tool reports the detected indicator.

This simulates how **security teams identify Indicators of Compromise during investigations**.

---

## Example Output

```
THREAT INTELLIGENCE IOC SCAN RESULTS
=============================================

Type: Malicious IP
Indicator: 192.168.1.10
Log Entry: User login from 192.168.1.10

Type: Malicious Domain
Indicator: evil-domain.com
Log Entry: Connection to evil-domain.com detected

Type: Malicious File Hash
Indicator: 5f4dcc3b5aa765d61d8327deb882cf99
Log Entry: File hash detected: 5f4dcc3b5aa765d61d8327deb882cf99
```

---

## Skills Demonstrated

* Threat intelligence analysis
* IOC detection
* Log investigation
* Security automation
* SOC investigation workflow

---

## Possible Improvements

Future enhancements could include:

* Integration with real threat feeds (AbuseIPDB, VirusTotal, MISP)
* Real-time log monitoring
* Automatic IOC enrichment
* Risk scoring for detected indicators

---

## Author

Tylesha Alexander
Cybersecurity Student | SOC Analyst Path | Security Automation


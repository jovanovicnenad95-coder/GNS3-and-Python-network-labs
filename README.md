# GNS3 & Python Network Automation Labs

This repository documents my journey becoming a Hybrid Network Engineer. It combines core networking protocols (GNS3 labs) with modern automation tools (Python, Netmiko).

## 📂 Repository Structure

### Day 1: Basic SSH Connectivity
* **Script:** `day1.py`
* **Goal:** Connect to a Cisco IOS device via SSH using Python (Netmiko) and retrieve interface status.
* **Lab Setup:** GNS3 (Cisco Router + VMware Network Adapter).

### Day 2: Parsing Output (String Operations)
* **Script:** `day2.py`
* **Goal:** Connect to the router, run `show version`, and use Python string manipulation to extract only the software version and uptime.
* **Key Concept:** `splitlines()` method and `for` loops.

## 🚀 How to Run

1. **Install Dependencies:**

   pip install netmiko

2. Run the script:

python day1.py
python day2.py

🛠️ Tech Stack

- Python 3

- Netmiko Library

- GNS3 Network Simulator

- Cisco IOS

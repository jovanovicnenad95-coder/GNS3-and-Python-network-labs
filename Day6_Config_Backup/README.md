# Day 6: Automated Configuration Backup

**Objective:** Create a Python script to retrieve the `running-config` from multiple devices and save them locally with timestamped filenames.

## 🐍 Script Logic (`day6.py`)
This script focuses on **File I/O** (Input/Output). It connects to each device, extracts the hostname dynamically, runs `show running-config`, and writes the output to a text file.

### Key Features
* **Dynamic Filenames:** Uses `hostname` + `timestamp` to create unique backup files.
* **File Operations:** Uses Python's `with open(...)` context manager to safely create and write files.

## 💻 Code Snippet

```python
# Retrieving config
output = net_connect.send_command("show running-config")

# Dynamic filename generation
filename = f"backups/{hostname}_{current_time}.txt"

# Writing to local disk
with open(filename, 'w') as backup_file:
    backup_file.write(output)
📊 Results
1. Script Execution:

2. Generated Backup Files: Successfully created timestamped backups for all 3 switches.
# Day 2: Parsing Network Output with Python

**Objective:** Extract structured data (Interface, IP, Status) from raw Cisco IOS CLI output using native Python string manipulation methods (`splitlines`, `split`), without relying on external parsing libraries.

## 🐍 Script Logic (`day2.py`)
The script processes raw output from `show ip interface brief` to isolate specific columns.

1.  **Input:** A raw multi-line string (simulating device output).
2.  **Processing:**
    * `splitlines()`: Breaks the string into a list of lines.
    * `split()`: Breaks each line into words/columns.
    * **Filtering:** Skips the header line and extracts `Interface` (index 0) and `IP Address` (index 1).
3.  **Output:** Prints a clean, formatted list of interfaces.

## 💻 Code Snippet

```python
# Core parsing logic used in the lab
output_lines = raw_output.splitlines()

for line in output_lines:
    # Skip the header line if it contains "Interface"
    if "Interface" in line:
        continue
    
    # Break the line into words
    items = line.split()
    
    # Extract specific data points
    interface = items[0]
    ip_address = items[1]
    status = items[4]
    
    print(f"Interface: {interface} | IP: {ip_address} | Status: {status}")
📊 Results
The script successfully transformed unstructured text into readable data:

Plaintext

Interface: GigabitEthernet0/0 | IP: 192.168.10.1 | Status: up
Interface: GigabitEthernet0/1 | IP: unassigned   | Status: up
Interface: GigabitEthernet0/2 | IP: 10.0.0.1     | Status: down
💡 Key Takeaways
String Manipulation: Mastered split() and splitlines() which are fundamental for network automation.

Data Structure: Understanding how to convert "human-readable" CLI text into "machine-readable" variables is the first step toward advanced automation.
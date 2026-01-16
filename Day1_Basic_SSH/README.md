# Day 1: Basic SSH Connectivity

**Objective:** Establish a programmatic SSH connection to a Cisco IOS router using Python and the `Netmiko` library to retrieve device status.

## 🐍 Script Logic (`day1.py`)
This script replaces manual PuTTY/SSH sessions. It utilizes the **Netmiko** library to handle the complexities of SSH negotiation and CLI interaction.

1.  **Define Device:** Create a dictionary with connection parameters (IP, Username, Password, Device Type).
2.  **Connect:** Initialize `ConnectHandler` to establish the SSH session.
3.  **Execute:** Send the command `show ip interface brief`.
4.  **Output:** Print the raw string returned by the device.

## 💻 Code Snippet

```python
from netmiko import ConnectHandler

# Device definition
cisco_router = {
    'device_type': 'cisco_ios',
    'host':   '192.168.10.1',
    'username': 'admin',
    'password': 'password',
}

# Establish connection
print(f"Connecting to {cisco_router['host']}...")
net_connect = ConnectHandler(**cisco_router)

# Send command
output = net_connect.send_command('show ip int brief')

# Print result
print(output)
📊 Results
The script successfully logged into the router and retrieved the interface status without manual intervention.

Plaintext

Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0     192.168.10.1    YES NVRAM  up                    up      
GigabitEthernet0/1     unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/2     unassigned      YES NVRAM  administratively down down    
💡 Key Takeaways
Netmiko: The industry-standard library for network automation (built on top of Paramiko).

Structured Data: Learned how to pass device credentials using a Python dictionary.

Automation Basics: Moved from "clicking in a terminal" to "running a script".
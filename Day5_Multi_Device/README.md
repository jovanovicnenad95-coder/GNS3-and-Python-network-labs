# Day 5: Multi-Device Automation using Loops

**Objective:** Scale network automation by configuring multiple switches simultaneously using Python `lists` and `for loops`.

## 🐍 Script Logic (`day5.py`)
Instead of defining a single device, we define a **list of dictionaries**. The script iterates through this list, applying the same configuration set to every device in the topology.

1.  **Inventory:** A Python list containing connection details for SW1, SW2, and SW3.
2.  **Config Set:** A list of VLAN commands to be deployed standardly across the network.
3.  **The Loop:** A `for` loop that connects, configures, saves, and disconnects from each device sequentially.

## 💻 Code Snippet

```python
# The power of automation: Configure 3 (or 300) devices with one loop
for device in switches:
    print(f"Connecting to {device['host']}...")
    net_connect = ConnectHandler(**device)
    
    # Send configuration
    net_connect.send_config_set([
        'vlan 100', 'name ENGINEERING',
        'vlan 200', 'name HR_DEPT'
    ])
    
    # Save to NVRAM
    net_connect.save_config()
📊 Results
The script successfully logged into all three switches (192.168.237.11-13) and deployed the new VLANs.

Verification on Switch (SW1)
💡 Key Takeaways
Scalability: The code structure allows adding more devices simply by appending them to the list, without changing the core logic.

Consistency: Ensures every switch has the exact same VLAN ID and Name, eliminating human error.
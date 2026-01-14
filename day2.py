from netmiko import ConnectHandler

# This acts as an "address book" for the device we want to connect to.
router = {
    'device_type': 'cisco_ios',
    'host':   '192.168.237.100', 
    'username': 'admin',
    'password': 'cisco',
    'port': 22,
}

print(f"Connecting to {router['host']}...")

# Connecting
net_connect = ConnectHandler(**router)
print("Success! Connection established.")

# Send a command to the device
result = net_connect.send_command('show version')

# Print the output nicely formatted
print("-" * 30)
lines = result.splitlines()
for line in lines:
    if "Software" in line or "uptime" in line:
        print(line.strip())
print("-" * 30)
net_connect.disconnect()

# Disconnect from the device
net_connect.disconnect()
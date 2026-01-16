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
rezultat = net_connect.send_command('show ip interface brief')

# Print the output nicely formatted
print("-" * 30)
print(rezultat)
print("-" * 30)

# Disconnect from the device
net_connect.disconnect()
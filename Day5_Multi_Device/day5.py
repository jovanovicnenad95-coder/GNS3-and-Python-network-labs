from netmiko import ConnectHandler

switches = [
    {
        'device_type': 'cisco_ios',
        'host': '192.168.237.11',
        'username': 'admin',
        'password': 'password',
        'secret': 'password',
    },
    {
        'device_type': 'cisco_ios',
        'host': '192.168.237.12',
        'username': 'admin',
        'password': 'password',
        'secret': 'password',
    },
    {
        'device_type': 'cisco_ios',
        'host': '192.168.237.13',
        'username': 'admin',
        'password': 'password',
        'secret': 'password',
    },
]

config_commands = [
    'vlan 100',
    'name ENGINEERING',
    'vlan 200',
    'name HR_DEPT',
    'exit'
]


print(" Starting Multi-Device Configuration...")
print("-" * 50)

for device in switches:
    print(f"Connecting to {device['host']}...")
    
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        
        output = net_connect.send_config_set(config_commands)
        print(f" Configured {device['host']} successfully.")
        
        save_out = net_connect.save_config()
        print(" Configuration saved.")
        
        net_connect.disconnect()
        
    except Exception as e:
        print(f" Failed to configure {device['host']}. Error: {e}")

print("-" * 50)
print(" All devices processed.")
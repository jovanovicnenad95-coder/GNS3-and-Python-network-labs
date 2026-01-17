import datetime
from netmiko import ConnectHandler

current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

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

print("Starting Backup Process...")
print("-" * 50)

for device in switches:
    print(f"Connecting to {device['host']}...")

    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        hostname = net_connect.find_prompt().replace('#', '')
        print(f"Retrieving running-config from {hostname}...")
        output = net_connect.send_command("show running-config")
        filename = f"backups/{hostname}_{current_time}.txt"
        with open(filename, 'w') as backup_file:
            backup_file.write(output)
        print(f"[SUCCESS] Backup saved to: {filename}")
        net_connect.disconnect()

    except Exception as e:
        print(f"[ERROR] Failed to backup {device['host']}. Details: {e}")

print("-" * 50)
print("Backup process completed.")
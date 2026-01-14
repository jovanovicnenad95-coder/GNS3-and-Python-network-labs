from netmiko import ConnectHandler

# Podaci za povezivanje na ruter
ruter = {
    'device_type': 'cisco_ios',
    'host':   '192.168.237.100', 
    'username': 'admin',
    'password': 'cisco',
    'port': 22,
}

print("Povezujem se na ruter...")

# Povezivanje
konekcija = ConnectHandler(**ruter)
print("Uspesno povezan! Saljem komandu...")

# Slanje komande
rezultat = konekcija.send_command('show ip interface brief')

# Ispis rezultata
print("-" * 30)
print(rezultat)
print("-" * 30)

# Raskidanje veze
konekcija.disconnect()
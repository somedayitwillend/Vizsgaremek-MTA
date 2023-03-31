from netmiko import ConnectHandler
from getpass import getpass

sw1= {
        "device_type": "cisco_ios",
        "host": "192.168.0.150",
        "username": "admin",
        "password": getpass(),
        "secret": "cisco"
}
sw2= {
        "device_type": "cisco_ios",
        "host": "192.168.0.151",
        "username": "admin",
        "password": getpass(),
        "secret": "cisco",
}

sw3= {
        "device_type": "cisco_ios",
        "host": "192.168.0.152",
        "username": "admin",
        "password": getpass(),
        "secret": "cisco",
}

for device in (sw1, sw2, sw3):
    net_connect = ConnectHandler(**device)
    try:
        net_connect.enable()
        old_passwd = net_connect.send_command("show vtp password")
        print(f"Current {old_passwd}")
        net_connect.config_mode()
        passwd = input("Adja meg az új VTP jelszót: ")
        net_connect.send_command(f"vtp password {passwd}")
        print(f"A VTP jeszó sikeresen módosítva lett.")
        new_passwd = net_connect.send_command("do show vtp password")
        print(f"New {new_passwd}")
        print()
    except:
        print("Hiba lépett fel, a VTP jelszó módosítása sikertelen.")
    net_connect.disconnect()

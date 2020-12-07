interface = input('Enter interface: ')
vlan = input('Enter vlan: ')


access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']
print('*' * 30)
print("interface {}".format(interface))
print("\n".join(access_template).format(vlan))

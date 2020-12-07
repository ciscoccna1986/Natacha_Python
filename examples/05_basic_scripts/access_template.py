#!/usr/bin/env python
interface = input('Enter interface: ')
vlan = input('Enter Vlan: ')
access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print("\n" +  '*' * 30)
print('Interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))

# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf = ospf_route.split()
os1 = ospf[0]
os2 = ospf[1].strip('[]')
os3 = ospf[3].rstrip(',')
os4 = ospf[4].rstrip(',')
os5 = ospf[5]

out = '''
Prefix                {0}
AD/Metric             {1}
Next-Hop              {2}
Last update           {3}
Outbound Interface    {4}
'''
print(out.format(os1,os2,os3,os4,os5))

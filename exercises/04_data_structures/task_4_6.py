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
out = "\n{:25} {}" * 5
ospf = ospf_route.replace(",","").replace("[","").replace("]","")
ospf = ospf.split()
print(out.format(
'Prefix',ospf[0],
'AD/Metric',ospf[1],
'Next-Hop',ospf[3],
'Out update',ospf[4],
'Outbound Interface',ospf[5]))

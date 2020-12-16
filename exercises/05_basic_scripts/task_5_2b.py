# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
ip,mask = argv[1].split('/')
mask = int(mask)
ip_int = ip.split('.')
oct1,oct2,oct3,oct4 = [
int(ip_int[0]),
int(ip_int[1]),
int(ip_int[2]),
int(ip_int[3]),
]
bin_ip = "{:08b} {:08b} {:08b} {:08b}".format(oct1,oct2,oct3,oct4)
bin_ips = bin_ip[:mask] + '0' * (32-mask)
int1,int2,int3,int4 = [
int(bin_ips[0:8], 2),
int(bin_ips[8:16], 2),
int(bin_ips[16:24], 2),
int(bin_ips[24:32], 2),
]
 
mask_bin = "1" * mask + "0" * (32-mask)
m1,m2,m3,m4 = [
int(mask_bin[0:8], 2),
int(mask_bin[8:16], 2),
int(mask_bin[16:24], 2),
int(mask_bin[24:32], 2),
  ]
  
ip_out = '''
 Network:
 {0:<8} {1:<8} {2:<8} {3:<8}
 {0:08b} {1:08b} {2:08b} {3:08b}
 '''
mask_out = '''
 Mask:
 /{0}
 {1:<8} {2:<8} {3:<8} {4:<8}
 {1:08b} {2:08b} {3:08b} {4:08b}
 '''
 
print(ip_out.format(int1,int2,int3,int4))
print(mask_out.format(mask,m1,m2,m3,m4))

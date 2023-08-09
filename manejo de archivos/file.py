# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 18:56:53 2023

@author: COMPU FACIL
"""

""" archivo=open("devices.txt")
for item in archivo:
    print(item)
archivo.close()"""

lista=[]
archivo=open("C:/Users/COMPU FACIL/Downloads/devices1.txt")
for item in archivo:
    
    item=item.strip("Cisco")
    lista.append(item)
    print(item)
    
archivo.close()
print(lista)
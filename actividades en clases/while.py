# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:02:17 2023

@author: COMPU FACIL
"""

"""contar=input("Ingrese el numero de veces que desea contar:")
contar=int(contar)
contador=1

while contador<=contar:
    print(contador)
    contador+=1"""
    
while True:
        x=input("Ingrese # a contar:")
        if x =='q' or x == 'quit':
            break
        
        x=int(x)
        y=1
        while True:
            print (y)
            y=y+1
            if y>x:
                break
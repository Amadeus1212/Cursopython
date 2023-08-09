# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:59:31 2023

@author: COMPU FACIL
"""

def bisiesto(año):
    
    
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        
       
        return False

año=int(input("ingrese año  : "))
print(bisiesto(año))



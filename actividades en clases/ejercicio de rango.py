# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:36:35 2023

@author: COMPU FACIL
"""

def validar(x,min,max):
    
        try:
            print("ingrese un valor entre : ",min, "y",max)
            n= int(input(x))
            assert n >= min and n <= max
            return n
        
        except ValueError:
            print("Error ,aingrese solo numeros")
        except:
            print("Error , valor debe estar en el rango :")
            
v = validar("ingrese un valor en el rango :", -100,100)
print('')
print("el numero es : ",v)
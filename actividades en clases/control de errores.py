# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:17:15 2023

@author: COMPU FACIL
"""

try:
    x=int(input("ingrese un numero para dividir : "))
    
    y=x/2
    
    print('')
    print("El resultado es :",y)
    print('')

except ZeroDivisionError:
    print(" Error de division ")
except ArithmeticError:
    print(" Error aritmetico ")
except:
    print(" ERROR ")
    
   
print("FIN")
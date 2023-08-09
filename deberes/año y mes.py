# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:07:26 2023

@author: COMPU FACIL
"""

def bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:      
        return False
        
def diasmes(año, mes):
    diasmes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if mes == 2 and bisiesto(año):
        return 29
    else:
        return diasmes[mes]

año = int(input("Ingresa un año: "))
mes = int(input("Ingresa un mes (1-12): "))

if 1 <= mes <= 12:
    num_dias = diasmes(año, mes)
    print("El número de días en el mes {} del año {} es: {}".format(mes, año, num_dias))
else:
    print("Mes inválido. Ingresa un valor entre 1 y 12 para el mes.")

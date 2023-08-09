# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:24:58 2023

@author: COMPU FACIL
"""

archivo=open("devices.txt", "a")
while True:
    nuevo=input("ingrese nuevo item : ")
        
    if nuevo == "exit":
        print("Guardado con exito !! ")
        break 
    
    archivo.write(nuevo + "\n")
archivo.close()
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:21:09 2023

@author: COMPU FACIL
"""

Nombre=input("Ingrese el nombre : ")
Apellido=input("Ingrese su apellido :")
Ubicacion=input("Ingrese su ubicacion :")
Edad=int(input("Ingrese su edad : "))

    
if Edad>=5 and Edad<=15:
    print("Registrado como menor de edad")

elif Edad>=18 and Edad<=22:
    print("Registrado como adolecente ")

elif Edad>=25 and Edad<=50:
    print("Registrado como adulto")
    

    

print("Estimado usuario",Nombre,Apellido,"\n"
      "usted ha sido "
     )
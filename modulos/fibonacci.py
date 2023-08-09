# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:41:41 2023

@author: COMPU FACIL
"""

def fibonacci(n):
    
    a, b =0,1
    while a <= n:
        print (a, end='')
        c=a+b
        a=b
        b=c
        
    print()
    
def suma(a,b):
    
    s=a+b
    
    print(s)
    
    
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:00:18 2023

@author: COMPU FACIL
"""

def bisiesto(año):
    
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:      
        return False

año = int(input("Ingresa un año: "))
print(bisiesto(año))
    
testData = [1900, 2004, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):

            año = testData[i]

            print(año,"->",end="")

            result = bisiesto(año)

            if result == testResults[i]:

                        print("OK")

            else:

                        print("Failed")
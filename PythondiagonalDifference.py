#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    sumaP = 0
    sumaS = 0
    Diferencia = 0

    n = len(arr)
    print("largo:",n)
    #Suma diagonal principal
    i = 0
    for lista in arr:
        print(lista)
        j=0
        for a in lista:
            if(i==j):
               sumaP = sumaP + a
            j=j+1
        i=i+1
    print(sumaP)
    #Suma diagonal secundaria
    i = n - 1
    for lista in arr:
        print(lista)
        j=0
        for a in lista:
            if(i==j):
               sumaS = sumaS + a
            j=j+1
        i=i-1
    print("Suma diagonal principal",sumaP)
    print("Suma diagonal secundaria",sumaS)
    Diferencia = sumaP - sumaS 
    #Modulo absoluto de la Diferencia
    if(Diferencia < 0):
        Diferencia = - Diferencia
    return(Diferencia)

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
# Lectura de las líneas de entrada
    print("Ingrese tamano de la matriz")
    n = int(input())
    print("d:",n)
    arr = []
    for _ in range(n):
        print("Ingrese fila de la matriz")
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(str(result) + '\n')
    


# Trazador (spline) lineal, grado 1
import numpy as np
import sympy as sp

def trazalineal(xi,fi):
    n = len(xi)
    x = sp.Symbol('x')
    polinomio = []
    tramo=1
    while not(tramo>=n):
        m =(fi[tramo]-fi[tramo-1])/(xi[tramo]-xi[tramo-1])
        inicio = fi[tramo-1]-m*xi[tramo-1]
        ptramo = inicio + m*x
        polinomio.append(ptramo)
        tramo = tramo + 1
    return(polinomio)

# PROGRAMA
# INGRESO , Datos de prueba
xi = [-1 , 0, 3, 4]
fi = [15.5, 3, 8, 1]
resolucion = 10 # entre cada par de puntos

# PROCEDIMIENTO
n = len(xi)
# Obtiene los polinomios por tramos
polinomio = trazalineal(xi,fi)

# SALIDA
print('Polinomios por tramos: ')
for tramo in range(1,n,1):
    print(' x = ['+str(xi[tramo-1])
          +','+str(xi[tramo])+']')
    print(str(polinomio[tramo-1]))
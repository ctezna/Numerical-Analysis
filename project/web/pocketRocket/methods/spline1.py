# Trazador (spline) lineal, grado 1
import numpy as np
import sympy as sp

def trazalineal(xi,fi):
    xi = [float(x) for x in xi]
    fi = [float(x) for x in fi]
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

def spline1_main(xi, fi):
    xi = [float(x) for x in xi]
    fi = [float(x) for x in fi]
    polinomio = trazalineal(xi,fi)
    n = len(xi)
    print('Polinomios por tramos: ')
    data = {'inter': [], 'poli': []}

    for tramo in range(1,n,1):
        #print(' x = ['+str(xi[tramo-1])+','+str(xi[tramo])+']')
        data['inter'].append(' x = ['+str(xi[tramo-1]) +','+str(xi[tramo])+']')
        data['poli'].append(str(polinomio[tramo-1]))
        #print(str(polinomio[tramo-1]))

    return data

#main()
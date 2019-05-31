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
    message = ""
    xi = [float(x) for x in xi]
    fi = [float(x) for x in fi]

    if not valid_data(xi):
        message += "Each x point must be different"
        return {}, message

    polinomio = trazalineal(xi,fi)
    n = len(xi)
    print('Polinomios por tramos: ')
    data = {'inter': [], 'poli': []}

    for tramo in range(1,n,1):
        #print(' x = ['+str(xi[tramo-1])+','+str(xi[tramo])+']')
        data['inter'].append(str(xi[tramo-1]) +' --- '+str(xi[tramo]))
        data['poli'].append(str(polinomio[tramo-1]))
        #print(str(polinomio[tramo-1]))

    return data, message


def valid_data(x_points):
    for i in x_points:
        count = x_points.count(i)

        if count >= 2:
            return False

    return True
#main()
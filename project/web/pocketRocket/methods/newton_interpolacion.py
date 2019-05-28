import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

def newton_inter(n, x, y):
    n = int(4)
    x = [float(i) for i in x]
    y = [float(i) for i in x]
    j = 0
    temp = 0
    tabla = np.zeros((n+1,n+1))

    for i in range(n):
        tabla[i][0] = x[i]
        tabla[i][1] = y[i]

    pol_new = polinomioNewton(tabla,n)
    res = pol_new[0].tolist()
    pol = pol_new[1]
    table = pol_new[2]

    for i in range(len(res)):
        res[i].pop(0)
    res.pop()
    return {'pol': pol, 'table': table}


def polinomioNewton(tabla,n):
    polinomio = "P(X) = " + str(tabla[0][1])
    F = Function('F')
    for j in range(2,n+1):
        for i in range(j-1,n):
            tabla[i][j] = (tabla[i][j-1] - tabla[i-1][j-1])/(tabla[i][0] - tabla[i-j+1][0])
            if(i==j-1):
                polinomio += " + " + str(tabla[i][j])
                for i in range(0,i):
                    polinomio += "(x - " + str(tabla[i][0]) + ")"
    data_table = imprimirTabla(tabla,n)
    F = parse_expr(polinomio.replace("P(X) = ","").replace("(","*("))
    print("\nPolinomio interpolante \n" + polinomio)

    return (tabla, polinomio, data_table)

def imprimirTabla(tabla,n):
    data_table = []
    print(" n | xi | f[xi] | Primera | Segunda | Tercera | nCuarta | Quinta | Nesima |" )
    for i in range(n):
        data_table.append(str(tabla[i]).replace("'"," ").replace(",","       ").replace("["," ").replace("]"," ").replace(" 0 ", " "))
        print(str(i) + "     " + str(tabla[i]).replace("'"," ").replace(",","       ").replace("["," ").replace("]"," ").replace(" 0 ", " "))
        print("\n")
    
    return data_table

    




#newton_inter(4,[0,1,3,5],[0,2,1,-1])

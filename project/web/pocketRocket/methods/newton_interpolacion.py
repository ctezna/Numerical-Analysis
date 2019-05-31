import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

def newton_inter(x, y):
    message = ""
    n = int(len(x))
    x = [float(i) for i in x]
    y = [float(i) for i in x]

    if not valid_data(x):
        message += "Each x point must be different"
        return {}, message

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

    return {'pol': pol, 'table': table, 'n': [x for x in range(len(table))]}, message


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
    #print("\nPolinomio interpolante \n" + polinomio)

    return (tabla, polinomio, data_table)

def imprimirTabla(tabla,n):
    new_data = []
    data_table = []
    #print(" n | xi | f[xi] | Primera | Segunda | Tercera | nCuarta | Quinta | Nesima |" )
    for i in range(n):
        data_table.append(str(tabla[i]).replace("'"," ").replace(",","       ").replace("["," ").replace("]"," ").replace(" 0 ", " "))
     #   print(str(i) + "     " + str(tabla[i]).replace("'"," ").replace(",","       ").replace("["," ").replace("]"," ").replace(" 0 ", " "))
      #  print("\n")

    
    for i in data_table:
        data = i.split(" ")
        a = []

        for j in data: 
            if j != '':
                a.append(j)
        new_data.append(a)


    return new_data


def valid_data(x_points):
    for i in x_points:
        count = x_points.count(i)

        if count >= 2:
            return False

    return True




#newton_inter(4,[0,1,3,5],[0,2,1,-1])

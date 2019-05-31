from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math
"""
Parámetros:
    valor -- punto donde se evalua el polinomio
    x -- vector con los x's
    y -- vector los x's evaluados en la función.
"""
def lagrange_method(valor,x,y):
    message = ""
    pol_list = []
    l = []
    valor = float(valor)
    x = [float(i) for i in x]
    y = [float(i) for i in y]

    if not valid_data(x):
        message += "Each x point must be different"
        return {}, message
        
    pol = ""
    G = Function('G')
    F = Function('F')
    n = len(x) #numero de puntos
    result = 0
    for k in range(n):
        productoria = 1
        termino = "("
        for i in range(n):
            if i != k:
                productoria *=  (valor - x[i])/(x[k] - x[i])
                termino += "(x-"+str(x[i])+")"
        termino += ")/("
        for i in range(n):
            if i != k:
                termino += "(" + str(x[k]) + "-" + str(x[i]) + ")"
        termino += ")"
        termino = termino.replace(")(",") * (")
        F = parse_expr(termino)
        pol_str = (termino.replace("((","(").replace("))",")") + " = " + str(expand(F)))
        pol_list.append(pol_str)
        l.append(k)
        #print("\n L" + str(k) + "(x) = " + termino.replace("((","(").replace("))",")") + " = " + str(expand(F)))
        toReplace = "L" + str(k) + "(x) = "
        pol += "(" + str(expand(F)) + ")*" + str(y[k])
        if k != n-1:
            pol += " + "
        result += productoria*y[k]
    G = str(expand(pol))
    #print ("\nPolinomio interpolante")
    #print (G)
    #print ("\nResultado")
    #print ("f(",valor,") = ",result)
    return {'PI': G, 'result': result, 'pol': pol_list, 'L': l}, message


def valid_data(x_points):
    for i in x_points:
        count = x_points.count(i)

        if count >= 2:
            return False

    return True


#agrange(4,[-1,0,3,4],[15.5,3,8,1])

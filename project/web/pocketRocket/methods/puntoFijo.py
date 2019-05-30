from sympy import symbols, diff, pprint, factorial, ln, exp, sin, cos, log, sqrt, sympify
import numpy as np
from decimal import Decimal
#(K^n/1-k) * (p1-p0)

#para escoger que funcion es mejor, evaluo la funcion en los extremos del intervalo
#y escogo la que los resultados den valores dentro del rango

# K - saco la primera derivada y la evaluo en los extremos del intervalo
#y me tiene que dar menor a uno, escogo el x mas grande

# para sacar la g() se despeja la x de una de las variables

def puntoFijo(f_string, g_string, f,g,x0,tol,nmax):
    message = ""
    data = {}

    if "ln" in f_string and float(x0) <= 0:
        message += "--- log can't take values <= 0"
        return message, data

    x = float(x0)
    if eval(g_string) == 0:
        message += "--- g(x0) can't be 0, please change x0"
        return message, data
    
    x0 = float(x0)
    tol = float(tol)
    nmax = float(nmax)
    dx0 = 0
    cont = 0
    err = tol+1
    err1 = tol+1
    x = symbols('x', real=True)
    fx = sympify(f).subs(x, x0)

    print("\n-------------------------------------------------------")
    print("iteracion | xcentro | fxcentro |error abs")
    print(cont, "|", x0,"|",fx,"|",err1)
    err_round = '%.2E' % Decimal(str(err1))
    data = {'iter': [cont], 'xcentro': [round(x0,4)], 'fcentro': [round(fx,4)], 'error': [err_round]}
    while((fx != 0) and (err1 > tol) and (cont < nmax) ):
        dx0 = sympify(g).subs(x, x0)
        fx = sympify(f).subs(x, dx0)
        err1 = abs(dx0-x0) #dx0 = xn x0= xn-1
        err = abs((dx0-x0)/dx0) #err relativo
        x0 = dx0
        cont = cont+1
        print(cont, "|", x0,"|",fx,"|",err1)
        data['iter'].append(cont)
        data['xcentro'].append(round(x0,4))
        data['fcentro'].append(round(fx,4))
        err_round = '%.2E' % Decimal(str(err1))
        data['error'].append(err_round)
    if(fx == 0):
        print("\n error:",err1)
        print(x0, "no es raiz")
        message += "is not root: %s" % (str(x0))
    elif(err1 < tol):
        print("\n error:",err1)
        print(x0, "aproxima a la raiz")
        message += "--- it's an aproximation: %s " %s (str(x0))
    else:
        print("\n el metodo fracaso")
        message += "Method failed"

    return message, data

def f(x): #fucnion originaĺ
    #print("exp(-x) - sin(4*x)")
    return -exp(7-4*x) - x**2 +10

def g(x): #despejo la x (del termino que quiera) 
    return sqrt(10-exp(7-4*x)) #xn+1


#         f,g,x0,tol,nmax
#puntoFijo(f,g,3.15,1e-7,100)
#derivada()

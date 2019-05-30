from sympy import symbols, diff, pprint, factorial, ln, exp, sin, cos, log, sqrt, sympify
import numpy as np
from decimal import Decimal

def secante_method(x0, x1, tol,niter, f, f_string):
    message = ""
    x0 = float(x0)
    x1 = float(x1)
    tol = float(tol)
    niter = int(niter)

    if x0 >= x1:
        message += "--- x0 >= x1 wrong interval"
        data = {}
        return message, data


    if x0 < 0 or x1 < 0 or tol < 0 or niter < 0:
        message += "--- Please check your values, something is wrong"
        data ={}
        return message, data

    #x = symbols('x', real=True)
    x = x0 
    y0 = eval(f_string)
    x = x1
    y1 = eval(f_string)
    #y0 = sympify(f).subs(x, x0)
    #y1 = sympify(f).subs(x, x1)
    #y0 = f(x0)
    #y1 = f(x1)
    cont = 0
    err=0
    print("\n-------------------------------------------------------")
    print("iteracion | xcentro | fxcentro |error abs")
    print(cont, "|", x0,"|",y1,"|",err)
    err_round = '%.2E' % Decimal(str(err))
    data = {'iter': [cont], 'xcentro': [round(x0,4)], 'fxcentro': [round(y1,4)], 'err': [err_round]}
    while abs(y1) > tol and cont < niter:
        try:
            denominator = float(y1 - y0)/(x1 - x0)
            x = x1 - float(y1)/denominator
        except ZeroDivisionError:
            message += "Error! - denominator zero for x = %s" % (str(x))
            print ("Error! - denominator zero for x = ", x)
            return message, data

        err = abs(x1-x0)
        x0 = x1
        x1 = x
        y0 = y1
        x = symbols('x', real=True)
        y1 = sympify(f).subs(x, x1)
        #y1 = f(x1)
        cont += 1
        print(cont, "|", x0,"|",y0,"|",err)
        data["iter"].append(cont)
        data["xcentro"].append(round(x0,4))
        data["fxcentro"].append(round(y1,4))
        err_round = '%.2E' % Decimal(str(err))
        data["err"].append(err_round)
    if abs(y1) > tol:
        cont = -1

    return message, data

def f(x):
    return exp(-x+1) - x**2 + 4*x

#x0 = 1   
#x1 = 2
#niter=11
#tol=0.0005
#secant(f, x0, x1, tol, niter)
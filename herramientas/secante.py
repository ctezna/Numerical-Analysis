from sympy import symbols, diff, pprint, factorial, ln, exp, sin, cos, log, sqrt
import numpy as np

def secant(f, x0, x1, tol,niter):
    y0 = f(x0)
    y1 = f(x1)
    cont = 0
    err=0
    print("\n-------------------------------------------------------")
    print("iteracion | xcentro | fxcentro |error abs")
    print(cont, "|", x0,"|",y1,"|",err)
    while abs(y1) > tol and cont < niter:
        try:
            denominator = float(y1 - y0)/(x1 - x0)
            x = x1 - float(y1)/denominator
        except ZeroDivisionError:
            print ("Error! - denominator zero for x = ", x)
            sys.exit(1)
        err = abs(x1-x0)
        x0 = x1
        x1 = x
        y0 = y1
        y1 = f(x1)
        cont += 1
        print(cont, "|", x0,"|",y0,"|",err)
    if abs(y1) > tol:
        cont = -1
    return x, cont

def f(x):
    return exp(-x+1) - x**2 + 4*x

x0 = 1   
x1 = 2
niter=11
tol=0.0005
secant(f, x0, x1, tol, niter)
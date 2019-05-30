from sympy import symbols, diff, pprint, factorial, ln, exp, sin, log , cos, sympify
import numpy as np
from decimal import Decimal

def regla_falsa (f,x0,x1,tol,nmax):
    temp,err,cont,xcentro = 0,0,1,0
    x0 = float(x0)
    x1 = float(x1)
    tol = float(tol)
    nmax = float(nmax)
    message = ""

    if x0 >= x1:
        message += "--- Please check your values, something is wrong"
        data ={}
        return message, data
    
    if x0 < 0 or x1 < 0 or nmax < 0 or tol < 0:
        message += "--- Please check your values, something is wrong"
        data ={}
        return message, data

    #x = symbols('x', real=True)
    #xant = sympify(f).subs(x, x0)
    #xact = sympify(f).subs(x, x1)
    x = x0
    xant = eval(f)
    x = x1
    xact = eval(f)
    data = {"iter": [], 'xmedio': [], 'fcentro': [], "error": []}
    if (xant == 0):
        print(x0, "es raiz")
        message += "-- is root: %s" % (str(x0))
        return message, data
    else:
        if (xact == 0):
            message += "-- is root: %s" % (str(x1))
            print(x1, "es raiz")
            return message, data
        else:
            if (xant*xact < 0):
                xcentro = x0 - (xant*(x1-x0)/(xact-xant))
                #fcentro = sympify(f).subs(x, xcentro)
                x = xcentro
                fcentro = eval(f)
                err = tol + 1
                data['iter'].append(cont)
                data['xmedio'].append(round(xcentro,4))
                data['fcentro'].append(fcentro)
                print (err)
                err_round = '%.2E' % Decimal(str(err))
                data['error'].append(err_round)
                while((err > tol) and (fcentro != 0) and cont < nmax):
                    if (xant*fcentro < 0):
                        x1 = xcentro
                        xact = fcentro
                    else:
                        x0 = xcentro
                        xant = fcentro
                    temp = xcentro
                    xcentro = x0 - (xant*(x1-x0)/(xact-xant))
                    #fcentro = sympify(f).subs(x, xcentro)
                    x = xcentro
                    fcentro = eval(f)
                    err = abs(xcentro - temp)
                    cont += 1
                    data['iter'].append(cont)
                    data['xmedio'].append(round(xcentro,4))
                    data['fcentro'].append(fcentro)
                    err_round = '%.2E' % Decimal(str(err))
                    data['error'].append(err_round)
                if (fcentro == 0):
                    print(xcentro,"es raiz")
                    message += "-- is root: %s" % (str(xcentro))
                else:
                    if(err < tol):
                        print('\n')
                        print(xcentro,"es una aproximacion a la raiz")
                        message += "-- it's an aproximation to root: %s" % (str(xcentro))
                        print(err, "con error")
                    else:
                        message += "--- Method failed"
                        print("el metodo fracaso")
                        return message, data
            else:
                message += "--- Bad interval, please consider change it"
                print("el intervalo no sirve")
    
    return message, data

def f(x):
    return exp(-x+1) - x**2 + 4*x + (7*(cos(x**2 - 4)**2)) -7

#          (f,x0,x1,tol,nmax):
#regla_falsa(f,0.0,3.3,1e-7,100)
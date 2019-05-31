import math
from sympy import symbols, sympify
from decimal import Decimal

def multipleRoots_method(tol,xa,niter, f, f_x_1, f_x_2):
    message = ""
    tol = float(tol)
    xa = float(xa)
    niter = int(niter)
    x = symbols('x', real=True)
    fx = sympify(f).subs(x, xa)
    dfx = sympify(f_x_1).subs(x, xa)
    d2fx = sympify(f_x_2).subs(x, xa)

    if tol <= 0 or xa <= 0 or niter <= 0:
        message += "Please check your data, something is wrong"
        return {}, message

    #fx = f(xa)
    #dfx = fd(xa)
    #d2fx = d2f(xa)
    cont = 0
    error = tol + 1
    print(cont, "         |", xa, "|", fx, "|", dfx, "|", d2fx, "|", error)
    err_round = '%.2E' % Decimal(str(error))
    data = {'iter': [cont], 'xa': [round(xa,4)], 'fx': [round(fx,4)], 'dfx': [round(dfx,4)], 'd2fx':[round(d2fx,4)], 'err':[err_round]}
    while((((dfx*dfx)-fx*d2fx))!= 0) and (fx !=0) and (error > tol) and (cont < niter) and (dfx != 0) and (d2fx != 0):
        xn = xa - ((fx*dfx)/((dfx*dfx)-fx*d2fx))
        fx = sympify(f).subs(x, xn)
        dfx = sympify(f_x_1).subs(x, xn)
        d2fx = sympify(f_x_2).subs(x, xn)
        #fx = f(xn)
        #dfx = fd(xn)
        #d2fx = d2f(xn)
        error = abs(xn - xa)
        xa = xn
        cont = cont + 1
        print(cont, "         |", xa, "|", fx, "|", dfx, "|", d2fx, "|", error)
        data['iter'].append(cont)
        data['xa'].append(round(xa,4))
        data['fx'].append(round(fx,4))
        data['dfx'].append(round(dfx,4))
        data['d2fx'].append(round(d2fx,4))
        err_round = '%.2E' % Decimal(str(error))
        data['err'].append(err_round)

    if fx == 0:
        message += "%s is a root" % (str(xa))
        print(str(xa) + " is a root")
    elif dfx == 0:
        message += "%s is a possible multiple root" % (str(xa))
        print(str(xa) + " Is a possible multiple root ")
    elif d2fx == 0:
        message += "%s is a possible multiple root" % (str(xa))
        print(str(xa) + " Is a possible multiple root ")
    elif error < tol:
        message += "%s is a root aproximation with a tolerance of = %s" % (str(xa), str(tol))
        print(str(xa) + " Is a root aproximation with a tolerance of = " + str(tol))
    else:
        message += "Failure reached in %s iterations" % (str(niter))
        print("failure reached in " + str(niter) + "iterations")

    return data, message


def f(x):
    return x*x*x - x*x - x + 1 + math.sin(x-1)**2

def fd(x):
    return 3*x*x - 2*x + math.sin(2*(x-1)) - 1

def d2f(x):
    return 6*x + 2*math.cos(2*(x-1)) - 2

#multipleRoots(10**-5,0.5,10)

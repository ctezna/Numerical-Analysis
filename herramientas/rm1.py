import math

def multipleRoots(tol,xa,niter):
    fx = f(xa)
    dfx = fd(xa)
    d2fx = d2f(xa)
    cont = 0
    error = tol + 1
    print(cont, "         |", xa, "|", fx, "|", dfx, "|", d2fx, "|", error)
    while((((dfx*dfx)-fx*d2fx))!= 0) and (fx !=0) and (error > tol) and (cont < niter) and (dfx != 0) and (d2fx != 0):
        xn = xa - ((fx*dfx)/((dfx*dfx)-fx*d2fx))
        fx = f(xn)
        dfx = fd(xn)
        d2fx = d2f(xn)
        error = abs(xn - xa)
        xa = xn
        cont = cont + 1
        print(cont, "         |", xa, "|", fx, "|", dfx, "|", d2fx, "|", error)
    if fx == 0:
        print(str(xa) + " is a root")
    elif dfx == 0: 
        print(str(xa) + " Is a possible multiple root ")
    elif d2fx == 0:
        print(str(xa) + " Is a possible multiple root ")
    elif error < tol:
        print(str(xa) + " Is a root aproximation with a tolerance of = " + str(tol))
    else:
        print("failure reached in " + str(niter) + "iterations")
def f(x):
    return x*x*x - x*x - x + 1 + math.sin(x-1)**2

def fd(x):
    return 3*x*x - 2*x + math.sin(2*(x-1)) - 1

def d2f(x):
    return 6*x + 2*math.cos(2*(x-1)) - 2

multipleRoots(10**-5,0.5,10)

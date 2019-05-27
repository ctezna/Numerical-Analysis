from sympy import symbols, diff, pprint, factorial, ln, exp, sin, cos, log, sqrt, sympify
import numpy as np

#(K^n/1-k) * (p1-p0)

#para escoger que funcion es mejor, evaluo la funcion en los extremos del intervalo
#y escogo la que los resultados den valores dentro del rango

# K - saco la primera derivada y la evaluo en los extremos del intervalo
#y me tiene que dar menor a uno, escogo el x mas grande

# para sacar la g() se despeja la x de una de las variables

def puntoFijo(f,g,x0,tol,nmax):
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
    data = {'iter': [cont], 'xcentro': [x0], 'fcentro': [fx], 'error': [err1]}
    while((fx != 0) and (err1 > tol) and (cont < nmax) ):
        dx0 = sympify(g).subs(x, x0)
        fx = sympify(f).subs(x, dx0)
        err1 = abs(dx0-x0) #dx0 = xn x0= xn-1
        err = abs((dx0-x0)/dx0) #err relativo
        x0 = dx0
        cont = cont+1
        print(cont, "|", x0,"|",fx,"|",err1)
        data['iter'].append(cont)
        data['xcentro'].append(x0)
        data['fcentro'].append(fx)
        data['error'].append(err1)
    if(fx == 0):
        print("\n error:",err1)
        print(x0, "no es raiz")
    elif(err1 < tol):
        print("\n error:",err1)
        print(x0, "aproxima a la raiz")
    else:
        print("\n el metodo fracaso")

    return data

def f(x): #fucnion originaĺ
    #print("exp(-x) - sin(4*x)")
    return -exp(7-4*x) - x**2 +10

def g(x): #despejo la x (del termino que quiera) 
    return sqrt(10-exp(7-4*x)) #xn+1


#         f,g,x0,tol,nmax
#puntoFijo(f,g,3.15,1e-7,100)
#derivada()

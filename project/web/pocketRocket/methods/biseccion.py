from sympy import symbols, diff, pprint, factorial, ln, exp, sin, cos, tan, log, sympify
import numpy as np

#LOS 3 TRAZADORES

'''
    f = funcion a la que se le busca la raiz
    a = menor valor del intervalo
    b = mayor valor del intervalo
    nmax = numero maximo de iteraciones
    tol = tolerancia del metodo? error absoluto
'''

#Metodo de Biseccion
def biseccion(f, a, b, nmax, tol):
    a = float(a)
    b = float(b)
    nmax = float(nmax)
    tol = float(tol)
    #definicion de variables
    cont = 1
    err = 1000
    centro = (a+b)/2
    x = symbols('x', real=True)
    fcentro = sympify(f).subs(x,centro)
    fant  = sympify(f).subs(x,a)
    fact = sympify(f).subs(x,b)
    if(abs(fant) <= tol):#si f(a) es raiz, retorne y termine el programa
        print(a,'es raiz de f')
    if (abs(fact) <= tol):#si f(b) es raiz, retorne y termine el programa
        print(b, 'es raiz de f')
    print("\n-------------------------------------------------------")
    print("iteracion | xi | xs | fcentro |error abs")
    print(cont,"       |  ", a,"|",b,"  |",fcentro,"|",err)
    data = {'iter': [cont], 'xi': [a], 'xs': [b], 'centro': [centro], 'fcentro': [fcentro],'error': [err]}
    #mientras no exeda el numero de iteraciones o el error no exeda la tolerancia, siga buscando una raiz
    while ((err >= tol) and (cont <= nmax)):
        if fant*fcentro < 0:
            b = centro
            fact = fcentro
        else:
            a = centro
            fant = fcentro
        temp = centro
        centro = (a+b)/2
        fcentro = sympify(f).subs(x,centro)
        err = abs(centro-temp) #error absoluto
        cont = cont + 1
        data['iter'].append(cont)
        data['xi'].append(a)
        data['xs'].append(b)
        data['centro'].append(centro)
        data['fcentro'].append(fcentro)
        data['error'].append(err)
        print(cont, "|", a,"|",b,"|",centro,"|",err)

    if(err < tol):
        print("\n err absoluto:",err)
        print('Se encontro una aproximacion de la raiz en', centro)
    else:
        print('El método fracasó después de N iteraciones')

    return data
#Al terminar, el metodo retorna una aproximacion
#a la raiz en el intervalo definido por busquedas
#incrementales y el polinomio otorgado por algun metodo de interpolacion


def f(x):
    return exp(-x + 1) - x**3 + 2 
#         f, a, b, nmax, tol
#biseccion(f,1.3899,1.3909,100,1*10**-7)
from sympy import symbols, diff, pprint, factorial, ln, exp, sin, cos, tan, log, sympify
import numpy as np
from decimal import Decimal

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
    messages = ""
    data = {}
    if a >= b:
        messages += "Please insert a valid interval"
        return messages, data

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
        print(a,'is root of f')
        messages += '- %s is root of f' % (str(a))
        return messages
    if (abs(fact) <= tol):#si f(b) es raiz, retorne y termine el programa
        print(b, 'es raiz de f')
        messages += '- %s es raiz de f' % (str(b))
        return messages

    print("\n-------------------------------------------------------")
    print("iteracion | xi | xs | fcentro |error abs")
    print(cont,"       |  ", a,"|",b,"  |",fcentro,"|",err)
    err_round = '%.2E' % Decimal(err)
    data = {'iter': [round(cont,4)], 'xi': [round(a,4)], 'xs': [round(b,4)], 'centro': [round(centro)], 'fcentro': [round(fcentro)],'error': [err_round]}
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
        data['xi'].append(round(a,4))
        data['xs'].append(round(b,4))
        data['centro'].append(round(centro,4))
        data['fcentro'].append(round(fcentro,4))
        err_round = '%.2E' % Decimal(err)
        data['error'].append(err_round)
        print(cont, "|", a,"|",b,"|",centro,"|",err)

    if(err < tol):
        #print("\n err absoluto:",err)
        messages += '- root aproximation found: %s' % (str(centro))
        print('Se encontro una aproximacion de la raiz en', centro)
    else:
        messages += '- El método fracasó después de N iteraciones'
        print('The method fails')

    return messages, data
#Al terminar, el metodo retorna una aproximacion
#a la raiz en el intervalo definido por busquedas
#incrementales y el polinomio otorgado por algun metodo de interpolacion


def f(x):
    return exp(-x + 1) - x**3 + 2 
#         f, a, b, nmax, tol
#biseccion(f,1.3899,1.3909,100,1*10**-7)
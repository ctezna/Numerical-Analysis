from sympy import symbols, diff, pprint, factorial, ln, exp, sin, cos, log, sympify
import numpy as np

#Metodo de busquedas incrementales
def busqueda_incremental(f, x0, paso, nmax, tol):
    x = symbols('x', real=True)
    #definicion de variables
    x0 = float(x0)
    paso = float(paso)
    nmax = float(nmax)
    tol = float(tol)
    r0 = sympify(f).subs(x,x0)
    if (abs(r0) <= tol): #si f(x0) es raiz, retorne y termine el programa
        print(x0,"es raiz")
        result += "[" + str(x0) + " , " + str(x0) + "]" + "\n"
    x1=x0+paso
    cont=1
    r1 = sympify(f).subs(x, x1)
    result = ""
    if (abs(r1) <= tol): #si f(x0) es raiz, retorne y termine el programa
        print(x1,"es raiz")
        result += "[" + str(x1) + " , " + str(x1) + "]" + "\n"
    while(cont < nmax): #mientras no exeda el numero de iteraciones, siga buscando una raiz
        if(r0*r1<0): #si hay cambio de signo de la funcion, hay una raiz en el intervalo x0-x1 
            print("Raiz entre",x0,"~",x1)  #imprime el intervalo
            result += "[" + str(x0) + " , " + str(x1) + "]" + "\n"
        #defino las nuevas variables para buscar otra raiz
        x0=x1
        r0=r1
        x1=x0+paso #incremento el paso
        r1 = sympify(f).subs(x, x1)
        cont=cont+1
        if(r1 == 0): #si la f(x1) = 0, entonces hay una raiz
            print(x0,"es raiz")
            result += "[" + str(x0) + " , " + str(x0) + "]" + "\n"

    return result

#Al terminar, el metodo retorna todos los intervalos
#en los uqe hay una raiz
        
def f(x): #funcion reciida como parametro
    return exp(-x+1) - x**2 + 4*x + (7*(cos(x**2 - 4)**2)) -7

#                   (f,x0,paso(h),namx,tol)
#busqueda_incremental(f,0.0,0.2,100,1.0e-7)
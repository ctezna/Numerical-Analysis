from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from scipy.misc import derivative
import sys
import sympy 
from sympy.parsing.sympy_parser import parse_expr
import numpy as np 
import matplotlib.pyplot as plt
import math

# Programa para encontrar derivadas simbolicas y evaluarlas con algun valor dado por el usuario

x = symbols('x', real=True)
s = input("\nFunción a derivar (respecto a x): ")
ps=parse_expr(s,locals())
derivada = diff(ps,x)
derivada2 = diff(derivada,x)
derivada3 = diff(derivada2,x)
derivada4 = diff(derivada3,x)
print("\nLa primera derivada es: ", derivada)
print("\nLa segunda derivada es: ", derivada2)
print("\nLa tercera derivada es: ", derivada3)
print("\nLa cuarta derivada es: ", derivada4)

decisionFuncion = int(input("\n¿Desea evaluar la funcion ingresada?\n1 = Si / 2 = No : "))

if decisionFuncion != 1 and decisionFuncion != 2:
    print("Error, favor solo ingresar alguna opción valida")
    sys.exit()
if decisionFuncion == 2:
    sys.exit()
while decisionFuncion == 1:
    valorAevaluar = int(input("\nvalor a evaluar en la funcion ingresada: "))
    resultado = sympy.sympify(ps).subs(x, valorAevaluar)
    print("\nResultado = ", resultado)
    break


decisionDerivada = int(input("\n¿Que derivada desea evaluar? (1, 2, 3, 4) : "))

if decisionDerivada == 1:
    valorAevaluar = int(input("\nvalor a evaluar en la 1ra derivada: "))
    resultado = sympy.sympify(derivada).subs(x, valorAevaluar)
    print("\nResultado = ", resultado)
elif decisionDerivada == 2:
    valorAevaluar = int(input("\nvalor a evaluar en la 2da derivada: "))
    resultado = sympy.sympify(derivada2).subs(x, valorAevaluar)
    print("\nResultado = ", resultado)
elif decisionDerivada == 3:
    valorAevaluar = int(input("\nvalor a evaluar en la 3ra derivada: "))
    resultado = sympy.sympify(derivada3).subs(x, valorAevaluar)
    print("\nResultado = ", resultado)
elif decisionDerivada == 4:
    valorAevaluar = int(input("\nvalor a evaluar en la 4ta derivada: "))
    resultado = sympy.sympify(derivada4).subs(x, valorAevaluar)
    print("\nResultado = ", resultado)
else :
    print("Error, favor solo ingresar alguna de las 4 primeras derivadas")
    sys.exit()
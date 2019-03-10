import sympy 
from sympy.parsing.sympy_parser import parse_expr
import numpy as np 
import matplotlib.pyplot as plt
import math

#   METODO DE BUSQUEDAS INCREMENTALES
#fx = Function introduce by the user
#a = First value of the interval
#b = Last value of the interval
#delta = cada incremento en la busqueda
#fa = funcion evaluada en a
#fb = funcion evaluada en b

print("\nIncremental Search Method\n")

x = sympy.symbols('x')  
fx = parse_expr(input("Introduce the function \n> "))
    
a = int(input("Introduce the first interval value (a) \n> "))
b = int(input("Introduce the last interval value (b) \n> "))
delta = float(input("Introduce the Delta wanted \n> "))

fa = sympy.sympify(fx).subs(x, a)
fb = sympy.sympify(fx).subs(x, b)

if fa*fb > 0:
    print("\n In the interval [%d,%d] There is no a root" % (a,b))

if fb == 0:
    print('\n\n %d Is a root because f(%d) is equal to %f\n\n' % (b,b,fb))
else:
    Xi = a + delta
    fxi = fx.subs(x, Xi)

while fa * fxi > 0 and a < b:
    a = Xi
    fa = fxi
    Xi = a + delta
    fxi = fx.subs(x, Xi)

    if fxi == 0:
        print('\n\n %f Is a root \n\n' % (Xi))
    elif fa * fxi < 0:
        print('\n In the inverval [%f,%f] a root is found.     \n' % (a, Xi))


#       METODO DE BISECCION

print("\nBisection Method\n")

tol = float(input("Introduce the tolerance (tol) \n> "))
iterations = 0
if fa*fb > 0:
    #end function, no root.
    print("No root found.")
else:
    print('\n{:^10}{:^10}{:^10}{:^10}'.format('iterations', 'a', 'b', 'mid point'))
    while (b - a)/2.0 > tol:
        iterations = iterations+1
        xa = (a + b)/2.0
        fxa = sympy.sympify(fx).subs(x, xa)
        if fxa == 0:
            answer = xa            
            print("Answer:", answer)
            break
        elif fa*fxa < 0: # Increasing but below 0 case
            b = xa
        else:
            a = xa
    print('\n{:^10}{:^10.5f}{:^10.5f}{:^10.5f}'.format(iterations, float(a), float(b), float(xa)))
    answer = xa
    print("\nAnswer: ", answer)
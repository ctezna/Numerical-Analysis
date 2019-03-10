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

#Programa principal
#xi = a
#xs = b

fa = sympy.sympify(fx).subs(x, a)

error = float((input('Introduce the error \n> ')))
xa = (a+Xi)/2.00000000
fxa = sympy.sympify(fx).subs(x, xa)
iterations = 0
print('{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}'.format('iterations','a','Xi','xa','sign','change','error'))

while abs(fxa) > error:
      iterations = iterations+1
      xa = (a+Xi)/2.0
      if (fa*fxa) < 0:
          b = xa
          signo = "negative"
          limite = "higher"
          #print(" The root found by the bisection method is: %f" % (xa))         
      else:
          a = xa
          signo = "positive"
          limite = "lower"   
          #print(" The root found by the bisection method is: %f" % (xa))
      print('{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10}{:^10}{:^10.4f}'.format(iterations,float(a),float(Xi),float(xa),signo,limite,fxa))
      if (a == Xi):
        break

print(" The root found by the bisection method is: %f \n" % (xa))

print(" \nEnd of the program.")

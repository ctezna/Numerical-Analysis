from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import pandas as pd
import numpy as np
import sympy
import math


def f(x):
    return math.exp(-x+1) - x**2 + 4*x + (7*(math.cos(x**2 - 4)**2)) -7
    #return math.log(math.sin(x)**2 + 1) - (1/2)


def f_1(x):
    return 3*(x**2) - 2*x + 2*sin(x-1) * cos(x-1) -1


def f_2(x):
    return 6*x + 2*cos(2*(x-1)) - 2


def x_future_multiple_roots(f_x, f_x_1, f_x_2, x_n):
    return float(x_n - ((f_x * f_x_1) / (f_x_1**2 - (f_x * f_x_2))))


def x_future_newton(f_x, f_x_1, x_n):
    return (x_n - (f_x/f_x_1))


def x_future_secante(x_past, x_n):
    f_x = f(x_n)
    f_x_past = f(x_past)
    delta_x = x_n - x_past
    return (x_n - ((f_x * delta_x)/(f_x - f_x_past))) 


def relative_err(x, x_n):
    return abs((x_n - x) / x_n)


def absolute_err(x, x_n):
    return abs(x_n - x)


def multiple_roots_method(x_n, tol, f, f_derivate_1, f_derivate_2):   
    x = symbols('x', real=True)
    tol = float(tol)
    x_n = float(x_n)
    f_x = sympify(f).subs(x, x_n)
    f_x_1 = sympify(f_derivate_1).subs(x, x_n)
    f_x_2 = sympify(f_derivate_2).subs(x, x_n)
    data = {"N": [0], "Xn": [x_n], "f(x)": [f_x], "f(x)^1": [f_x_1], "f(x)^2": [f_x_2], "ER": [0], "EA": [0]}
    rel_err = 100000
    cont = 1

    while f(x_n) != 0 and rel_err > tol:
        x_past = x_n
        x_n = x_future_multiple_roots(f_x, f_x_1, f_x_2, x_n)
        f_x = sympify(f).subs(x, x_n)
        f_x_1 = sympify(f_derivate_1).subs(x, x_n)
        f_x_2 = sympify(f_derivate_2).subs(x, x_n)
        abs_err = absolute_err(x_past, x_n)
        rel_err = relative_err(x_past, x_n)

        data['N'].append(count)
        data["Xn"].append(x_n)
        data["f(x)"].append(f_x)
        data["f(x)^1"].append(f_x_1)
        data["f(x)^2"].append(f_x_2)
        data["ER"].append(rel_err)
        data["EA"].append(abs_err)
        count += 1

    return data

def newton_method(x_n, tol, n, f, f_derivate_1):
    message = ""
    print("\n NEWTON")
    tol = float(tol)
    x_n = float(x_n)
    n = int(n)

    if tol < 0  or x_n <= 0 or n < 0:
        message += "--- Please check your values, something is wrong"
        data ={}
        return message, data


    x = symbols('x', real=True)
    f = sympify(f)
    f_x = f.subs(x, x_n)
    f_x_1 = sympify(f_derivate_1).subs(x, x_n)
    data = {"N": [0], "Xn": [round(x_n,4)], "f(x)": [round(f_x,4)], "f(x)^1": [round(f_x_1,4)], "ER": [0], "EA": [0]}
    rel_err = 10000
    count = 1
    
    while f.subs(x, x_n) != 0 and count < n and rel_err > tol:
        x_past = x_n
        x_n = x_future_newton(f_x, f_x_1, x_n) #xn+1
        f_x = sympify(f).subs(x, x_n)
        f_x_1 = sympify(f_derivate_1).subs(x, x_n)
        abs_err = absolute_err(x_past, x_n)
        rel_err = relative_err(x_past, x_n)
        data["Xn"].append(round(x_n,4))
        data["f(x)"].append(round(f_x,4))
        data["f(x)^1"].append(round(f_x_1,4))
        err_round_rel = '%.2E' % Decimal(str(rel_err))
        err_round_abs = '%.2E' % Decimal(str(abs_err))
        data["ER"].append(err_round_rel)
        data["EA"].append(err_round_abs)
        data['N'].append(count)
        count += 1

    return message, data



def secante(x_0, x_1, tol, n, f):
    print("\n SECANTE")
    x_0 = float(x_0)
    x_1 = float(x_1)
    tol = float(tol)
    n = float(n)
    x = symbols('x', real=True)
    f_x_0 = sympify(f).subs(x, x_0)
    f_x_1 = sympify(f).subs(x, x_1)
    data = {"N": [], "Xn": [x_0, x_1], "f(x)": [f_x_0, f_x_1], "ER": [0,0], "EA": [0,0]}
    rel_err = 100000
    count = 1
    while sympify(f).subs(x, x_1) != 0 and count < n and rel_err > tol:
        x_new = x_future_secante(x_0, x_1) #xn+1
        x_0 = x_1
        x_1 = x_new
        f_x = sympify(f).subs(x, x_1)
        abs_err = absolute_err(x_0, x_1)
        rel_err = relative_err(x_0, x_1)
        data["N"].append(count)
        data["Xn"].append(x_1)
        data["f(x)"].append(f_x)
        data["ER"].append(rel_err)
        data["EA"].append(abs_err)
        count += 1
        print("iteracion:",count,"valor ampliado xi:",x_1)


    return data

tol = 1e-7
xn = -0.5
n = 100
#multiple_roots(xn, tol)
#newton(xn, tol, n)
#ecante(0, 3, tol, n)
#print (x_future_multiple_roots(0.001208993, -1*(0.054696496), 1.670346083, 0.5))
#print(f(xn))

# un numero a la -10 YA ES NAN EN CALIPSO
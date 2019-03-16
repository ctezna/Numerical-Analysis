from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import pandas as pd
import numpy as np
import sympy
import math


def f(x):
    return x**4 - 18*x**2 + 81


def f_1(x):
    return 4*x**3 - 36*x 


def f_2(x):
    return 12*x**2 - 36


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


def multiple_roots(x_n, tol):   
    f_x = f(x_n)
    f_x_1 = f_1(x_n)
    f_x_2 = f_2(x_n)
    data = {"Xn": [x_n], "f(x)": [f_x], "f(x)^1": [f_x_1], "f(x)^2": [f_x_2], "ER": [0], "EA": [0]}
    rel_err = 100000

    while f(x_n) != 0 and rel_err > tol:
        x_past = x_n
        x_n = x_future_multiple_roots(f_x, f_x_1, f_x_2, x_n)
        f_x = f(x_n)
        f_x_1 = f_1(x_n)
        f_x_2 = f_2(x_n)
        abs_err = absolute_err(x_past, x_n)
        rel_err = relative_err(x_past, x_n)
        data["Xn"].append(x_n)
        data["f(x)"].append(f_x)
        data["f(x)^1"].append(f_x_1)
        data["f(x)^2"].append(f_x_2)
        data["ER"].append(rel_err)
        data["EA"].append(abs_err)

    print (pd.DataFrame(data=data))


def newton(x_n, tol, n):
    f_x = f(x_n)
    f_x_1 = f_1(x_n)
    data = {"Xn": [x_n], "f(x)": [f_x], "f(x)^1": [f_x_1], "ER": [0], "EA": [0]}
    rel_err = 10000
    count = 1

    while f(x_n) != 0 and count < n and rel_err > tol:
        x_past = x_n
        x_n = x_future_newton(f_x, f_x_1, x_n)
        f_x = f(x_n)
        f_x_1 = f_1(x_n)
        abs_err = absolute_err(x_past, x_n)
        rel_err = relative_err(x_past, x_n)
        data["Xn"].append(x_n)
        data["f(x)"].append(f_x)
        data["f(x)^1"].append(f_x_1)
        data["ER"].append(rel_err)
        data["EA"].append(abs_err)
        count += 1

    print (pd.DataFrame(data=data))


def secante(x_0, x_1, tol, n):
    f_x_0 = f(x_0)
    f_x_1 = f(x_1)
    data = {"Xn": [x_0, x_1], "f(x)": [f_x_0, f_x_1], "ER": [0,0], "EA": [0,0]}
    rel_err = 100000
    count = 1

    while f(x_1) != 0 and count < n and rel_err > tol:
        x_new = x_future_secante(x_0, x_1)
        x_0 = x_1
        x_1 = x_new
        f_x = f(x_1)
        abs_err = absolute_err(x_0, x_1)
        rel_err = relative_err(x_0, x_1)
        data["Xn"].append(x_1)
        data["f(x)"].append(f_x)
        data["ER"].append(rel_err)
        data["EA"].append(abs_err)
        count += 1

    print(pd.DataFrame(data=data))

tol = 0.5e-8
xn = -2.5
n = 10
multiple_roots(xn, tol)
#newton(xn, tol, n)
#secante(1.3, 1.4, tol, n)
#print (x_future_multiple_roots(0.001208993, -1*(0.054696496), 1.670346083, 0.5))
#print(f(xn))

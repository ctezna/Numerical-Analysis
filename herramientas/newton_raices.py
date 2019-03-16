from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import pandas as pd
import numpy as np
import sympy
import math


def f(x):
    return x**3 + 4*x**2 - 10


def f_1(x):
    return 3*x**2 + 8*x


def f_2(x):
    return 12*x**2 - 36 


def x_future_multiple_roots(f_x, f_x_1, f_x_2, x_n):
    return float(x_n - ((f_x * f_x_1) / (f_x_1**2 - (f_x * f_x_2))))


def x_future_newton(f_x, f_x_1, x_n):
    return (x_n - (f_x/f_x_1))


def absolute_error(x, x_n):
    return abs((x_n - x) / x_n)


def relative_err(x, x_n):
    return abs(x_n - x)


def multiple_roots(x_n, tol):   
    f_x = f(x_n)
    f_x_1 = f_1(x_n)
    f_x_2 = f_2(x_n)
    data = {"Xn": [x_n], "f(x)": [f_x], "f(x)^1": [f_x_1], "f(x)^2": [f_x_2], "ER": [0], "EA": [0]}
    abs_err = 100000

    while f(x_n) != 0 and abs_err > tol:
        x_past = x_n
        x_n = x_future_multiple_roots(f_x, f_x_1, f_x_2, x_n)
        f_x = f(x_n)
        f_x_1 = f_1(x_n)
        f_x_2 = f_2(x_n)
        abs_err = absolute_error(x_past, x_n)
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
    abs_err = 10000
    count = 1

    while f(x_n) != 0 and count < n:
        x_past = x_n
        x_n = x_future_newton(f_x, f_x_1, x_n)
        f_x = f(x_n)
        f_x_1 = f_1(x_n)
        abs_err = absolute_error(x_past, x_n)
        rel_err = relative_err(x_past, x_n)
        data["Xn"].append(x_n)
        data["f(x)"].append(f_x)
        data["f(x)^1"].append(f_x_1)
        data["ER"].append(rel_err)
        data["EA"].append(abs_err)
        count += 1

    print (pd.DataFrame(data=data))



tol = 0.5e-8
xn = 1.5
n = 10
#multiple_roots(xn, tol)
newton(xn, tol, n)

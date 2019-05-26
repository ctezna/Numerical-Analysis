import pandas as pd
import math
import numpy as np

# Fixed Point Method
# g(x) evaluated in every point of [a,b] should be within [a,b]
# abs(g'(a,b)) <= k < 1


def f(x):
    return math.exp(x+1) - 7*x**2 -4 *x+2


def g(x):
    return math.log(7*x**2 + 4*x -2) -1


def absolute_err(current_x, previous_x):
    return abs(float(current_x - previous_x))


def relative_err(current_x, previous_x):
    return abs(float(((current_x - previous_x) / current_x)))


def get_data(g, f, abs_err, rel_err):
    data["g(x)"].append(g)
    data["f(x)"].append(f)
    data["ER"].append(rel_err)
    data["EA"].append(abs_err)


def fixed_point(n, x0, tol):
    g_value = g(x0)
    abs_err = absolute_err(g_value, x0)
    count = 0
    while (abs_err > tol and count < n):
        g_value = g(x0)
        f_value = f(g_value)
        abs_err = absolute_err(g_value, x0)
        rel_err = relative_err(g_value, x0)
        get_data(g_value, f_value, abs_err, rel_err)
        x0 = g_value
        count += 1

    return data


def show_data(data):
    return pd.DataFrame(data=data, dtype=np.float64)


x0 = 3.5
n = 1000
tol = 1e-7
data = {"g(x)":[x0], "f(x)":[f(x0)], "ER":[0], "EA":[0]}
data = fixed_point(n, float(x0),tol)
print (show_data(data))

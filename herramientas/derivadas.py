from sympy import *
from scipy.misc import derivative
import sympy as sy
import scipy
from sympy.functions import *
import matplotlib.pyplot as plt
import numpy as np
import math
from sympy.abc import x

x = Symbol('x')
f = exp(2*x)-cos(x)



derivada = f.diff(x)
print(derivada)


#f = lambda x: 2*x**3
#print(derivative(f, 1.0, dx=1e-6))

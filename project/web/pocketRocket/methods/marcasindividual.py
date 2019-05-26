import sys
import numpy as npy

#DEBE SER CUADRADA!!
K = [[0, 2, 3], [7, -1, 20], [1, -14, 8]] 
s = [-1,0,1]  


print ("Solucion: ", npy.linalg.solve(K,s))
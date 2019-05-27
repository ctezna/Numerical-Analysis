import sys
import numpy as npy

def eliminacion(A,b):
    b = [float(x) for x in b]
    n = len(A)
    Ab = forma_matriz_aumentada(A,b)
    print (Ab)
    for k in range(1,n):
        print("Etapa ",k)
        for i in range(k,n):
            multiplicador = Ab[i][k-1]/float(Ab[k-1][k-1])
            for j in range(k,n+2):
                Ab[i][j-1] = Ab[i][j-1] - multiplicador * Ab[k-1][j-1]
        #print ("Matriz aumentada \n",npy.array(Ab))
    return Ab

def forma_matriz_aumentada(A,b):
    new_A = A.tolist()
    for i in range(len(new_A)):
        new_A[i].append(b[i])

    return new_A


#A = [[20, -1, 3,4], [6, 23, 4,3], [7, 21, 46,9],[-3,-9,12,38]] 
#b = [30,-10,20,-14] 
#eliminacion(A,b)

import sys
import numpy as npy

def eliminacion(A,b):
    message = ""
    Ab = forma_matriz_aumentada(A,b)
    etapas = []
    matriz_lista = []

    if not is_square(A.tolist()):
        message += "Should be a cuadratic Matrix"
        return {'etapas':etapas, 'matrix': matriz_lista}, message

    if npy.linalg.det(A) == 0.0:
        message += "Determinant = 0"
        return {'etapas':etapas, 'matrix': matriz_lista}, message

    b = [float(x) for x in b]
    n = len(A)
    for k in range(1,n):
        print("Etapa ",k)
        etapas.append(k)
        for i in range(k,n):
            multiplicador = Ab[i][k-1]/float(Ab[k-1][k-1])
            for j in range(k,n+2):
                Ab[i][j-1] = Ab[i][j-1] - multiplicador * Ab[k-1][j-1]
        matriz_lista.append(Ab)
        print ("Matriz aumentada \n",npy.array(Ab))

    return {'etapas':etapas, 'matrix': matriz_lista}, sustitucion_regresiva(Ab)


def forma_matriz_aumentada(A,b):
    new_A = A.tolist()
    for i in range(len(new_A)):
        new_A[i].append(b[i])

    return new_A


def sustitucion_regresiva(Ab):
    print(Ab)
    n = len(Ab)
    x = npy.zeros(n)
    x[n-1] = Ab[n-1][n]/float(Ab[n-1][n-1])
    for i in range(n,0,-1):
        sumatoria = 0
        for p in range(i+1,n+1):
            sumatoria += Ab[i-1][p-1]*x[p-1]
            x[i-1] = (Ab[i-1][n]-sumatoria)/float(Ab[i-1][i-1])
    return x


def is_square (A):
    return (all (len (row) == len (A) for row in A))

#A = [[20, -1, 3,4], [6, 23, 4,3], [7, 21, 46,9],[-3,-9,12,38]] 
#b = [30,-10,20,-14] 
#eliminacion(A,b)

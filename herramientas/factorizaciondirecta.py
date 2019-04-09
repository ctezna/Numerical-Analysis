from math import sqrt
import numpy as np

#                   PYTHON 3.7 !!!

def cholesky(A,n):
    L,U = inicializa(n,2)

    for k in range(n):
        suma1 = 0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        L[k][k] = sqrt(A[k][k]-suma1)
        U[k][k] = L[k][k]
        for i in range(k,n):
            suma2 = 0
            for p in range(k):
                suma2+=L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/float(U[k][k])
        for j in range(k+1,n):
            suma3 = 0
            for p in range(k):
                suma3+= L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/float(L[k][k])
        print("\nEtapa ",  k, ":" )
        print("\nMatriz L")
        print(L)
        print("\nMatriz U")
        print(U)
    print ("\n\n\n Prueba: (analiza con la matriz ingresada)\n", np.dot(L,U))
    return L,U


def crout(A,n):
    L,U = inicializa(n,1)

    for k in range(n):
        suma1 = 0.0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        L[k][k] = A[k][k] - suma1
        for i in range(k+1,n):
            suma2 = 0.0
            for p in range(k):
                suma2 += L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/float(U[k][k])
        for j in range(k+1,n):
            suma3 = 0.0
            for p in range(k):
                suma3 += L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/float(L[k][k])
        print("\nEtapa ",  k )
        print("\nL:\n")
        print(L)
        print("\nU:\n")
        print(U)#imprimir L  U y k etapa
    print ("\n\n\n Prueba: (analiza con la matriz ingresada)\n", np.dot(L,U))
    return L,U

def doolittle(A,n):
    L,U = inicializa(n,0)
    for k in range(n):
        suma1 = 0.0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        U[k][k] = A[k][k]-suma1
        for i in range(k+1,n):
            suma2 = 0.0
            for p in range(k):
                suma2 += L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/float(U[k][k])
        for j in range(k+1,n):
            suma3 = 0.0
            for p in range(k):
                suma3 += L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/float(L[k][k])
        print("\nEtapa ",  k )
        print("\nL:\n")
        print(L)
        print("\nU:\n")
        print(U)#imprimir L  U y k etapa
    print ("\n\n\n Prueba: (analiza con la matriz ingresada)\n", np.dot(L,U))
    return L,U
#Doolittle == 0, Crout == 1, Cholesky == 2
def inicializa(n,metodo):
    L , U = [] , []
    if metodo == 0:
        L = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
        U = [[0 for j in range(n)] for i in range(n)]
    elif metodo == 1:
        L = [[0 for j in range(n)] for i in range(n)]
        U = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
    elif metodo == 2:
        L = [[0 for j in range(n)] for i in range(n)]
        U = [[0 for j in range(n)] for i in range(n)]
    return L , U


#       PYTHON 3.7 !!!

# Requisitos para cada metodo
#cholesky(A,n)
#doolittle(A,n)

# n es el orden de la matriz !!!

#K = [[4,-2,1],[20,-7,12],[-8,13,17]]
K = [[3,4,-2],[4,8,-2],[-2,-2,4],[-2,-2,4]]
s = [-1,0,1]  
n = 3


#crout(K,n)
#doolittle(K,n)
cholesky(K,n)
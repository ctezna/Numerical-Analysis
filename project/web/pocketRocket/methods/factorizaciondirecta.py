from cmath import sqrt
import numpy as np

#                   PYTHON 3.7 !!!

def cholesky(A,n, b):
    message = ""
    data = {'etapas': [], 'L': [], 'U':[]}
    L,U = inicializa(n,2)

    if not is_square(A.tolist()):
        message += "Should be a cuadratic Matrix"
        return [], message

    if np.linalg.det(A) == 0.0:
        message += "Determinant = 0"
        return [], message
     

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
            L[i][k] = (A[i][k]-suma2)/(U[k][k])
        for j in range(k+1,n):
            suma3 = 0
            for p in range(k):
                suma3+= L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/(L[k][k])
        print("\nEtapa ",  k, ":" )
        data['etapas'].append(k)
        print("\nMatriz L")
        print(L)
        data['L'].append(L)
        print("\nMatriz U")
        data['U'].append(U)
        print(U)
    
    #m = forma_matriz_aumentada(U, [float(x) for x in b])
    #message = sustitucion_regresiva(m)
    #print ("\n\n\n Prueba: (analiza con la matriz ingresada)\n", np.dot(L,U))
    return data, message


def crout_method(A,n,b):
    data = {'etapas': [], 'L': [], 'U':[]}
    L,U = inicializa(n,1)
     
    if not is_square(A.tolist()):
        message += "Should be a cuadratic Matrix"
        return [], message

    if np.linalg.det(A) == 0.0:
        message += "Determinant = 0"
        return [], message

    for k in range(n):
        data['etapas'].append(k)
        suma1 = 0.0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        L[k][k] = A[k][k] - suma1
        for i in range(k+1,n):
            suma2 = 0.0
            for p in range(k):
                suma2 += L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/(U[k][k])
        for j in range(k+1,n):
            suma3 = 0.0
            for p in range(k):
                suma3 += L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/(L[k][k])

        data['L'].append(L)
        data['U'].append(U)

    #m = forma_matriz_aumentada(U, [float(x) for x in b])
    #message = sustitucion_regresiva(m)

    return data, message


def doolittle_method(A,n, b):
    data = {'etapas': [], 'L': [], 'U':[]}
    L,U = inicializa(n,0)
     
    if not is_square(A.tolist()):
        message += "Should be a cuadratic Matrix"
        return [], message

    if np.linalg.det(A) == 0.0:
        message += "Determinant = 0"
        return [], message

    for k in range(n):
        suma1 = 0.0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]

        U[k][k] = A[k][k]-suma1
        for i in range(k+1,n):
            suma2 = 0.0
            for p in range(k):
                suma2 += L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/(U[k][k])
        for j in range(k+1,n):
            suma3 = 0.0
            for p in range(k):
                suma3 += L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/(L[k][k])
        print("\nEtapa ",  k )
        data['etapas'].append(k)
        print("\nL:\n")
        print(L)
        print("\nU:\n")
        print(U)#imprimir L  U y k etapa
        data['L'].append(L)
        data['U'].append(U)

    #print ("\n\n\n Prueba: (analiza con la matriz ingresada)\n", np.dot(L,U))
    #m = forma_matriz_aumentada(U, [float(x) for x in b])
    #message = sustitucion_regresiva(m)

    return data, message

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
    return L,U


def sustitucion_regresiva(Ab):
    print(Ab)
    n = len(Ab)
    x = np.zeros(n)
    x[n-1] = Ab[n-1][n]/float(Ab[n-1][n-1])
    for i in range(n,0,-1):
        sumatoria = 0
        for p in range(i+1,n+1):
            sumatoria += Ab[i-1][p-1]*x[p-1]
            x[i-1] = (Ab[i-1][n]-sumatoria)/float(Ab[i-1][i-1])
    return x


def is_square (A):
    return (all (len (row) == len (A) for row in A))


def forma_matriz_aumentada(A,b):
    new_A = A
    for i in range(len(new_A)):
        new_A[i].append(b[i])

    return new_A

#       PYTHON 3.7 !!!

# Requisitos para cada metodo
#cholesky(A,n)
#doolittle(A,n)

# n es el orden de la matriz !!!

#K = [[4,-2,1],[20,-7,12],[-8,13,17]]
K = [[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]]
#s = [-1,0,1]  
n = 4


#crout(K,n)
#oolittle_method(K,n)
#cholesky(K,n)

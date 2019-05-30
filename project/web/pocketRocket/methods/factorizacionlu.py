import numpy as np

#                   PYTHON 3.7 !!!
#K = [[4,-2,1],[20,-7,12],[-8,13,17]]

def is_square (A):
    return (all (len (row) == len (A) for row in A))


def lu_simple_gauss(A, m, b):
    message = ""
    data = {'etapas': [], 'L': [], 'U':[]}

    if not is_square(A.tolist()):
        message += "Should be a cuadratic matrix"
        return [], message

    if np.linalg.det(A) == 0.0:
        message += "Determinant = 0"
        return {'etapas':etapas, 'matrix': matriz_lista}, message

    matriz = np.zeros([m,m])
    u = np.zeros([m,m])
    l = np.zeros([m,m])

    for r in range(0,m):
        #print(r)
        for c in range(0,m):
            matriz[r,c]=A[r,c]
            matriz[r,c]=float(A[r,c])
            u[r,c]=A[r,c]
    #operaciones para hacer ceros debajo de la diagonal principal

    for k in range (0,m):
        data['etapas'].append(k)
        for r in range(0,m):
            if (k == r):
                l[k,r]=1
            if (k<r):
                factor=(matriz[r,k]/matriz[k,k])
                l[r,k]=factor
                for c in range (0,m):
                    matriz[r,c]=matriz[r,c]-(factor*matriz[k,c])
                    u[r,c]=matriz[r,c]
        data['L'].append(l)
        data['U'].append(u)
        
    m = forma_matriz_aumentada(u, [float(x) for x in b])
    message = sustitucion_regresiva(m)
    return data, message
        

def sustitucion_regresiva(Ab):
    n = len(Ab)
    x = np.zeros(n)
    x[n-1] = Ab[n-1][n]/float(Ab[n-1][n-1])
    for i in range(n,0,-1):
        sumatoria = 0
        for p in range(i+1,n+1):
            sumatoria += Ab[i-1][p-1]*x[p-1]
            x[i-1] = (Ab[i-1][n]-sumatoria)/float(Ab[i-1][i-1])
    return x


def forma_matriz_aumentada(A,b):
    new_A = A.tolist()
    for i in range(len(new_A)):
        new_A[i].append(b[i])

    return new_A
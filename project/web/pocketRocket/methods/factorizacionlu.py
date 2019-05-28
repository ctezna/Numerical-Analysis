import numpy as np

#                   PYTHON 3.7 !!!
#K = [[4,-2,1],[20,-7,12],[-8,13,17]]

def lu_simple_gauss(A, m):
    data = {'etapas': [], 'L': [], 'U':[]}
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
        
    return data    
        



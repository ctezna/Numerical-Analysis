import sys
import numpy as npy

def forma_matriz_aumentada(A,b):
   for i in range(len(A)):
       A[i].append(b[i])
   return A


def pivoteo_total(Ab,k,marcas,n):
    message = ""
    #inicializar marcas
    mayor = 0
    fila_mayor = k
    columna_mayor = k
    for r in range(k,n):
        for s in range(k,n):
            if abs(Ab[r][s]) > mayor:
                mayor = abs(Ab[r][s])
                fila_mayor = r
                columna_mayor = s
    if mayor == 0:
        message += "Not unique solution"
        return Ab, marcas, message
    else:
        if fila_mayor != k:
            Ab[fila_mayor],Ab[k] = Ab[k],Ab[fila_mayor]
        if columna_mayor != k:
            for row in Ab:
                row[k],row[columna_mayor] = row[columna_mayor],row[k]
            marcas[k],marcas[columna_mayor] = marcas[columna_mayor],marcas[k]
    return Ab,marcas,""

def eliminacion_gaussiana_pivoteo(A,b,metodo):
    matriz_list = []
    message = ""
    etapas = []
    A = A.tolist()
    b = [int(x) for x in b]
    Ab = forma_matriz_aumentada(A,b)
    n = len(A)
    marcas = npy.arange(n)

    if not is_square(A):
        message += "Should be a cuadratic matrix"
        return {"etapas": etapas, "matriz": Ab}, message, []

    if npy.linalg.det(A) == 0.0:
        message += "Determinant = 0"
        return {'etapas':etapas, 'matrix': matriz_lista}, message

    for k in range(n-1):
        print ("Etapa ",k)
        etapas.append(k)
        Ab,marcas,message = pivoteo_total(Ab,k,marcas,n)   
        if message:
            return {"etapas": etapas, "matriz": Ab}, message, []

        for i in range(k+1,n):
            if Ab[k][k]:
                multiplicador = Ab[i][k]/float(Ab[k][k])
            else:
                # raise Exception("Error, división por 0")
                message += "Error division 0"
                return {"etapas": etapas, "matriz": Ab}, message, []
                sys.exit()
                print ("Error, división por 0")
            for j in range(k,n+1):
                Ab[i][j] = Ab[i][j] - multiplicador * Ab[k][j]
        print ("Matriz aumentada \n",npy.array(Ab))
        matriz_list.append(Ab)
    if metodo ==  1:
        return {"etapas": etapas, "matriz": matriz_list}, message, sustitucion_regresiva(Ab)
    elif metodo == 2:
        sol = Ab
        return {'Ab': sol, 'marcas': marcas}


def sustitucion_regresiva(Ab):
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
#B = [30,-10,20,-14]  
#eliminacion_gaussiana_pivoteo(A,b,2)

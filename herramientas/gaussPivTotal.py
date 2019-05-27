import sys
import numpy as npy

def forma_matriz_aumentada(A,b):
   for i in range(len(A)):
       A[i].append(b[i])
   return A


def pivoteo_total(Ab,k,marcas,n):
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
        return "El sistema no tiene solución única"
    else:
        if fila_mayor != k:
            Ab[fila_mayor],Ab[k] = Ab[k],Ab[fila_mayor]
        if columna_mayor != k:
            for row in Ab:
                row[k],row[columna_mayor] = row[columna_mayor],row[k]
            marcas[k],marcas[columna_mayor] = marcas[columna_mayor],marcas[k]
    return Ab,marcas

def eliminacion_gaussiana_pivoteo(A,b,metodo):
    n = len(A)
    marcas = npy.arange(n)
    Ab = forma_matriz_aumentada(A,b)
    for k in range(n-1):
        print ("Etapa ",k)
        Ab,marcas = pivoteo_total(Ab,k,marcas,n)    
        for i in range(k+1,n):
            if Ab[k][k]:
                multiplicador = Ab[i][k]/float(Ab[k][k])
            else:
                # raise Exception("Error, división por 0")
                sys.exit()
                print ("Error, división por 0")
            for j in range(k,n+1):
                Ab[i][j] = Ab[i][j] - multiplicador * Ab[k][j]
        print ("Matriz aumentada \n",npy.array(Ab))
    if metodo ==  1:
        return Ab
    elif metodo == 2:
        return Ab,marcas



A = [[20, -1, 3,4], [6, 23, 4,3], [7, 21, 46,9],[-3,-9,12,38]] 
B = [30,-10,20,-14]  
eliminacion_gaussiana_pivoteo(A,b,2)

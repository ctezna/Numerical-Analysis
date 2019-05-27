import sys
import numpy as npy

def eliminacion(A,b):
    n = len(A)
    Ab = forma_matriz_aumentada(A,b)
    for k in range(1,n):
        print("Etapa ",k)
        for i in range(k,n):
            multiplicador = Ab[i][k-1]/float(Ab[k-1][k-1])
            for j in range(k,n+2):
                Ab[i][j-1] = Ab[i][j-1] - multiplicador * Ab[k-1][j-1]
        print ("Matriz aumentada \n",npy.array(Ab))
    return Ab

def forma_matriz_aumentada(A,b):
   for i in range(len(A)):
       A[i].append(b[i])
   return A

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

def eliminacion_gaussiana_pivoteo(A,b,metodo):
    n = len(A)
    marcas = npy.arange(n)
    Ab = forma_matriz_aumentada(A,b)
    for k in range(n-1):
        print ("Etapa ",k)
        if metodo == 1:
            Ab = pivoteo_parcial(Ab,k,n)
        elif metodo == 2:
            Ab,marcas = pivoteo_total(Ab,k,marcas,n)
            print ("Marcas ",marcas)
        elif metodo == 3:
            s = []
            for i in range(len(A)):
                s.append(max(A[i]))
            print (s)
            Ab = pivoteo_escalonado(Ab,k,n,s)
        for i in range(k+1,n):
            if Ab[k][k]:
                multiplicador = Ab[i][k]/float(Ab[k][k])
                print ("multiplicador fila ",i," ",multiplicador)
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


def pivoteo_parcial(Ab,k,n):
    mayor =  abs(Ab[k][k])
    fila_mayor = k

    for s in range(k+1,n):
        if abs(Ab[s][k]) > mayor:
            mayor = abs(Ab[s][k])
            fila_mayor = s

    if mayor == 0:
        return "El sistema no tiene solucion unica"
    else:
        if fila_mayor != k:
            Ab = IntercambieFilas(Ab,fila_mayor,k)
        return Ab

# fila k = fila_mayor fila_mayor = k
def IntercambieFilas(Ab,fila_mayor,k):
    Ab[k], Ab[fila_mayor] = Ab[fila_mayor], Ab[k]
    return Ab


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


def pivoteo_escalonado(Ab,k, n, s):
    mayor = 0
    fila_mayor = k
    cocientes = []
    for i in range(k,n):
        cocientes.append(abs(Ab[i][k])/s[i])
    fila_mayor = max(range(len(cocientes)), key = lambda i: cocientes[i])
    mayor = cocientes[fila_mayor]
    if mayor == 0:
        print ("El sistema no tiene solucion unica")
    elif fila_mayor != k:
        Ab[k], Ab[fila_mayor] = Ab[fila_mayor], Ab[k]
        s[k],s[fila_mayor] = s[fila_mayor],s[k]
    return Ab



#Funciones:
#eliminacion
#eliminacion gaussiana con pivoteo
#pivoteo parcial
#pivoteo total
#pivoteo escalonado
#sustitución regresiva

#Metodos
#parcial = 1
#total = 2
#escalonado = 3
K = [[1, 0, 0], [1, 1, 1], [1, 2/3, 4/9]] 
s = [1,0,1/2]  

print(eliminacion_gaussiana_pivoteo(K,s,1))
#eliminacion(K,s)

#Ks = [[7, -1, 20, 0], [0, -13.85714286, 5.14285714, 1], [0, 0, 3.74226804, -0.8556701]] 
#sustitucion_regresiva(Ks)


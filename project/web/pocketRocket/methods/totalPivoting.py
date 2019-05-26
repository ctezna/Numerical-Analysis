import math
import numpy as np



'''a = [
        [14,6,-2,3,12],
        [3,15,2,-5,32],
        [-7,4,-23,2,-24],
        [1,-3,-2,16,14]
        ]'''


'''a = [
        [1,1/2,1/3,1],
        [1/2,1/3,1/4,0],
        [1/3,1/4,1/5,0],
        ]'''            
a = [
        [-7,2,-3,4,-12],
        [5,-1,14,-1,13],
        [1,9,-7,13,31],
        [-12,13,-8,-4,-32]
        ]

n = len(a)
marcas = [i for i in range(0,n)]


def intercambioDeFilas(filaMayor,k):
    for i in range(0,len(a)+1):
        aux = a[k][i]
        a[k][i] = a[filaMayor][i]
        a[filaMayor][i]= aux
    
def intercambioDeColumnas(columnaMayor,k):
    #print(marcas)
    aux = marcas[k]
    marcas[k] = marcas[columnaMayor]
    marcas[columnaMayor] = aux
    for j in range(0,len(a)):
        aux = a[j][k]
        a[j][k] = a[j][columnaMayor]
        a[j][columnaMayor] = aux
        



def pivoteoTotal(k):
    mayor = 0
    filaMayor = k
    columnaMayor = k
    for r in range(k,n):
        for s in range (k,n):
            if (math.fabs(a[r][s]) > mayor):
                mayor = math.fabs(a[r][s])
                filaMayor = r
                columnaMayor = s
        
    if(mayor == 0):
        print("division 0")
        return;
    else:
        if(filaMayor != k):
            intercambioDeFilas(filaMayor,k)
        if(columnaMayor != k):
            intercambioDeColumnas(columnaMayor,k)
            #intercambioDeMarcas()
    

def elimination():
    for k  in range(0,n-1):
        pivoteoTotal(k)
        for i  in range (k + 1, n):    
            multiplicador = a[i][k]/a[k][k]
            for j in range (k,n + 1):
                a[i][j] = a[i][j]-(multiplicador*a[k][j])
        

    return sustitucion()


def orderning(x):
    return [i for _,i in sorted(zip(marcas,x))]
        


def sustitucion():
    n = len(a) -1
    x = [i for i in range(n+1)]
    x[len(x)-1] = a[n][n+1]/a[n][n]
    
    
    for i in range(0,n+1):
        sumatoria = 0
        auxi = n - i 
        sumatoria = 0
        for p in range(auxi+1,n+1):
            sumatoria = sumatoria + a[auxi][p]*x[p]
        x[auxi]=(a[auxi][n+1]-sumatoria)/a[auxi][auxi]
    #print marcas
    #duda error numero proximo a cero
    marcas.reverse()
    x.reverse()
    x = orderning(x)
    for i in range(0,len(x)):
        if(math.fabs(x[i]) < 10**-15):
            x[i] = 0    
    return x
            



#elimination()
#for i in a:
#    print(i)
#intercambioDeFilas(0,2)


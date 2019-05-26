import numpy as np

#                   PYTHON 3.7 !!!
#K = [[4,-2,1],[20,-7,12],[-8,13,17]]

m = int(input("\nintroduce el orden de la matriz: "))
matriz = np.zeros([m,m])
u = np.zeros([m,m])
l = np.zeros([m,m])

for r in range(0,m):
    for c in range(0,m):
        matriz[r,c]=(input("Elemento a[" + str(r+1) + "," + str(c+1) + "]"))
        matriz[r,c]=float(matriz[r,c])
        u[r,c]=matriz[r,c]
#operaciones para hacer ceros debajo de la diagonal principal

for k in range (0,m):
    
    for r in range(0,m):
        if (k == r):
            l[k,r]=1
        if (k<r):
            factor=(matriz[r,k]/matriz[k,k])
            l[r,k]=factor
            for c in range (0,m):
                matriz[r,c]=matriz[r,c]-(factor*matriz[k,c])
                u[r,c]=matriz[r,c]
    print("\nEtapa ",  k, ":" )
    print("\nMatriz L")
    print(l)
    print("\nMatriz U")
    print(u)  
print ("\n\n\n Prueba: (analiza con la matriz ingresada)\n", np.dot(l,u))          
        



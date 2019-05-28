import math
import numpy as np

class totalPivoting():

    def __init__(self, a):
        self.a = a
        self.n = len(self.a)
        self.marcas = [i for i in range(0, self.n)]


    def inicializar_marcas(self):
        self.n = len(self.a)
        self.marcas = [i for i in range(0, self.n)]


    def intercambioDeFilas(self, filaMayor,k):
        for i in range(0,len(self.a)+1):
            aux = self.a[k][i]
            self.a[k][i] = self.a[filaMayor][i]
            self.a[filaMayor][i]= aux
    
    def intercambioDeColumnas(self, columnaMayor,k):
        #print(self.marcas)
        aux = self.marcas[k]
        self.marcas[k] = self.marcas[columnaMayor]
        self.marcas[columnaMayor] = aux
        for j in range(0,len(self.a)):
            aux = self.a[j][k]
            self.a[j][k] = self.a[j][columnaMayor]
            self.a[j][columnaMayor] = aux
        

    def pivoteoTotal(self, k):
        mayor = 0
        filaMayor = k
        columnaMayor = k
        for r in range(k,self.n):
            for s in range (k,self.n):
                if (math.fabs(self.a[r][s]) > mayor):
                    mayor = math.fabs(self.a[r][s])
                    filaMayor = r
                    columnaMayor = s
        
        if(mayor == 0):
            print("division 0")
            return;
        else:
            if(filaMayor != k):
                self.intercambioDeFilas(filaMayor,k)
            if(columnaMayor != k):
                self.intercambioDeColumnas(columnaMayor,k)
                #intercambioDeself.marcas()
    

    def elimination(self):
        self.a = self.a.tolist()
        for k  in range(0,self.n-1):
            self.pivoteoTotal(k)
            for i  in range (k + 1, self.n):    
                multiplicador = self.a[i][k]/self.a[k][k]
                for j in range (k,self.n + 1):
                    self.a[i][j] = self.a[i][j]-(multiplicador*self.a[k][j])
        

        return self.sustitucion()


    def orderning(self, x):
        return [i for _,i in sorted(zip(self.marcas,x))]
        


    def sustitucion(self):
        n = len(self.a) -1
        x = [i for i in range(n+1)]
        x[len(x)-1] = self.a[n][n+1]/self.a[n][n]
    
    
        for i in range(0,n+1):
            sumatoria = 0
            auxi = n - i 
            sumatoria = 0
            for p in range(auxi+1,n+1):
                sumatoria = sumatoria + self.a[auxi][p]*x[p]
            x[auxi]=(self.a[auxi][n+1]-sumatoria)/self.a[auxi][auxi]
    #print self.marcas
    #duda error numero proximo a cero
        self.marcas.reverse()
        x.reverse()
        x = self.orderning(x)
        for i in range(0,len(x)):
            if(math.fabs(x[i]) < 10**-15):
                x[i] = 0   

        return {'solution': x, 'matriz': self.a}
            



#elimination(a)
#for i in a:
#    print(i)
#intercambioDeFilas(0,2)


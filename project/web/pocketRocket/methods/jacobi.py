import math
import numpy as np


"""a = [[4, -1,   0,  3],
     [1, 15.5, 3,  8],
     [0, -1.3, -4, 1.1],
     [14, 5,   -2, 30]]
n = len(a)
initialValues = [0,0,0,0]
totalResult = [[] for y in range(len(initialValues))]
"""
class jacobiClass():

    def __init__(self, niter, tol, x0, a):
        self.message = ""
        self.niter = int(niter)
        self.tol = float(tol)
        self.x0 = [int(x) for x in x0]
        self.a = a.tolist()
        self.n = len(self.a)
        self.totalResult = [[] for y in range(len(self.x0))]


    def calculateNewJacobi(self, x0):
        relaxed = 1
        x = []
        for i in range(0,self.n):
            sum = 0
            for j in range(0,self.n):
                if(j != i):
                    sum = sum + self.a[i][j]*self.x0[j]
            value = (relaxed*((self.a[i][self.n-1] - sum)/self.a[i][i]))+(1-relaxed)*self.x0[i]
            x.append(value)
            self.totalResult[i].append(value)
        return x

    def norm(self, x):
        return max([math.fabs(x) for x in x])


    def minus(self, x1,x0):
        x = []
        for i in range(0,len(x1)):
            x.append(x1[i]-x0[i])
        return x


    def is_square (self, A):
        return (all (len (row) == len (A) for row in A))
    

    def jacobi_method(self):
        data = {'n': [], 'err': []}

        if not self.is_square(self.a):
            self.message += "Should be a cuadratic Matrix"
            return [], self.message

        if np.linalg.det(self.a) == 0.0:
            self.message += "Determinant = 0"
            return [], self.message

        for i in range(len(self.totalResult)):
            label = 'x%s' % str(i)
            data[label] = []
            
        major = []
        iters = []
        cont = 0
        dispersion = self.tol + 1
        major.append(0)
        iters.append(0)
        for i in range(0,len(self.x0)):
            self.totalResult[i].append(self.x0[i]) 
        while(dispersion > self.tol and cont < self.niter ):
            x1 = self.calculateNewJacobi(self.x0)
            dispersion = self.norm(self.minus(x1, self.x0)) 
            major.append("%e" % dispersion)
            self.x0 = x1
            cont = cont +1
            iters.append(cont)
        if (dispersion < self.tol):
            data['n'].append(iters)
            for i in range(0,len(self.totalResult)):
                label = 'x%s' % str(i)
                data[label].append(self.totalResult[i])
            data['err'].append(major)
        else:
            self.message += "Failed!"
            print("Failed!")

        return data, self.message

#instance = jacobi(100,10**-7,initialValues, a)
#print(instance.jacobi_method())
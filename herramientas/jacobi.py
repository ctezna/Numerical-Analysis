import math
from prettytable import PrettyTable

table = PrettyTable()

a = [[4, -1,   0,  3],
     [1, 15.5, 3,  8],
     [0, -1.3, -4, 1.1],
     [14, 5,   -2, 30]]
n = len(a)
iters = []
major = []
initialValues = [0,0,0,0]
totalResult = [[] for y in range(len(initialValues))]
relaxed = 1

def calculateNewJacobi(x0):
    x = []
    for i in range(0,n):
        sum = 0
        for j in range(0,n):
            if(j != i):
                sum = sum + a[i][j]*x0[j]
        value = (relaxed*((a[i][n-1] - sum)/a[i][i]))+(1-relaxed)*x0[i]
        x.append(value)
        totalResult[i].append(value)
    return x

def norm(x):
        return max([math.fabs(x) for x in x])

def minus(x1,x0):
    x = []
    for i in range(0,len(x1)):
        x.append(x1[i]-x0[i])
    return x
    
def jacobi(niter,tol,x0):
    cont = 0
    dispersion = tol + 1
    major.append(0)
    iters.append(0)
    for i in range(0,len(x0)):
        totalResult[i].append(x0[i]) 
    while(dispersion > tol and cont < niter ):
        x1 = calculateNewJacobi(x0)
        dispersion = norm (minus(x1, x0)) 
        major.append("%e" % dispersion)
        x0 = x1
        cont = cont +1
        iters.append(cont)
    if (dispersion < tol):
        table.add_column("n",iters)
        for i in range(0,len(totalResult)):
            table.add_column("x"+str(i),totalResult[i])
        table.add_column("major error",major)
        print(table)
    else:
        print("Failed!")

jacobi(100,10**-7,initialValues)
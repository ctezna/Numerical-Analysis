import sympy
import totalPivoting
x = sympy.Symbol('x')

xn =[1,3,4,5,7]
fxn =[4.31,1.5,3.2,2.6,1.8]


inequality =[]
functions =[]
result =[]
des = []

class splineQ():

    def __init__(self, xn, fxn):
        self.xn = [float(x) for x in xn]
        self.fxn = [float(x) for x in fxn]
        self.inequality = []
        self.functions = []
        self.result = []
        self.des = []
        self.createInequality()


    def createInequality(self):
        for i in range(0,len(self.xn)-1):
            if(i < len(self.xn)):
                self.inequality.append(((self.xn[i],self.fxn[i]),(self.xn[i+1],self.fxn[i+1])))
    
    
    def quadratic(self):
        superMatrix = [[0 for x in range(3*len(self.inequality)+1)] for y in range(3*len(self.inequality))] 
        n = len(superMatrix)
        j = 0
        z = 0
        for i in self.inequality:
            auxj = str(z-j)
            superMatrix[j][z] = i[0][0]**2
            superMatrix[j][z+1] = i[0][0]
            superMatrix[j][z+2] = 1
            superMatrix[j][n] = i[0][1]
            superMatrix[j+1][z] = i[1][0]**2
            superMatrix[j+1][z+1] = i[1][0]
            superMatrix[j+1][z+2] = 1
            superMatrix[j+1][n] = i[1][1]
            z += 3
            j += 2
        k = j
        z = 0
        for i in range(0,len(self.inequality)-1):
            superMatrix[k][z] = 2*self.inequality[i][1][0]
            superMatrix[k][z+1] = 1
            superMatrix[k][z+3] = -2*self.inequality[i+1][0][0]
            superMatrix[k][z+4] = -1
            superMatrix[k][n] = 0
            k += 1
            z += 3
        superMatrix[k][0] = 1
        totalPivoting.a = superMatrix
        totalPivoting.n = len(superMatrix)
        totalPivoting.marcas = [i for i in range(0,totalPivoting.n)]
        aux = totalPivoting.elimination()
        j = 0
        for i in range(0,len(inequality)):
            func = aux[j]*x**2+aux[j+1]*x + aux[j+2]
            print(str(self.inequality[i][0][0])+" <= x <= "+str(self.inequality[i][1][0]))
            print(func)
            j += 3
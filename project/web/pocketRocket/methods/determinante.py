import numpy

#"""
m = int(input('\nValor de m:'))
n = int(input('Valor de n:'))

matrix = numpy.zeros((m,n))
vector = numpy.zeros((n))
x = numpy.zeros((m))

print ('Introduce la matriz de coeficientes y el vector solución')

for r in range(0, m):
    for c in range(0, n):
        matrix[(r),(c)]=(input("Elemento a["+str(r+1)+","+str(c+1)+"] "))

#Codigo funcionando para matrices 3x3 - ingresada por el usuario
print ('\nmatriz ingresada: \n')
print(matrix)
print ('\nDeterminante de la matriz: ', numpy.linalg.det(matrix))

#"""

"""
#Codigo alternativo para matrices de orden nxn
matrixnn = [[0, 2, 3], [7, -1, 20], [1, -14, 8]] 
print ('\nmatriz ingresada: \n')
print(matrixnn)
print ('\nDeterminante de la matriz: ', numpy.linalg.det(matrixnn))
"""
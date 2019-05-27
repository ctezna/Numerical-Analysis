from math import fabs
def sor_method(A, b, tol, w):
	tol = float(tol)
	w = float(w)
	n = len(A)
	Xk = [0.0]*n
	sumation = 0.0
	data = {'Xk1': [], 'err': []}
	for i in range(n):
		if A[i][i] == 0:
			exit('Los elementos A[i][i] deben ser diferentes de 0')

	Xk1 = [b[i]/float(A[i][i]) for i in range(n)]
	minus = lambda x, y: [x[i]-y[i] for i in range(n)]

	for j in range(n):
	 	dominancia = 0.0
	 	for i in range(n):
	 		if j != i:
	 			dominancia += fabs(A[i][j])
	 	if A[i][i] < dominancia:
	 		exit('La matriz no converge')

	while (normaInfVector(minus(Xk1,Xk)) / float(normaInfVector(Xk1))) > tol:
		Xk[:] = Xk1[:]
		for i in range(n):
			sumation1 = sum(A[i][j]*Xk1[j] for j in range(i))
			sumation2 = sum(A[i][j]*Xk1[j] for j in range(i+1, n))
			err=(normaInfVector(minus(Xk1,Xk)) / float(normaInfVector(Xk1)))
			Xk1[i] = (float(w)/A[i][i])*(b[i] - sumation1 - sumation2) + (1-w)*Xk[i]
		data['Xk1'].append(Xk1)
		data['err'].append(err)

	return data


def normaInfVector(L):
	""" Calcula la norma infinita de un vector:
		||x|| = max {|xi|}, i = 0, 1, ... n.
	"""

	maximum = fabs(L[0])
	for i in range(1, len(L)):
		maximum = max(maximum, fabs(L[i]))
	return maximum	


#A = [[4, -1, 0, 3], [1, 15.5, 3, 8], [0, -1.3, -4, 1.1], [14, 5, -2, 30] ]
#b=[1,1,1,1]
#tol=0.000005
#w=0.7
#print(sor_method(A,b,tol,w))

import numpy as np

def is_square (A):
    return (all (len (row) == len (A) for row in A))


def gaussPivPar(A,b):
  message = ""
  matriz_list = []
  etapas  = []
  A = A.tolist()
  b = [int(x) for x in b]
  n = len(A)
  M = A

  if not is_square(A):
    message += "Should be a cuadratic matrix"
    return [], message


  if np.linalg.det(A) == 0.0:
    message += "Determinant = 0"
    return [], message

  i = 0
  for x in M:
   x.append(b[i])
   i += 1

  for k in range(n):
   print ("Iteracion: ", k)
   etapas.append(k)
   for i in range(k,n):
     if abs(M[i][k]) > abs(M[k][k]):
        M[k], M[i] = M[i],M[k]
     else:
        pass

   for row in M:
    print (type(row))
   for j in range(k+1,n):
       q = float(M[j][k]) / M[k][k]
       for m in range(k, n+1):
          M[j][m] -=  q * M[k][m]

  x = [0 for i in range(n)]

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-1,-1,-1):
    z = 0
    for j in range(i+1,n):
        z = z  + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]
  return {'solucion': x}

#A = [[20, -1, 3, 4], [6, 23, 4, 3], [7, 21, 46, 9], [-3, -9, 12, 38]]
#b = [30, -10, 20, -14]

#gaussPivPar(A,b)
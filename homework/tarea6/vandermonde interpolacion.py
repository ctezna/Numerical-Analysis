import numpy as np

x = np.array([-2,-1,0,1])
y = np.array([0,1,1,0])


print(np.vander(x))
print("\ndeterminante de la matriz: ", np.linalg.det(np.vander(x)))
print("\n")
#print(np.vander(y))
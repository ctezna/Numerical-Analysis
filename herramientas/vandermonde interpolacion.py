import numpy as np

x = np.array([-1,0,3,4])
y = np.array([15.5,3,8,1])


print(np.vander(x))
print("\ndeterminante de la matriz: ", np.linalg.det(np.vander(x)))
print("\n")
print(np.vander(y))

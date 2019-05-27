import numpy as np

def vandermorde_method(x,y):
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    det = np.linalg.det(np.vander(x))
    return {'determinante': det, 'x_vander': np.vander(x), 'y_vander':np.vander(y)}



import numpy as np

def vandermorde_method(x,y):
    message = ""
    x = [float(i) for i in x]
    y = [float(i) for i in y]

    if not valid_data(x):
        message += "Each x point must be different"
        return {}, message

    message = np.linalg.det(np.vander(x))
    return {'x_vander': np.vander(x), 'y_vander':np.vander(y)}, message


def valid_data(x_points):
    for i in x_points:
        count = x_points.count(i)

        if count >= 2:
            return False

    return True


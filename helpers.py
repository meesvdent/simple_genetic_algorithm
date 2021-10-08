import numpy as np

def flip_boolean(x, y):
    x = np.array(x)
    y = np.array(y)

    for i, b in enumerate(x):
        if y[i] == True:
            x[i] = not b

    return x



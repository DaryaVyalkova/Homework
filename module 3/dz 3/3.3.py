import numpy as np

X = np.array([
    [1, 1, 145],
    [1, 2, 163],
    [1, 3, 240],
    [1, 3, 350],
    [1, 4, 421],
    [1, 4, 397],
    [1, 5, 620]
])

Y = np.array([
    [80],
    [170],
    [100],
    [220],
    [200],
    [270],
    [500]
])

XTY = X.T.dot(Y)
XTX = X.T.dot(X)
w = np.linalg.inv(XTX).dot(XTY)
print(w)

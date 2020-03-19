import numpy as np
x0 = np.ones(10)
x1 = [64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.97, 59.3, 116.03]
x2 = [2, 3, 4,  2, 3, 4, 2, 4, 1, 3]
y = [62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84]
X = np.stack((x0, x1, x2), axis=0)
Y = np.vstack(y)
print(X)
print(Y)
X = np.mat(X)
W = ((X.T * X).I) * X.T * Y
print(W)
print(W.shape)
import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 3, 7])
Y = np.array([2, 6, 14])

w = 0.0
b = 0.0
lr = 0.01
iters = 1000


for i in range(iters):
    y_pred = w * X + b
    error = Y - y_pred

    w_grad = -2 * np.dot(X, error) / len(X)
    b_grad = -2 * np.sum(error) / len(X)

    w -= lr * w_grad
    b -= lr * b_grad

print(w, b)


plt.plot(X, Y, linestyle='--', color='green', alpha=0.5, label='data')
plt.plot(X, np.array(y_pred), linestyle='--',
         color='red', alpha=0.3, label='predictions')
plt.legend()
plt.grid(True)
plt.title('Comparing')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

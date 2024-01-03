import numpy as np
import matplotlib.pyplot as plt


X = np.random.normal(0, 1, 3000)
Y = np.random.normal(3, 4, 3000)

plt.scatter(X, Y, marker='>', s=2, color='purple', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Points')

plt.show()

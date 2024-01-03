import math
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return (math.sin(x) / math.factorial(abs(math.floor(x))))**(math.floor(x/math.pi))


x = np.linspace(-10, 11)
y = [func(i) for i in x]

plt.plot(x, y, linestyle='--', color='green', alpha=0.5)
plt.grid(True)
plt.title('Вот такая моя функция')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

import numpy as np
import matplotlib.pyplot as plt


data = np.random.normal(16, 2, 1000)
plt.hist(data, color='red', alpha=0.5)
plt.show()

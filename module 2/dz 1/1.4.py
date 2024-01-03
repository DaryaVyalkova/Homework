import numpy as np

mtx = np.array([np.arange(1, 11) for i in range(10)])
print(mtx)

column_sums = np.sum(mtx, axis=0)
print(column_sums)

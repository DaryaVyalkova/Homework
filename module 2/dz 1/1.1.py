import numpy as np


arr = np.random.randint(1, 11, size=100)
res = arr[arr > 7]

print(res)
print(f"{len(res)/len(arr)*100}%")

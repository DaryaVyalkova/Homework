import numpy as np

total = np.empty(1000)
for i in range(1000):
    arr = np.random.randint(1, 11, size=100)
    res = arr[arr > 7]
    total[i] = len(res)/len(arr)*100

print(f"{len(total[total == 20])} из 1000")

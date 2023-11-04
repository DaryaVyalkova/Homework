from functools import reduce
s = [1, 2, 3, 4, 5]
ans = reduce((lambda x, y: x if x > y else y), s)
print (ans)
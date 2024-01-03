s = [1, 12, 13, 15, 24, 26, 30]
ans = list(filter(lambda x: (x%12==0 or x%13==0), s))
print(ans)
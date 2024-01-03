s1 = [1, 2, 3, 4]
s2 = [5, 6, 7, 8, 9]

if len(s1) > len(s2):
    s1, s2 = s2, s1
mysum = list(map(lambda x, y: x + y, s1, s2[:len(s1)]))
mysum.extend(s2[len(s1):])

print(mysum)

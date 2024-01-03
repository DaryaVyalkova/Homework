cities=[]
num = int(input())
ans = 0
for i in range(num):
    cities.append(input())
for i in cities:
    if cities.count(i) != 1:
        ans += cities.count(i)
        cities.remove(i)
print (ans)
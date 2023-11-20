n = int(input("Введите 'n': "))
simples = []
c = 0

for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            c += 1
    if c == 0:
        simples.append(i)
    else:
        c = 0

print(*simples)

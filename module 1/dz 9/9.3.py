n = int(input("Введите 'n': "))
delimeters = []

for i in range(1, n+1):
    if n % i == 0:
        delimeters.append(i)

print(*delimeters)

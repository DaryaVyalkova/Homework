def NOK(a, b):
    c = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return c // (a + b)


a, b = map(int, input("Введите 'a' и 'b': ").split())
print(NOK(a, b))

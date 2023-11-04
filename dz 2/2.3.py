number1, number2 = map(int, input('Введите два числа через пробел: ').split())
if number1%2==0 and number2%2!=0:
    print('YES')
else:
    print('NO')
number1 = int(input('Введите число: '))
sum=0
while number1>0:
    number2 = number1%10
    sum += number2
    number1 = number1//10
print (sum)
s = list(map(int, input().split(' ')))
n = int(input())
s = [i**n for i in s]
print(s)
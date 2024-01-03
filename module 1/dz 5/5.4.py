s1 = input().split(' ')
s2 = input().split(' ')
s3 = input().split(' ')
all = set(s1+s2+s3)
ans = ''
for i in all:
    if i in s1 and i in s2 and i in s3:
        ans += i + ' '
print (ans)
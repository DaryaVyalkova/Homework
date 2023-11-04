s = input()
for i in range(len(s)-1):
    if i==0:
        s = s[:i] + s[i].upper() + s[i+1::]
    if s[i] in ('.', '!', '?') :
        s = s[:i+2] + s[i+2].upper() + s[i+3::]
print(s)
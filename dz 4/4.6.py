a = input()
while a.find('(') != -1:
    simb1 = a.find('(')
    simb2 = a.find(')')
    s = a[simb1+1:simb2]
    a = a[simb2+1::]
    print (s)
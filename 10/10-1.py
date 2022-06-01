def sum(a):
    c=0
    for i in range(len(a)):
        c+=a[i]
    return c

a=list(map(int,input()))
b=sum(a)
print(b)




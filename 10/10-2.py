def loop(a):
    a = str(a)
    if a==a[::-1]:
        return 1
    else:
        return 0

a=list(map(int,input().split()))
for i in range(a[0], a[1]+1):
    if loop(i)==1:
        print(i)


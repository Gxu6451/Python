def isprime(x):
    for i in range(2,x):
            if x%i==0:
                return 0
    return 1

a=int(input())
x=isprime(a)
print(x)
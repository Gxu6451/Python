a=int(input())
if a>1:
    for i in range(2,a):
        if (a%i)==0:
            print(0)
            break
    else:
        print(1)
else:
    print(0)
#说思路吧
#用i除遍2到a的的数
#有能除尽的就不是素数
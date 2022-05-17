a=int(input()) #输入
for a in range(100,a+1): #a遍历100-a+1
    i=a//100 #百位
    j=a//10%10 #十位
    k=a%10 #个位
    if a==i*i*i+j*j*j+k*k*k: #水仙花数的定义
        print(a)


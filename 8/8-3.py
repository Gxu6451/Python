a=input() #输入
A=0
n=0
for i in a: #i遍历a
    if i.isdigit(): #如果是数字
        n+=1 #n+1
    elif i.isalpha(): #如果是字母
        A+=1 #A+1
    else: #其他的不管
        pass
print(A,n) #输出A,n

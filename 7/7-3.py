a=input().split() #按空格分割输入字符，转为列表
d1=eval(a[0]) #a[0]是什么eval就转化成什么
d2=eval(a[1])
if a[2]=="+": #如果是+
    print(d1+d2) #输出加和后结果
elif a[2]=="-": #如果-
    print(d1-d2) #输出-的结果
elif a[2]=="*": #如果*
    print(d1*d2) #输出*的结果
elif a[2]=="/": #如果/
    if d1%d2==0: #如果能整除
        print(int(d1/d2)) #输出除的结果
    else: #整除不了
        print("{:.2f}".format(d1/d2)) #保留两位小数输出
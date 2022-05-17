'''a=int(input())
b=list(map(int,input().split()))
print(max(b),min(b))''' #列表的方法也对
a=int(input()) #没用，就纯占位置的
b=input().split() #按空格分割输入字符，转为列表
x=int(b[0])
y=int(b[0])
for i in b: #i遍历b
    if int(x)>int(i): #如果x>i
        x=i #让i等于x
    elif int(y)<int(i): #如果y<i
        y=i #让i等于y
print(y,x) #输出y,x



x = list(map(int, input().split("."))) #生日
y = list(map(int, input().split("."))) #当前日期
if y[1]>x[1] or (y[1]==x[1] and y[2]>x[2]): #当前月大于生日月或当前月等于生日月但当前天大于生日天
    a=y[0]-x[0] #当前年减生日年
    print(a) #输出
else: #其他的情况
    b=y[0]-x[0]-1 #当前年减生日年再减一
    print(b) #输出


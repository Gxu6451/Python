'''x=list(map(eval, input().split()))
day=[31,28,31,30,31,30,31,31,30,31,30,31]
if x[0] % 400 == 0 or (x[0] % 4==0 and x[0] %100!=0):
    if x[1]==2:
        print(sum(day[0:x[1]-1])+x[2])
    else:
        print(sum(day[0:x[1] - 1]) + x[2])
else:
    print(sum(day[0:x[1]-1])+x[2])'''
#上面的能拿9分
x=list(map(eval, input().split())) #输入年月日
mon=[31,28,31,30,31,30,31,31,30,31,30,31] #平年个月日期
year=x[0] #输入的年
month=x[1] #输入的月
day=x[2] #输入的日
if year%400==0 or (x[0] % 4==0 and x[0] %100!=0): #判断输入年是否为闰年
    if month == 1: #如果输入的月等于1
        print(day) #输出输入的日
    elif month==2 and day!=29: #若输入的月为2且输入的日不等于29
        print(31+day) #输出31+输入的日
    else: #如果输入的月不等于1
        print(sum(mon[0:x[1]-1])+day+1) #输出各月日期加和+输入的日+1
else: #若不为闰年
    print(sum(mon[0:x[1]-1])+day) #输出各月日期加和+输入的日
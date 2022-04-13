a=int(input()) #输入第一天的能力值
b=a/1000 #能力值变化为千分之一
dayup = pow((1+b),365) #努力的结果
daydown= pow((1-b),365) #放任的结果
c=dayup/daydown #二者比值
print("{:.2f},{:.2f},{}".format(dayup,daydown,round(c))) #分别输出努力放任的结果和二者比值。format为格式化函数，{:.2f}为保留两位小数的格式。round为四舍五入
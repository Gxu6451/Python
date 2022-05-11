a=eval(input()) #工资
if a<1000: #按要求写就行
    print("{:.2f}".format(a)) #format是format数字格式化函数
elif 1000<=a<2000:
    print("{:.2f}".format(a-a*0.10,2)) #
elif 2000<=a<3000:
    print("{:.2f}".format(a-a*0.15,2))
elif 3000<=a<4000:
    print("{:.2f}".format(a-a*0.20,2))
elif 4000 <= a :
    print("{:.2f}".format(a - a * 0.25,2))

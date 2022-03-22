a=eval(input())
b=a/1000
dayup = pow((1+b),365)
daydown= pow((1-b),365)
c=dayup/daydown
print("{:.2f},{:.2f},{}".format(dayup,daydown,round(c)))


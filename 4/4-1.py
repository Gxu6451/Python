x, y = input().split()  # 输入两个整数中间用空格隔开
x = int(x)  # int将x转换为整型。
y = int(y)  # 同上
'''以上三行可以用map一行解决
x, y= map(int, input().split())'''
a = list(range(x, y + 1, 2))  # list将从x开始到y+1结束，以2为步长的数转化为列表
b = len(a)  # len函数将a的个数赋给b
print(a)  # 输出a
print(b)  # 输出b

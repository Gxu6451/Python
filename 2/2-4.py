'''S=math.sqrt(s*(s-x)*(s-y)*(s-z))
s=(x+y+z)/2
三角形的面积公式
注意：公式中的S区分大小写
'''
import math #调用math库
x,y,z=input().split() #通过split函数对字符串进行切片
x=int(x) #将一个字符串或数字转换为整型。
y=int(y) #同上
z=int(z) #同上
s=(x+y+z)/2 #求公式中s的值
S=math.sqrt(s*(s-x)*(s-y)*(s-z)) #利用math.sqrt求平方根
print("{:.3f}".format(S)) #输出保留三位小数的S值
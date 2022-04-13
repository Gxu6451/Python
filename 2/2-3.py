x,y,z=input().split() #split通过指定分隔符对字符串进行切片
x=int(x) #int将x转换为整型。
y=int(y) #同上
z=int(z) #同上
print(x+y+z) #加和
print("{:.2f}".format((x+y+z)/3)) #取平均

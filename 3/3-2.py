x=input() #输入数据
y=ord(x)-1 #ord函数返回x前一位的 ASCII 数值
z=ord(x)+1 #ord函数返回x后一位的 ASCII 数值
print(chr(y),x,chr(z)) #利用chr函数返回y和z对应的 ASCII 字符
print(y,ord(x),z) #利用ord函数返回x的 ASCII 数值
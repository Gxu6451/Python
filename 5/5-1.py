x = input().split(",")  # 用","分割返回输入字符串的列表
y = input().split(",")  # 用","分割返回输入字符串的列表
z = dict(zip(x, y))  # 映射函数方式来构造字典
b = int(input())  # 输入key的位数
c = z.get(x[b])  # 返回输入key的值
print(c)  # 输出c

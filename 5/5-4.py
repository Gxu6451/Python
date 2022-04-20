x = list(map(str, input()))  # list把map将input()转化的字符串转为列表
x.reverse()  # 反向列表中元素
y = "".join(x)  # 按引号内的规则将列表元素组合
print(y)  # 输出y

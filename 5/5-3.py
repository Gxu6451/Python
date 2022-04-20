x = map(int, input().split())  # map将input().split()转化为整形
y = map(int, input().split())  # map将input().split()转化为整形
a = list(x)  # 将x转化为列表
b = list(y)  # 将y转化为列表
b.append(123)  # 在列表末尾添加123
print(a[1:] + b)  # 输出列表a从第二个元素开始后的所有元素和列表b

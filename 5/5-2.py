import random  # 调用random库
a=int(input())  # 将输入的数转化为整形
random.seed(a)  # seed方法令a为随机数生成器的种子
x=random.randint(1,100)  # 产生（1,100）间的随机数
print(x,x,x)  # 输出3个
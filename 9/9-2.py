a=list(map(str,input()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
print("".join(b))
#i是a里的元素
#b是空列表
#把在a列表里的不在b里的元素放进b
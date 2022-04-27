x,y,z = map(eval, input().split()) #输入三个数
if x>y: #如果x>y
    x, y=y,x #x,y互换位置
if x>z: #如果x>z
    x,z=z,x #x,z互换位置
if y>z: #如果y>z
    y,z=z,y #y,z互换位置
print(x,y,z) #输出换完位置后的xyz








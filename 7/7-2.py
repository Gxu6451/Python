h,m,s  =map(int, input().split(":")) #map按:分割出时分秒
s+=1 #令秒加一
if s==60: #如果秒加一后等于60
    m+=1 #分加一
    s=0 #秒变0
    if m==60: #分加一后等于60
        h+=1 #时加一
        m=0 #分变0
        if h==24: #如果时加一后等于24
            h=0 #时变0
h=str(h) #转换为字符串
m=str(m)
s=str(s)
print(h+':'+m+':'+s)

h,m =map(int, input().split(":")) #map按:分割出时分
hangle=h*1/12*360+m*1/60*30 #时针与12点的夹角
mangle=m*1/60*360 #分针与12点的夹角
includedangle=abs(hangle-mangle) #时针分针夹角的绝对值
if includedangle>180: #如果时针分针夹角的绝对值大于180
    print("{:.3f}".format(abs(360-includedangle))) #输出时针分针夹角的补角
else: #如果时针分针夹角的绝对值小于180
    print("{:.3f}".format(includedangle)) #输出时针分针夹角的绝对值
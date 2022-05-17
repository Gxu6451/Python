n=int(input()) #输入天数
f=n*100000 #富豪给的钱
while 0<=n<=30: #n大于0小于30
    a=(2**n)-1 #等比数列求和
    print(f) #输出富豪给的钱
    print(a) #输出陌生人给的钱
    break #停止循环

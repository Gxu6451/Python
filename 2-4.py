'''S=math.sqrt(s*(s-x)*(s-y)*(s-z))
s=(x+y+z)/2
'''
import math
x,y,z=input().split()
x=int(x)
y=int(y)
z=int(z)
s=(x+y+z)/2
S=math.sqrt(s*(s-x)*(s-y)*(s-z))
print("{:.3f}".format(S))

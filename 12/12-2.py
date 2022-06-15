import re
read_file=open("in.txt",'r',encoding='UTF-8')
a=read_file.read()
b=re.sub('\d',' ',a)
c=re.sub('[+=-]',' ',b)
d=b.split()
#print(a)
#print(b)
print(len(d),len(a)-1)
'''read_file=open("in.txt",'r',encoding='UTF-8')
a=read_file.read()
import re
read_file=open("in.txt",'r',encoding='UTF-8')
a=read_file.read()
print(a)
#print(len(a.split()),len(a)-1)
for i in range(0,9):
    b=str.replace('i',' ')
    print(b)'''
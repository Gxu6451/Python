import re
read_file=open("in.txt",'r',encoding='UTF-8')
a=read_file.read()
b=re.sub('\d',' ',a)
str=re.sub('[+=-]',' ',b)
c=str.split()
print(len(c),len(a)-1)

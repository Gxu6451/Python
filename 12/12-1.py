fin=open("filecopy.in",'r',encoding='UTF-8')
a=fin.read()
print(type(a),a)
fout=open("filecopy.out",'w',encoding='UTF-8')
b=a
fout.write(b)
print(b)
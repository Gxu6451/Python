key = list(input())
keylist =[]
for i in key:
    if not i in keylist:
        keylist.append(i)
ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
      'x', 'y', 'z']
for i in range(len(keylist)):
    ab.remove(keylist[i])
ab.reverse()
rawcipher = keylist + ab
cipher = "".join(rawcipher)
read_file = open("encrypt.txt", 'r', encoding='UTF8')
write_file = open("output.txt", 'w', encoding='UTF8')
rawtext = read_file.read()
read_file.close()
intab1 = 'abcdefghijklmnopqrstuvwxyz'
trantab = rawtext.maketrans(intab1, cipher)  # cipher,intab1
write = write_file.write(rawtext.translate(trantab))
print(rawtext.translate(trantab))
write_file.close()
import csv
import turtle
with open("turtuledata2.txt",'r',encoding='UTF-8') as f1:
    mylist1=list(csv.reader(f1))
atl=turtle.Turtle()
turtle.colormode(255)
for i in mylist1[1:]:
    i=list(map(int,i))
    atl.pensize(i[-1])
    atl.pencolor(i[-4],i[-3],i[-2])
    if i[0]==1:
        atl.right(i[1])
    else:
        atl.left(i[1])
    atl.forward(i[2])
turtle.done()
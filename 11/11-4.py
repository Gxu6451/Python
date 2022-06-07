import turtle
a=turtle.Turtle()
l=int(input())
n=6
jiao=(n-2)*180/n
def star(l):
    a.fillcolor("yellow")
    a.begin_fill()
    for i in range(3):
        a.forward(l)
        a.right(120)
    a.end_fill()

for i in range(n):
    a.forward(l)
    a.left(360/n)
    star(l)
a.fillcolor("red")
a.begin_fill()
for i in range(n):
    a.left(jiao)
    a.forward(l)
    a.left(180)
a.end_fill()
a.screen.mainloop()
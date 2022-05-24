import turtle
a=turtle.Turtle()
a.speed(50)
r=20
x=["red","blue","pink","purple","yellow","orange","coral","brown","fuchsia","blue"]
for i in range(9,0,-1):
    a.penup()
    a.right(90)
    a.forward(-r)
    a.left(90)
    a.pendown()
    a.fillcolor(x[i-1])
    a.begin_fill()
    a.circle(r*i)
    a.end_fill()
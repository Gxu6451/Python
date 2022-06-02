def mycircle(r):
    import turtle
    a = turtle.Turtle()
    a.speed(50)
    for i in range(9, 0, -1):
        x = ["red", "blue", "cyan", "pink", "yellow", "orange", "coral", "brown", "fuchsia", "blue"]
        a.penup()
        a.right(90)
        a.forward(-r)
        a.left(90)
        a.pendown()
        a.fillcolor(x[i - 1])
        a.begin_fill()
        a.circle(r * i)
        a.end_fill()
    turtle.mainloop()

r=float(input())
for j in (r,10,-10):
    mycircle(j)

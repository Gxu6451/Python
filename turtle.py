#画蟒
import turtle
tl=turtle.Turtle()
tl.goto(-400,0)
pythonsize=20
tl.pensize(pythonsize)
tl.pencolor('red')
tl.seth(-40)
rad=40;angle=80;len=6;neckrad=pythonsize/2
for i in range(len):
    tl.circle(rad,angle)
    tl.circle(-rad,angle)
tl.circle(rad,angle/2)
tl.fd(rad)
tl.circle(neckrad+1,180)
tl.fd(rad*2/3)
print(len)
tl.screen.mainloop()
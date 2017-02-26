import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.speed(1)
tess.penup()
tess.stamp()
for i in range(12):
    tess.forward(150)
    tess.pendown()
    tess.pensize(3)
    tess.forward(10)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.forward(-180)
    tess.right(30)

wn.mainloop() 
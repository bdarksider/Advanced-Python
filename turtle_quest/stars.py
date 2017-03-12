import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()

# turtle properties
tess.color("hotpink")
tess.pensize(5)
tess.speed(1)

# move turtle to a point from where star would take proper shape
tess.penup()
tess.left(150)
tess.forward(230)

#reset to initial angle
tess.left(-150)

# draw stars
for i in range(5):
    # pendown to draw stars
    tess.speed(5)
    tess.pendown()

    for i in range(5):
        tess.forward(60)
        tess.right(144)
    tess.speed(2)

    # penup to go to specific distance
    tess.penup()
    # distance according to question
    tess.forward(60 + 350)
    tess.right(144)
wn.mainloop()

# in question it says what will happen if penup is not performed
# remove penup at line 33 and try

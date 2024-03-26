#import turtle
#
#t=turtle.Turtle()
#
#t.pencolor("red")
#t.pensize(3)
#
#for i in range(5):
#    t.forward(100)
#    t.left(144)
#
#t.hideturtle()
#
#turtle.done()

#螺旋线

import turtle

t=turtle.Turtle()

def drawSpiral(t,lineLen):
    if lineLen>0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(t,lineLen-5)

drawSpiral(t,100)

turtle.done()
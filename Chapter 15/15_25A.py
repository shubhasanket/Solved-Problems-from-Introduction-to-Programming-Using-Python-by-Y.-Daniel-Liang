from turtle import *

tracer(100000)
hideturtle()
speed(100)

def koch1(a,order):
    if order == 0:
        fd(a)
    else:
        pencolor("Blue")
        koch1(a/3,order-1)  #fd(a//3)
        left(60)
        pencolor("Red")
        koch1(a/3,order-1)  #fd(a//3)
        left(-120)
        pencolor("Black")
        koch1(a/3,order-1)  #fd(a//3)
        left(60)
        pencolor("Green")
        koch1(a/3,order-1)  #fd(a//3)

def koch(a,order):
    left(60)
    for i in range (3):
        koch1(a,order)
        right(120)
##koch1(200,1)
d = 400
penup()
goto(-d/2,-d/3)
pendown()
width(2)
koch(d,4)
update()

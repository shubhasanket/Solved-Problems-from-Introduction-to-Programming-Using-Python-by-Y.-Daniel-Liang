"""The Hilbert curve, first described by German mathematician David Hilbert in 1891,
is a space-filling curve that visits every point in a square grid with a size of
2 * 2, 4 * 4, 8 * 8, 16 * 16, or any other power of 2. Rewrite the Hilbert curve
in Exercise 15.33 using Turtle, as shown in Figure 15.20. Your prsogram should
prompt the user to enter the order and display the corresponding fractal for the
order."""
from turtle import *
a = 200
##hideturtle()
penup()
goto(-a/2, a/2)
pendown()
##lt(90)
def hilbert_Curve(a, order, type1):
##    if order == 0:
##        return
##    elif order%2 == 1:
##        rt(90)
##    else:
##        lt(90)

    if order == 1:
        print("...")
        draw(a, type1)
    elif type1:
        print("....")
##        rt(90)
##        hilbert_Curve(a/2, order-1, not type1)
##        lt(90)
##        fd(a/2)
##        hilbert_Curve(a/2, order-1, type1)
##        rt(90)
##        fd(a/2)
##        rt(90)
##        hilbert_Curve(a/2, order-1, type1)
##        fd(a/2)
##        lt(90)
##        hilbert_Curve(a/2, order-1, not type1)
        hilbert_Curve(a/2, order-1, not type1)
        rt(90)
        fd(a/2)
        hilbert_Curve(a/2, order-1, type1)
        lt(90)
        fd(a/2)
        lt(90)
        hilbert_Curve(a/2, order-1, type1)
        fd(a/2)
        rt(90)
        hilbert_Curve(a/2, order-1, not type1)
    else:
##        rt(90)
##        hilbert_Curve(a/2, order-1, type1)
##        rt(90)
##        fd(a/2)
##        hilbert_Curve(a/2, order-1, not type1)
##        lt(90)
##        fd(a/2)
##        lt(90)
##        hilbert_Curve(a/2, order-1, not type1)
##        fd(a/2)
##        rt(90)
##        hilbert_Curve(a/2, order-1, type1)
        hilbert_Curve(a/2, order-1, type1)
        lt(90)
        fd(a/2)
        hilbert_Curve(a/2, order-1, not type1)
        rt(90)
        fd(a/2)
        rt(90)
        hilbert_Curve(a/2, order-1, not type1)
        fd(a/2)
        lt(90)
        hilbert_Curve(a/2, order-1, type1)
        
        

        
def draw(a, type1):
    if type1:
        fd(a)
        lt(90)
        fd(a)
        lt(90)
        fd(a)
    else:
        fd(a)
        rt(90)
        fd(a)
        rt(90)
        fd(a)
        
    
first = False
def main():
    global first
    order = 3
    if order%2 == 1:
        first = True
        rt(90)
    hilbert_Curve(a, order, first)
main()

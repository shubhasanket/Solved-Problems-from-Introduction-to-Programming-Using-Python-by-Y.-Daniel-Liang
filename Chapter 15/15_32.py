"""(Turtle: Recursive tree) Rewrite the recursive tree in Exercise 15.31 using Turtle, as shown in Figure 15.18.
Your program should prompt the user to enter the order and display the corresponding fractal for the order.
"""
from turtle import *
a = 200
theta = 60
k = 0.55
speed(100)
tracer(1000)
lt(90)
penup()
goto(0,-a)
pendown()
def tree(a, order):
    if order == 0:
        fd(a)
        bk(a)

    else:
        fd(a)
        lt(theta/2)
        tree(a*k, order-1)
        rt(theta)
        tree(a*k, order-1)
        lt(theta/2)
        bk(a)

tree(a,8)
update()        
        
        
    
    

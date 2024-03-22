'''An H-tree is a fractal defined as follows:
1. Begin with a letter H. The three lines of the H are of the same length,
as shown in Figure 15.1a.
2. The letter H (in its sans-serif form, H) has four endpoints. Draw an H
centered at each of the four endpoints to an H-tree of order 1, as shown
in Figure 15.1b. These Hs are half the size of the H that contains the fourendpoints.
3. Repeat Step 2 to create an H-tree of order 2, 3, ..., and so on, as shown in
Figure 15.1c–d.
'''
from turtle import *

tracer(10000)
hideturtle()
speed(1000)
lt(90)

def h_Tree(a,order):
    if order == 0:
        lt(90)
        fd(a/2)
        rt(90)
        fd(a/2)
        bk(a)
        fd(a/2)
        rt(90)
        fd(a)
        lt(90)
        fd(a/2)
        bk(a)
        fd(a/2)
        lt(90)
        fd(a/2)
        right(90)
    else:
        lt(90)
        fd(a/2)
        rt(90)
        fd(a/2)
        h_Tree(a/2, order-1)
        bk(a)
        h_Tree(a/2, order-1)
        fd(a/2)
        rt(90)
        fd(a)
        lt(90)
        fd(a/2)
        h_Tree(a/2, order-1)
        bk(a)
        h_Tree(a/2, order-1)
        fd(a/2)
        lt(90)
        fd(a/2)
        right(90)

h_Tree(400,6)
update()        
        
        

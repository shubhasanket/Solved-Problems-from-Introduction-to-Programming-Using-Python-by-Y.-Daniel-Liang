#HILBERT 2
from turtle import *

#hideturtle()
#speed(1)
tracer(10)
step = 600
angle=90


def myhilbert(order, step, angle):
    if order > 0:
        #Turtle facing east

        right(angle)  #Original
        myhilbert(order - 1, step, -angle)
##        left(angle)
##        forward(step)
##        right(angle)
##        forward(step)
##        right(angle)
##        forward(step)
##        left(angle)

        forward(step)     #Original connecting line 1

        left(angle)   #Original
        myhilbert(order -1, step, angle)
##        right(angle)
##        forward(step)     #connecting line 1
##        left(angle)
##        forward(step)     #connecting line 2
##        left(angle)
##        forward(step)     #connecting line 3
##        right(angle)

        forward(step)     #Original connecting line 2
        myhilbert(order -1, step, angle)        
        #####Hilbert 1
##        right(angle)
##        forward(step)     #connecting line 1
##        left(angle)
##        forward(step)     #connecting line 2
##        left(angle)
##        forward(step)     #connecting line 3
##        right(angle)

        left(angle)   #Original
        forward(step)     #Original connecting line 3
        #####Hilbert 1A
        myhilbert(order - 1, step, -angle)        
##        left(90)
##        forward(step)
##        right(90)
##        forward(step)
##        right(90)
##        forward(step)
##        left(90)


        right(angle)  #Original
        ####
        ###Turtle facing east as at beginning

order = 4
penup()
goto(-step/2,step/2)
pendown()
s = step/(2**order-1)
myhilbert(order,s,angle)    
update()
done()

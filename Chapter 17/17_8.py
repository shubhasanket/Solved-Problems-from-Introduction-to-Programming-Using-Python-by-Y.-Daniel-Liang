'''17.8 (Turtle: bubble sort animation) Write a program that animates
the bubble sort algorithm. Create a list that consists of 20 distinct
numbers from 1 to 20 in a random order. The list elements are displayed
in a histogram, as shown in Figure 17.15. If two elements are swapped,
redisplay them in the histogram.
'''
import turtle as t
import time
import random
t.hideturtle()
##t.speed(0)
t.tracer(100)
def bubbleSort(lst):
    needNextPass = True

    k = 1
    while k < len(lst) and needNextPass:
        needNextPass = False
        for i in range(len(lst)-k):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                update(lst)

                needNextPass = True
##        k += 1
def update(lst):
    
    x = 25
    y = 30
    w = 700
    h = 300
    length = len(lst)
    unit_y = (h-2*y)/length
    unit_x = (w-2*x)*0.8/length
    gap = (w-2*x)*0.2/(length+1)
    t.clear()
    t.penup()
    t.goto(-w/2+x,-h/2+y)
    t.pendown()
    for u in lst:
        t.forward(gap)
        t.left(90)
        t.forward(unit_y*u)
        t.right(90)
        t.forward(unit_x)
        t.right(90)
        t.forward(unit_y*u)
        t.left(90)
    t.forward(gap)
    t.penup()
    t.goto(-w/2+x+unit_x/2+gap/2,-h/2+y-unit_y)
    for u in lst:
        t.pendown()
        t.write(u)
        t.penup()
        t.forward(unit_x+gap)
        
    t.update() # as I am using t.tracer(), I want to update turtle before getting into the next cycle
    time.sleep(1.5)
##    print("'''")
##    input("Press Enter to continue")


def main():
##    lst = [2,3,2,5,6,1,2,3,14,12,11,11,23,12,12,21]
    lst = [random.randrange(1,30) for i in range (17)]
    t.screensize(canvwidth = 500, canvheight = 300)
    bubbleSort(lst)
    for v in lst:
        print(str(v) + " ", end = "")

main()


    
        
     
    

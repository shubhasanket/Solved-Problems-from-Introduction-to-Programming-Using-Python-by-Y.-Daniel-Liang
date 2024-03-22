"""16.17 Write a program that prompts the user to enter points and
displays a noncrossed polygon that links all the points, as shown in
Figure 16.11a. A polygon is crossed if two or more sides intersect, as
shown in Figure 16.11b. Use the following algorithm to construct a polygon
from a set of points.
"""
import random
from tkinter import *
import sys
import math


class nonCrossPoly:
    ''' Step 1: Given a list of points S, select the rightmost lowest point
        and name it p0 in S.

        Step 2: Sort the points in S angularly along the x-axis with p0 as
        the center. If there is a tie and two points have the same angle, the
        one that is closest to p0 is consider greater. The points in S are
        now sorted as p0, p1, p2, ..., pn-1.

        Step 3: The sorted points form a non-cross polygon.
        '''
    def __init__(self,points,n,m):
        if len(points) < 3:
            print("There must be at least 3 points")
            sys.exit()
        self.points = points
##        print("Right click to remove points and left click to add points")
        window = Tk()
        self.canvas = Canvas(window, height = m, width = n, bg ="white")
        self.canvas.pack()
##        self.canvas.bind("<Button-3>",self.removePoint)
##        self.canvas.bind("<Button-1>",self.addPoint)
        self.drawPoints()
##        window.mainloop()

    def steps(self):
        # Steps 1
        S = sorted(self.points,key = lambda x : (x[1],x[0])) 
        h0 = S[-1]
        p0 = h0 # p0 is the first point
        # Step 2
##        print(p0)
        s = []
        for p in S:
            s.append([self.findAngle(p0,p),self.distance(p0,p),p])

        l = sorted(s,key = lambda x: (x[0],-x[1]))
        # Step 3:
        # will be done in self.drawPoints()
##        print("S = ",S)
##        print("s = ",s)
##        print("l = ",l)
        return l



    def drawPoints(self):
        self.canvas.delete("points","line")
        for u in self.points:
            a = u[0]
            b = u[1]
            self.canvas.create_oval(a-2,b-2,a+2,b+2, fill = "black", tags = "points")
##            self.canvas.create_text(a,b+5, text = "("+str(a)+","+str(b)+")")
    ##    window.update()
        l = self.steps()
        l.append(l[0])
##        print(l)
        for i in range (len(l)-1):
            self.canvas.create_line(l[i][2][0],l[i][2][1],l[i+1][2][0],l[i+1][2][1], fill = "black", tags = "line")
        l.pop()  

    def distance(self,p1,p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 )    

    def findAngle(self,p0,p1):
        if p0 == p1:
            return 0
        #p0 is the lowest rightmost point
        #p1 is the point whose angle is to be found from the horizontal axis
        #p2 is a point on the x axis - to the the right of p0
        p2 = [p0[0] + 10, p0[1]]
        #Find the three sides
        #a0 is opposite side of p0, a1 opposite to p1 etc
        a0 =  math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])) 
        a1 = math.sqrt((p0[0] - p2[0]) * (p0[0] - p2[0]) + (p0[1] - p2[1]) * (p0[1] - p2[1]))
        a2 = math.sqrt((p0[0] - p1[0]) * (p0[0] - p1[0]) + (p0[1] - p1[1]) * (p0[1] - p1[1]))

        angle0 = math.degrees(math.acos((a0 * a0 - a1 * a1 - a2 * a2) / (-2 * a1 * a2)))
        return angle0
        

m = 800
n = 1100            
points = [[random.randrange(0.1*n,0.9*n),random.randrange(0.1*m,0.9*m)]for i in range (30)]
nonCrossPoly(points,1000,800)        
        

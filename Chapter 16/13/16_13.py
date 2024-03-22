"""16.13 (Tkinter: convex hull using gift-wrapping algorithm) Exercise
16.11 finds a convex hull for a set of points entered from the console.
Write a Tkinter program that enables the user to add/remove points by
clicking the left/right mouse button, and displays a convex hull.
"""

import sys
from tkinter import *
import random
class convexHull:
    '''Step 1:
    Given a list of points S, let the points in S be labeled
    s0, s1, ..., sk. Select the rightmost lowest point h0 in S. As shown in
    Figure 16.8a, h0 is such a point. Add h0 to the convex hull H. H is a
    list initially being empty. Let t0 be h0.

    Step 2:
    Let t1 be s0. For every point s in S if s is on the right side of the
    direct line from t0 to t1: let t1 be s

    (After Step 2, no points lie on the right side of the direct line from t0
    to t1)

    Step 3:
    If t1 is h0 (see Figure 16.6d), the points in H form a convex hull
    for S. Otherwise, add t1 to H, let t0 be t1, and go to Step 2.
    '''
    def __init__(self,points,n,m):
        if len(points) < 3:
            print("There must be at least 3 points")
            sys.exit()
        self.points = points
        print("Right click to remove points and left click to add points")
        window = Tk()
        self.canvas = Canvas(window, height = m, width = n, bg ="white")
        self.canvas.pack()
        self.canvas.bind("<Button-3>",self.removePoint)
        self.canvas.bind("<Button-1>",self.addPoint)
        self.drawPoints()
        window.mainloop()

    def steps(self):
        # Step 1
        l = [] # list of the points that will form the hull
        S = sorted(self.points,key = lambda x : x[1])
    ##    print(S)
        h0 = S[-1]
        l.append(h0)
        t0 = h0
    ##    print("S =",S)
        # Step 2
        
        t1 = S[0]
        while l[0] != l[-1] or len(l) == 1:
    ##        print("t1 =", t1)
            for j in range (len(S)):
    ##            print("S[j] =",S[j])
                if self.pointPosition(t0,t1,S[j]):
                    t1 = S[j]
            # Step 3
            l.append(t1)
            t0 = t1
            i = 0
            t1 = S[i]
            while t0 == t1:
                i += 1
                t1 = S[i]
                
    ##        print(l)
    ##        
        return  l

    def drawPoints(self):
        self.canvas.delete("points","line")
        for u in self.points:
            a = u[0]
            b = u[1]
            self.canvas.create_oval(a-2,b-2,a+2,b+2, fill = "black", tags = "points")
    ##    window.update()
        l = self.steps()
        for i in range (len(l)-1):
            self.canvas.create_line(l[i][0],l[i][1],l[i+1][0],l[i+1][1], fill = "black", tags = "line")
        return

    def addPoint(self,event):
        self.points.append([event.x,event.y])
        self.drawPoints()
        return
    
    def removePoint(self,event):
        tol = 2
        x = event.x
        y = event.y
        for u in self.points:
            if (x-tol<=u[0]<=x+tol) and (y-tol<=u[1]<=y+tol):
                self.points.remove(u)
        self.drawPoints()
        return
            
    def pointPosition(self,p0,p1,p2):
        r = (p1[0]-p0[0])*(p2[1]-p0[1]) - (p2[0]-p0[0])*(p1[1]-p0[1])
        ret = True if r > 0 else False
    ##    print("for", p0, p1, p2, "ret =",ret)
        return ret
m = 800
n = 1000            
points = [[random.randrange(0.1*n,0.9*n),random.randrange(0.1*m,0.9*m)]for i in range (1000)]
convexHull(points,1000,800)

"""16.15 (Tkinter: convex hull using Graham’s algorithm) Extend Exercise
16.12 to display the points and their convex hull, as shown in Figure
16.5c
"""

from tkinter import *
import sys
import random
import math
import pickle

class Graham_algo:
    '''Step 1: Given a list of points S, select the rightmost lowest
    point and name it p0 in the set S. As shown in Figure 16.9a, p0 is
    such a point.

    Step 2: Sort the points in S angularly along the x-axis with p0 as
    the center, as shown in Figure 16.9b. If there is a tie and two
    points have the same angle, discard the one that is closest to p0.
    The points in S are now sorted as p0, p1, p2, ..., pn-1

    Step 3: Push p0, p1, and p2 into a stack H. A stack is a first-in,
    last out data structure. Elements are added/removed from the top of
    the stack. It can be implemented using a list in which the items are
    appended to the end of the list and retrieved or removed from the end
    of the list. So the end of the list is the top of the stack.

    Step 4: i = 3
            while i < n:
                Let t1 and t2 be the top first and second element in stack H;
                if (pi is on the left side of the direct line from t2 to t1):
                    Push pi to H
                i += 1 # Consider the next point in S
                else:
                    Pop the top element off the stack H

    Step 5: The points in H form a convex hull.
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
        S = sorted(self.points,key = lambda x : (x[1],x[0])) 
    ##    print(S)
        h0 = S[-1]
    ##    i = len(S)-2
    ##    while h0[1] == S[i][1]:
    ##        if S[i][0] > h0[0]:
    ##            h0 = S[i]
    ##        i -= 1
        p0 = h0 # p0 is the first point
    ##    print("S =",S)
        # Step 2
        s = []
        for p in S:
            s.append([self.findAngle(p0,p),p])

        s.sort() # sorting s with respect to angles
        n = len(s)
        i = 0
        while i < n-1:
            if s[i][0] == s[i+1][0]:
                #print(self.s[i],"and",self.s[i+1])
                d1 = self.distance(p0,s[i][1])
                d2 = self.distance(p0,s[i+1][1])
                #print("Distance",d1,d2)
                if d1 < d2:
                    s.pop(i)
                else:
                    s.pop(i+1)
                n = n - 1    
            else:
                i = i + 1
        # now s has no duplicates of angles
        # Step 3
        l = [s[0][1],s[1][1],s[2][1]]
    ##    print(l)

        # Step 4
        i = 3
        n = len(s)
        while i < n:
    ##        print(len(l))
            d = self.whichSide(l[-2],l[-1],s[i][1])
            if d < 0: # on the left
                l.append(s[i][1])
                i += 1
            else:
                l.pop()
                    

        return l

    def drawPoints(self):
        self.canvas.delete("points","line")
        for u in self.points:
            a = u[0]
            b = u[1]
            self.canvas.create_oval(a-2,b-2,a+2,b+2, fill = "black", tags = "points")
    ##    window.update()
        l = self.steps()
        l.append(l[0])
        for i in range (len(l)-1):
            self.canvas.create_line(l[i][0],l[i][1],l[i+1][0],l[i+1][1], fill = "black", tags = "line")
        l.pop()
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

    def distance(self,p1,p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 )

    def whichSide(self,p0,p1,p2):
        return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])  


##m = 800
##n = 1000            
##points = [[random.randrange(0.1*n,0.9*n),random.randrange(0.1*m,0.9*m)]for i in range (70000)]
##s = '20000'
##fname = str(s)+".dat"
##infile = open(fname,"rb")
##points = pickle.load(infile)
##print(Graham_algo(points,1000,800))

m = 800
n = 1000            
points = [[random.randrange(0.1*n,0.9*n),random.randrange(0.1*m,0.9*m)]for i in range (400)]
Graham_algo(points,1000,800)

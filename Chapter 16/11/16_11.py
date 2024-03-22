"""16.11 (Geometry: gift wrapping algorithm for finding a convex hull)
Section 16.16.1 introduced the giftwrapping algorithm for finding a
convex hull for a set of points. Assume that Tkinter’s coordinate system
is used for the points.
"""
import sys
from tkinter import *
import random
import pickle

def convexHull(points,n,m):
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
    if len(points) < 3:
        print("There must be at least 3 points")
        sys.exit()
    window = Tk()
    canvas = Canvas(window, height = m, width = n, bg ="white")
    canvas.pack()
    for u in points:
        a = u[0]
        b = u[1]
        canvas.create_oval(a-2,b-2,a+2,b+2, fill = "black")
##    window.update()
    l = steps(points)
    for i in range (len(l)-1):
        canvas.create_line(l[i][0],l[i][1],l[i+1][0],l[i+1][1], fill = "black")
        
    return l[:-1]
    wiindow.mainloop()

def steps(points):
    # Step 1
    l = [] # list of the points that will form the hull
    S = sorted(points,key = lambda x : (x[1],x[0])) 
    h0 = S[-1]
##    i = len(S)-2
##    while h0[1] == S[i][1]:
##        if S[i][0] > h0[0]:
##            h0 = S[i]
##        i -= 1
##    print(S)
    
    print(h0)
    l.append(h0)
    t0 = h0
##    print("S =",S)
    # Step 2
    
    t1 = S[0]
    while l[0] != l[-1] or len(l) == 1:
##        print("t1 =", t1)
        for j in range (len(S)):
##            print("S[j] =",S[j])
            if pointPosition(t0,t1,S[j]):
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

def pointPosition(p0,p1,p2):
    r = (p1[0]-p0[0])*(p2[1]-p0[1]) - (p2[0]-p0[0])*(p1[1]-p0[1])
    ret = True if r > 0 else False
##    print("for", p0, p1, p2, "ret =",ret)
    return ret

m = 800
n = 1000            
points = [[random.randrange(0.1*n,0.9*n),random.randrange(0.1*m,0.9*m)]for i in range (40000)]
print(convexHull(points,1000,800)) 
##s = '20000'
##fname = str(s)+".dat"
##infile = open(fname,"rb")
##points = pickle.load(infile)
##print(convexHull(points,1000,800))
    

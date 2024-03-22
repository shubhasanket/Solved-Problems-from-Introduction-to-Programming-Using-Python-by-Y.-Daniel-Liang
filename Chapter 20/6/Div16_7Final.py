"""
16.7 (Closest pair of points) Section 16.8 introduced an algorithm
for finding a closest pair of points using a divide-and-conquer
approach. Implement the algorithm.
"""
import random
import time
import pickle
##x = []
def closest_pair(s):
    sx = sorted(s) # ordered on x
    sy = sorted(s,key = lambda x : x[1])
    d, x = closest_pairHelper(sx, sy)
    return x
    
def closest_pairHelper(sx, sy):
    '''Step 1: Sort the points in increasing order of x-coordinates.
    For the points with the same x-coordinates, sort on y-coordinates.
    This results in a sorted list S of points.
    
    Step 2: Divide S into two subsets S1 and S2 of the equal size
    using the midpoint in the sorted list. Let the midpoint be in S1 .
    Recursively find the closest pair in S1 and S2 . Let d1 and d2 denote
    the distance of the 2 closest pairs in the two subsets, respectively.


    Step 3: Find the closest pair between a point in S1 and a point in S2
    and denote their distance to be d3. The closest pair is the one with
    the distance min(d1,d2,d3)
    '''
##    x = []
    if len(sx) <= 3:
##        print(s)
        return brute(sx)
    #step 1:
##  sx is alrady sorted
    else:        
        #step 2:
        if len(sx)%2 == 0:
            ind = int(len(sx)/2)
        else:
            ind = int((len(sx)+1)/2)
    ##    print(ind)
        mid = sx[ind-1]
    ##    print(mid)
        s1 = sx[:ind]
        s2 = sx[ind:]
    ##        print(s1,s2)
    ##    mid = s[ind-1] # this is the midpoint

        #step 3:
        left = []
        right = []
        midx = mid[0]
        for x in sy:
            if x[0] <= midx:
                left.append(x)
            else:
                right.append(x)
        
        d1, x1 = closest_pairHelper(s1,left)
        d2, x2 = closest_pairHelper(s2,right)
    ##    d,x = d1, []+x1 if d1 == min(d1,d2) else d2, []+x2
        if d1 == min(d1,d2):
            d = d1
            x = x1
        else:
            d = d2
            x = x2
        
##        stripL, stripR = [], []
        # Algorithm for obtaining stripL and stripR
##        for p in sy:
##            if p in s1 and mid[0] - p[0] <= d:
##                stripL.append(p)
##            elif p in s2 and p[0] - mid[0] <= d:
##                stripR.append(p)
##        # Algorithm for finding a closest pair in step 3
##        r = 0 # r is the index in stripR
##        len_stripR = len(stripR)
##        len_stripL = len(stripL)
##        for p in stripL:
##            # Skip the points below the ractangle area
##            while r < len_stripR and stripR[r][1] <= p[1] - d:
##                r += 1
##    ##        r1 = r
##            count = 0
##            while r < len_stripR and abs(stripR[r][1] - p[1]) <= d:
##                if count > 6:
##                    break
##               # Check if (p,stripR[r1]) is a possible closest pair
##                if distance(p,stripR[r]) < d:
##                   d = distance(p,stripR[r])
##                   x = [p,stripR[r]]
##    ##               print(x)
##                r += 1
##                count += 1
        s_y = [x for x in sy if midx - d <= x[0] <= midx + d]
        ln_y = len(s_y)  # store length of subarray for quickness

        for i in range(ln_y - 1):
            for j in range(i+1, min(i + 7, ln_y)):
                p, q = s_y[i], s_y[j]
                dst = distance(p, q)
                if dst < d:
                    x = [p, q]
                    d = dst

        return d, x


def distance(p,q):
    #return pow((q[0]-p[0])**2 + (q[1]-p[1])**2,0.5)
    return ((q[0]-p[0])**2 + (q[1]-p[1])**2) ** 0.5

##def dis_3(l):
##    temp = [distance(l[0],l[1]),distance(l[1],l[2]),
##            distance(l[0],l[2])]
##    i = temp.index(min(temp))
##    if i == 0:
##        x = [l[0],l[1]]
##    elif i == 1:
##        x = [l[1],l[2]]
##    else:
##        x = [l[0],l[2]]
##    return temp[i], x
def brute(sx):
    #print("Brute",len(sx))
    di = distance(sx[0], sx[1])
    p1 = sx[0]
    p2 = sx[1]
    ln_sx = len(sx)
    if ln_sx == 2:
        return di, [p1, p2]
    for i in range(ln_sx-1):
        for j in range(i + 1, ln_sx):
            if i != 0 and j != 1:
                d = distance(sx[i], sx[j])
                if d < di:  # Update min_dist and points
                    di = d
                    p1, p2 = sx[i], sx[j]
    return di, [p1, p2]
def main():
    N = 10000
##    l = [[random.randint(0, N*1000) for i in range(2)] for j in range(N)]
####    l = [[75100, 34917], [64521, 10267], [14265, 77543], [79563, 37232], [75583, 14640], [61447, 46912], [5703, 68295], [43889, 36927], [94161, 34523], [58262, 28271], [199, 28454], [80898, 9752], [62678, 26274], [2666, 3759], [50994, 90713], [9913, 31129], [24741, 50287], [72530, 26439], [73657, 2256], [30797, 5504], [83234, 256], [44347, 26049], [80347, 8720], [59790, 97329], [96678, 91437], [15109, 94514], [48134, 398], [52253, 19128], [41467, 23992], [59332, 92851], [62120, 47917], [8859, 46364], [74886, 44043], [46013, 48117], [33200, 22002], [37609, 92380], [56246, 18880], [49893, 78977], [31887, 89238], [12559, 45562], [97159, 67275], [89556, 45029], [82414, 22488], [44362, 46890], [38837, 59872], [52238, 41562], [41614, 38737], [79290, 29000], [15714, 50389], [79333, 44866], [8348, 26425], [1233, 15347], [84013, 78924], [11908, 94913], [76773, 37200], [49968, 2858], [95205, 35647], [65501, 25559], [95333, 14290], [47829, 56928], [48639, 58070], [93018, 87068], [13281, 18551], [23264, 54026], [3720, 75968], [35428, 76396], [95283, 61399], [36687, 48897], [25061, 91092], [47289, 78412], [26615, 83616], [90162, 66571], [19412, 94169], [10141, 55564], [85988, 32399], [87361, 93391], [10660, 51103], [29349, 41691], [99384, 23364], [44383, 81898], [45465, 95166], [55715, 56478], [24265, 71986], [53291, 37846], [73282, 28189], [9978, 89277], [85479, 96887], [29560, 20314], [19466, 38655], [96199, 15012], [51266, 28756], [94895, 72052], [24507, 61273], [37983, 46823], [92501, 82097], [37748, 62937], [72589, 14835], [53285, 13286], [76592, 199], [9809, 93423]]
####    print(l)
##    t1 = time.time()
##    x = closest_pair(l)
##    print("Shortest distance is",round(distance(x[0],x[1]),4))
##    print("The closest pair is", x)
##    t2 = time.time()
##    print(t2-t1)
####    print(distance(x[0],x[1]))

    fname = str(N)+".dat"
    infile = open(fname,"rb")

    l = pickle.load(infile)
    #l = [[random.randint(0, N*100) for i in range(2)] for j in range(N)]
    
    
##    print(l)
    t1 = time.time()
    x = closest_pair(l)
    t2 = time.time()
    print(x, "Shortest distance is",distance(x[0],x[1]))

    print(t2-t1)




 























    

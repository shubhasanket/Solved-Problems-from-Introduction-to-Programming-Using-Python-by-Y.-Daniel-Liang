"""
16.7 (Closest pair of points) Section 16.8 introduced an algorithm
for finding a closest pair of points using a divide-and-conquer
approach. Implement the algorithm.
"""
import random
import time
##x = []
def closest_pair(s):
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
    if len(s) == 2:
##        print(s)
        return distance(s[0],s[1]), s
    else:
        #step 1:
    ##    print("..............")
        s.sort()
    ##    print(s)
        
        #step 2:
        if len(s)%2 == 0:
            ind = int(len(s)/2)
        else:
            ind = int((len(s)+1)/2)
    ##    print(ind)
        mid = s[ind-1]
    ##    print(mid)
        if len(s) == 3:
            s1 = s[:ind]
            s2 = s[ind-1:]
    ##        print(s1,s2)
        else:
            s1 = s[:ind]
            s2 = s[ind:]
    ##        print(s1,s2)
    ##    mid = s[ind-1] # this is the midpoint

        #step 3:
        x1 = closest_pair(s1)
        x2 = closest_pair(s2)
    ##    d,x = d1, []+x1 if d1 == min(d1,d2) else d2, []+x2
        d1 = distance(s1[0],s1[1])
        d2 = distance(s2[0],s1[1])
        if d1 == min(d1,d2):
            d = d1
            x = x1
        else:
            d = d2
            x = x2
        l = []+s
        l.sort(key = lambda x: x[1]) # l has now been ordered on y
        stripL, stripR = [], []
        # Algorithm for obtaining stripL and stripR
        for p in l:
            if p in s1 and mid[0] - p[0] <= d:
                stripL.append(p)
            elif p in s2 and p[0] - mid[0] <= d:
                stripR.append(p)

        # Algorithm for finding a closest pair in step 3
        r = 0 # r is the index in stripR
        len_stripR = len(stripR)
        len_stripL = len(stripL)
        for p in stripL:
            # Skip the points below the ractangle area
            while r < len_stripR and stripR[r][1] <= p[1] - d:
                r += 1
    ##        r1 = r
            while r < len_stripR and abs(stripR[r][1] - p[1]) <= d:
               # Check if (p,stripR[r1]) is a possible closest pair
                if distance(p,stripR[r])<d:
                   d = distance(p,stripR[r])
                   x = [p,stripR[r]]
##                   print(x)
                r += 1

        return x


def distance(p,q):
    return pow((q[0]-p[0])**2 + (q[1]-p[1])**2,0.5)


def main():
    N = 100
    l = [[random.randint(0, N*1000) for i in range(2)] for j in range(N)]
    l = [[75100, 34917], [64521, 10267], [14265, 77543], [79563, 37232], [75583, 14640], [61447, 46912], [5703, 68295], [43889, 36927], [94161, 34523], [58262, 28271], [199, 28454], [80898, 9752], [62678, 26274], [2666, 3759], [50994, 90713], [9913, 31129], [24741, 50287], [72530, 26439], [73657, 2256], [30797, 5504], [83234, 256], [44347, 26049], [80347, 8720], [59790, 97329], [96678, 91437], [15109, 94514], [48134, 398], [52253, 19128], [41467, 23992], [59332, 92851], [62120, 47917], [8859, 46364], [74886, 44043], [46013, 48117], [33200, 22002], [37609, 92380], [56246, 18880], [49893, 78977], [31887, 89238], [12559, 45562], [97159, 67275], [89556, 45029], [82414, 22488], [44362, 46890], [38837, 59872], [52238, 41562], [41614, 38737], [79290, 29000], [15714, 50389], [79333, 44866], [8348, 26425], [1233, 15347], [84013, 78924], [11908, 94913], [76773, 37200], [49968, 2858], [95205, 35647], [65501, 25559], [95333, 14290], [47829, 56928], [48639, 58070], [93018, 87068], [13281, 18551], [23264, 54026], [3720, 75968], [35428, 76396], [95283, 61399], [36687, 48897], [25061, 91092], [47289, 78412], [26615, 83616], [90162, 66571], [19412, 94169], [10141, 55564], [85988, 32399], [87361, 93391], [10660, 51103], [29349, 41691], [99384, 23364], [44383, 81898], [45465, 95166], [55715, 56478], [24265, 71986], [53291, 37846], [73282, 28189], [9978, 89277], [85479, 96887], [29560, 20314], [19466, 38655], [96199, 15012], [51266, 28756], [94895, 72052], [24507, 61273], [37983, 46823], [92501, 82097], [37748, 62937], [72589, 14835], [53285, 13286], [76592, 199], [9809, 93423]]
    print(l)
    t1 = time.time()
    x = closest_pair(l)
    print("Shortest distance is",round(distance(x[0],x[1]),4))
    print("The closest pair is", x)
    t2 = time.time()
    print(t2-t1)
##    print(x)
    print(distance(x[0],x[1]))
main()


 























    

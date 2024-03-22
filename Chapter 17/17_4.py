"""17.4 (Radix sort) Write a program that randomly generates 1000000 integers
and sorts them using radix sort
"""
import random
import time
def radix_sort(lst):
    N = 10
    buckets = [[] for i in range (N)]
##    print(buckets)

    m = 0
    for u in lst:
        if u > m: m = u
        buckets[u%10].append(u)
##    print(m)
##    print(buckets)
    k = 0
    for i in range (N):
        if buckets[i] != None:
##            buckets[i].sort()
            for u in buckets[i]:
                lst[k] = u
                k += 1
            buckets[i].clear()
    ord_of_mag = len(str(m))
##    print(ord_of_mag)
##    print(lst)
    for i in range (1,ord_of_mag):
        for u in lst:
##            print("u = ", u)
##            print("radix = ",(u%(10**(i+1)))//(10**i))
            buckets[(u%(10**(i+1)))//(10**i)].append(u)
        k = 0
##        print(buckets)
        
##        for i in range (N):
##            if buckets[i] != None:
####                buckets[i].sort()
##                for u in buckets[i]:
##                    lst[k] = u
##                    k += 1
##                buckets[i].clear()
        
        
        lst.clear()
        for i in range (N):
            if buckets[i] != None:
##                buckets[i].sort()
                lst.extend(buckets[i])
                buckets[i].clear()
##            print(lst) 
    return

def main():
##    lst = [331,454,230,34,343,45,59,453,345,231,9,3]
    t1 = time.time()
    lst = [random.randrange(100000000000) for i in range (10000000)]
    radix_sort(lst)
    t2 = time.time()
##    print(lst)
    print(t2-t1)
##    print(lst)
    print("Done")
        
if __name__ == "__main__":
    main()

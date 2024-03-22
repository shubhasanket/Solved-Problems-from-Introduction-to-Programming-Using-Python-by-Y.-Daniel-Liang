import sys
sys.setrecursionlimit(100000)

def sum_series(n, s = 0):
    if n == 0:
        return s

    return sum_series(n-1, s+1/n)

def main(m):
##    for j in range (m+1):
##        n = j
    n = m
    s = 0
    for i in range (1, n+1):
        s += 1/i
    print("With loop:", s)
    print("With recursion:", sum_series(n))
    
main(10000)

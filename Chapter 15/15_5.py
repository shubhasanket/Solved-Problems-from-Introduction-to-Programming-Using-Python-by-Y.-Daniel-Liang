import sys
sys.setrecursionlimit(10000)

def sum_series(n,s=0):
    if n == 0:
        return s

    return sum_series(n-1, s+(n/(2*n+1)))

def main(m):
    for j in range (m+1):
        n = j
        s = 0
        for i in range (1, n+1):
            s += i/(2*i+1)
        print("With loop:", s)
        print("With recursion:", sum_series(n))
    
main(100)

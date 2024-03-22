"""16.3
Boyer Moore (Bad Character)
"""
import time

def BM_find(T,P):
    # Boyer Moore bad character algorithm
    l_T = len(T)
    l_P = len(P)
    a = {}
    for i in range(l_P):
        a[P[i]] = i
    n = l_P - 1                 # will be used with P
    m = n                       # will be used with T
    l = []                      # list to store the starting index of the matches

    while m < l_T:

        if T[m] == P[n]:
            if n == 0:          # solution found
                l.append(m+1)   # save the solution
                m += 2*l_P      # reset m and n
                n = l_P - 1
            else:
                m -= 1
                n -= 1
        else:
            k = a.get(T[m],-1)
            if k != -1:         # char found in P
                if k > n:       # when the matched char is to the right of P[n]
                    m += (l_P-1)-n + 1
                else:
                    m += (l_P-1)-k
            else:               # when no char found in P
                m += 2*l_P - n - 1
            n = l_P - 1
    return l

def main():
    inf = open("savitriFinal.txt", "r")
    T = inf.read()
    P = "SAVITRI"
    s = 0
    n = 100
    for i in range (n):     
      e = time.time()
      l = BM_find(T,P)
      f = time.time()
      s += f-e
    ##l = BM_find(T,P)
    print("Number of matches:",len(l))
    print("The indeces:")
    print(l)
    print("Runtime:", s/n)

main()

"""16.3
Boyer Moore (Bad Character)
"""

T = "AjAWdjlhlaDFWEOrFWEOrhFWEOrieoiehwFWEOrejberjK"
##T = "DFWEOrFWEOrhFWEOrieoiehwFWEOrejbWEOrerjK"
P = "FWEOr"
##T = "AAAAA"
##P = "AA"

l_T = len(T)
l_P = len(P)
#creating a list of the highest indeces of the occurences of the charters in P  
a = [-1]*256
for i in range(l_P):
    a[ord(P[i])] = i

##print(a)
def BM_find(T,P):
    # Boyer Moore bad char algo
    n = l_P - 1 # will be used with P
    m = n       # will be used with T
    l = [] # list to store the starting index of the matches
    print(T)
    print(P)
    while m < l_T:
    ##    print("m =", m)
    ##    print("n =", n)
    ##    print(T[m-n:m+1])
    ##    print(P[:n+1])
        if T[m] == P[n]:
    ##        print("Char match found:",T[m])
    ##        print(T[m-n:m+1])
    ##        print(P[:n+1])
    ##        print("m =", m)
    ##        print("n =", n)
            m -= 1
            n -= 1
        else:
            if a[ord(T[m])] != -1:
                if a[ord(T[m])] > n:
                    m += (l_P-1)-n + 1
                else:
    ##            print()
    ##            print("Char in P:",T[m])
    ##            print("m =", m)
    ##            print("n =", n)
            # the character T[M] is in P
    ##            m += l_P +2 - n + (a[ord(T[m])]-l_P)
    ##            m += (a[ord(T[m])]-n+1)+1 # The error is here. The rest of the code is fine
                    m += (l_P-1)-n + (l_P-1)-a[ord(T[m])]
    ##            print("m =", m)
    ##            print("n =", n)
    ##            print(T[m-l_P+1:m+1])
    ##            print(P[:l_P])

            else:
                m += 2*l_P - n - 1
                
            n = l_P - 1    

##        if n < 0:
####            print("Solution found")
##            # solution found
##            l.append(m+1)
##            m += 2*l_P
##            n = l_P - 1

        if n < 0:
            l.append(m+1)
            m += l_P + 1
            n = l_P - 1

    return l

print(BM_find(T,P))

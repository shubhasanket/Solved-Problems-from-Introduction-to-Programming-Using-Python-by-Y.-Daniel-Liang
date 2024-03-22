"""16.3
Boyer Moore (Bad Character)
"""
import time
##T = "AjAWdjlhlaDFWEOrFWEOrhFWEOrieoiehwFWEOrejberjK"
####T = "DFWEOrFWEOrhFWEOrieoiehwFWEOrejbWEOrerjK"
##T = "FWEOraFWEOrabFWEOrBSEFWEOFWEOr"
##P = "FWEOr"
##T = "AAAAA"
##P = "AA"


#creating a list of the highest indeces of the occurences of the charters in P  


##print(a)
def BM_find(T,P):
    # Boyer Moore bad char algo
    l_T = len(T)
    l_P = len(P)
    a = [-1]*256
    for i in range(l_P):
        a[ord(P[i])] = i
    n = l_P - 1 # will be used with P
    m = n       # will be used with T
    l = [] # list to store the starting index of the matches
##    print(T)
##    print(P)
    while m < l_T:
##        print(m,n)
        if T[m] == P[n]:
            if n == 0: # solution found
##                print(m+1)
                l.append(m+1)
##            m += l_P + 1
                m += 2*l_P
                n = l_P - 1
            else:
                m -= 1
                n -= 1
        else:
            if a[ord(T[m])] != -1: # char found in P
                if a[ord(T[m])] > n: # when the matched char is to the right of P[n]
                    m += (l_P-1)-n + 1
##                    print("................")
                else:
                    m += (l_P-1)-n + (n-a[ord(T[m])])
            else: # when no char found in P
                m += 2*l_P - n - 1
            n = l_P - 1
    return l

##inf = open("Savitri_formatted_stage_2.txt", "r")
inf = open("savitriFinal.txt", "r")
T = inf.read()
P = "SAVITRI"
l = BM_find(T,P)
print(l)
print(len(l))
##final = []
##while T != "":
##    l = BM_find(T,P)
##    final += l
##    T = inf.readline()
##s = 0
##n = 1000
##for i in range (n):
##  e = time.time()
##  l = BM_find(T,P)
##  f = time.time()
##  s += f-e
##print(l)
##print(len(l))
##print(s/n)


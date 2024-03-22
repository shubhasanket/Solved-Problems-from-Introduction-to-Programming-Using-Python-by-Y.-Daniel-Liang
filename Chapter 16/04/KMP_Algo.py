"""KMP Algorithm
https://www.youtube.com/watch?v=5i7oKodCRJo
"""
import time
# The failure function
def fail_func(s):
##    print(s)
    l = []
    for i in range(1,len(s)+1):
##        print(s[:i])
        a = set()
        b = set()
        for j in range(1,i):
            a.add(s[:j])
            b.add(s[j:i])
##        print(a)
##        print(b)
        temp = a & b
##        print(temp)
        if temp: # temp is not empty
            l.append(len(max(temp)))
        else: # temp is empty
            l.append(0)
##        print()
    return l
        
##print(fail_func("amalgamation"))  

def KMP_find(T,P):
    ff = fail_func(P)
    l_T,l_P = len(T),len(P)
    i,j = 0,0
    l = []
    t1 = time.time()
    while j < l_P and i < l_T:
        if T[i] == P[j]:
            if j == l_P-1:
##                print("Solution found")
                l.append(i-(l_P-1))
                i += 1
                j = 0
            else:
                i += 1
                j += 1
        elif ff[j] == 0:
            if j != 0:
                j -= 1
            else:
                i += 1
        else:
            j = ff[j] - 1
    t2 = time.time()
    return l, t2-t1

##T = "FWEOraFWEOrabFWEOrBSEFWEOFWEOr"
##P = "FWEOr"
##print(KMP_find(T,P))        
inf = open("savitriFinal.txt", "r")
T = inf.read()
P = "SAVITRI"
##l = KMP_find(T,P)
##print(l)
##print(len(l))
##final = []
##while T != "":
##    l = BM_find(T,P)
##    final += l
##    T = inf.readline()
s1 = 0
s2 = 0
n = 100
for i in range (n):
  e = time.time()
  l,t = KMP_find(T,P)
  s2 += t
  f = time.time()
  s1 += f-e
print(l)
print(len(l))
print(s1/n)
print(s2/n)
    

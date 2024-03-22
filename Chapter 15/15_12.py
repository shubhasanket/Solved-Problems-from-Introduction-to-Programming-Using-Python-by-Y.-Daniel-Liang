def largest(l):
    return largestHelper(l, l[0])

def largestHelper(l,m,i=0):
    if i == len(l)-1:
        return m
    i += 1
    if m < l[i]:
        m = l[i]
    return largestHelper(l,m,i)

l = [1,5,99,22,33,66,45,95,1,2,3,4,5555,6,7,8,9,999,1123,156,777]
print(largest(l))
        
        

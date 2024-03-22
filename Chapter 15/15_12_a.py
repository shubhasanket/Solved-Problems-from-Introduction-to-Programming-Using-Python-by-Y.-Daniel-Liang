def largest(l,i=None,j=1):
    if i == None:
        try:
            i = l[0]
        except:
            return "The list is empty"
    
    if j == len(l):
        return i
    elif l[j] > i:
        i = l[j]
    return largest(l,i,j+1)

l = [1,2,3,4,5,6,7,8,9]
l =[]
print(largest(l))

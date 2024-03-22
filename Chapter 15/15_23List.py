#15-23 String permutation - return a list containing all the permutations

def displayPermutation(s):
    plist = []
    displayPermutationHelper("",s,plist)
    return plist

def displayPermutationHelper(s1, s2,plist):
    '''
    uses a loop to move a character from s2 to s1 and recursively invokes
    it with a new s1 and s2 . The base case is that s2 is empty and prints s1 to the
    console.)
    '''
    if s2 == "":
        plist.append(s1)
        return #s1
    for i in range(len(s2)):
        displayPermutationHelper(s1 + s2[i], s2[0:i] + s2[i+1:],plist)

a = displayPermutation("abc") 
b = displayPermutation("123") 
print(a)
print(b)
print(displayPermutation("ab"))


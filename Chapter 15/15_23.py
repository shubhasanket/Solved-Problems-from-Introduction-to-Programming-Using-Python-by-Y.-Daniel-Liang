#15-23 String permutation

def displayPermutation(s):
    return displayPermutationHelper("",s)

def displayPermutationHelper(s1, s2):
    '''
    uses a loop to move a character from s2 to s1 and recursively invokes
    it with a new s1 and s2 . The base case is that s2 is empty and prints s1 to the
    console.)
    '''
    if s2 == "":
        print(s1)
        return 
    for i in range(len(s2)):
        displayPermutationHelper(s1 + s2[i], s2[0:i] + s2[i+1:])

displayPermutation("abc") 
displayPermutation("123") 


'''(Find the number of uppercase letters in a string)
Write a recursive function to return the number of uppercase
letters in a string using the following function headers:
def countUppercase(s):
def countUppercaseHelper(s, high):
'''

def countUppercase(s):
    return countUppercaseHelper(s,n=0)

def countUppercaseHelper(s,n):
    if len(s) == 0:
        return n
    else:
        if s[0].isupper():
            n += 1
        return countUppercaseHelper(s[1:],n)

print(countUppercase("AbMasjsaMNNNP"))

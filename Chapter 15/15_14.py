'''(Occurrences of a specified character in a string)
Rewrite Exercise 15.10 using a helper function to pass
the substring of the high index to the function.
The helper function header is:
def countHelper(s, a, high):
'''

def count(s,a):
    return countHelper(s.upper(),a.upper(),n=0)

def countHelper(s,a,n):
    if len(s) == 0:
        return n
    else:
        if s[0] == a:
            n += 1
        return countHelper(s[1:],a,n)

print(count("Weeeeeeeeeeelcome", "e"))

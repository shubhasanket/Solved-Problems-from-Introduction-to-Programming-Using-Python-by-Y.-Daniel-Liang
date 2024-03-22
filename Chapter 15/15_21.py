'''(Binary to decimal) Write a recursive function that parses a binary
number as a string into a decimal integer. The function header is as
follows: def binaryToDecimal(binaryString):
Write a test program that prompts the user to enter a binary string and displays its
decimal equivalent.
'''

def binaryToDecimal(s):
    s = s[::-1]
##    print(s)
    return binaryToDecimalHelper(s,n=0,i=0)

def binaryToDecimalHelper(s,n,i):
    if i == len(s):
        return n
    else:
        return binaryToDecimalHelper(s,n+eval(s[i])*2**(i),i+1)

print(binaryToDecimal("10000000000"))

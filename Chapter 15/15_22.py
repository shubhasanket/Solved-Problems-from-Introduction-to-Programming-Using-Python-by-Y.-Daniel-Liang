'''(Hex to decimal) Write a recursive function that parses a
hex number as a string into a decimal integer. The function header
is as follows:
def hexToDecimal(hexString):
Write a test program that prompts the user to enter a hex string
and displays its decimal equivalent.
'''
l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def hexToDecimal(s):
    return hexToDecimalHelper(s[::-1],i=0, m=0)

def hexToDecimalHelper(s,i,m):
    if i == len(s):
        return m
    else:
        return hexToDecimalHelper(s,i+1,m+(l.index(s[i]))*(16**(i)))

print(hexToDecimal('ABCDEF123456789'))

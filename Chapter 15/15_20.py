'''(Decimal to hex) Write a recursive function that converts a decimal
number into a hex number as a string. The function header is as follows:
def decimalToHex(value):
Write a test program that prompts the user to enter a decimal number and dis-
plays its hex equivalent.
'''
l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def decimalToHex(n):
    if n == 0:
        return 0
    return decimalToHexHelper(n,s='')

def decimalToHexHelper(n,s):
    if n == 0:
        return s
    else:
        return decimalToHexHelper(n//16, l[n%16]+s)

print(decimalToHex(1522))
        

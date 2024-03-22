'''(Decimal to binary) Write a recursive function that converts
a decimal number into a binary number as a string. The function
header is as follows:
def decimalToBinary(value):
'''

def decimalToBinary(n):
    if n == 0:
        return 0
    return decimalToBinaryHelper(n, m ='')

def decimalToBinaryHelper(n,m):
    if n == 0:
        return m

    else:
        return decimalToBinaryHelper(n//2, str(n%2)+m)

print(decimalToBinary(0))

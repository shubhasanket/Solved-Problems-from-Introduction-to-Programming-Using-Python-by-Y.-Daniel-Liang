"""(Print the digits in an integer reversely) Write a recursive function that displays
an integer value reversely on the console using the following header:
def reverseDisplay(value):
For example, invoking reverseDisplay(12345) displays 54321. Write a test
program that prompts the user to enter an integer and displays its reversal.
"""
import math

##def reverseDisplay(n, m = 0):
##    if math.floor(math.log(n, 10)) == 0:
##        return m+(n%10)*(10**math.floor(math.log(n, 10)))
##     
##    return reverseDisplay(n//10, m+(n%10)*(10**math.floor(math.log(n, 10))))
##
##print(reverseDisplay(12345455993214))

def reverseDisplay(n, m = 0):
    if n == 0:
        return m
    else:
        return reverseDisplay(n//10, m*10 + n%10)

def main():
    n = 100090005
    if n%10 == 0:
        n = n*10 + 1
        a = reverseDisplay(n)
        b = str(a)[1:]
##        b = eval(b[1:])
        print(b)
    else:
        print(reverseDisplay(n))
##print(reverseDisplay(10009000))
main()

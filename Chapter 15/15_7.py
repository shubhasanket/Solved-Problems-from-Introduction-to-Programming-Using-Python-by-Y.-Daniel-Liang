'''(Fibonacci series) Modify Listing 15.2 so that the program
finds the number of times the fib function is called.
(Hint: Use a global variable and increment itevery time the
function is called.)
'''
global x
x = 0
def fib(n):
    global x
    x += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(35)
print("The function fib has been invoked", x, "time" if x == 1 else "times") 

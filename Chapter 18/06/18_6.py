"""18.6 (Match grouping symbols) A Python program contains various pairs
of grouping symbols, such as: Parentheses: ( and ). Braces: { and }.
Brackets: [ and ].
Note that the grouping symbols cannot overlap. For example, (a{b)} is
illegal. Write a program to check whether a Python source-code file has
correct pairs of grouping symbols. Your program should prompt the user
to enter a file name.
"""

from Stack import Stack    
                
def check(filename):  
    inf = open(filename, "r")
    r = inf.read()
    left = ["[","(","{"]
    right = ["]",")","}"]
    a = Stack()
    for u in r:
        if u in left:
            a.push(u)
##            print(a)
        elif u in right:
##            print(u)
            pos = right.index(u)
##            print(left[pos],a.peek(),a.isEmpty())
            if (not a.isEmpty() and (left[pos] == a.peek())):
##                print
                a.pop()
            else:
                return False
##        print("..",a)
    if a.isEmpty():
        return True
    else:
        return False

def main():
##    filename = input("Input file name: ")
    print("The grouping symbols match:",check("Input.txt"))

if __name__ == "__main__":
    main()

'''18.7 (Postfix notation) Postfix notation is a way of writing expressions
without using parentheses. For example, the expression (1 + 2) * 3 would be
written as 1 2 + 3 *. A postfix expression is evaluated using a stack. Scan
a postfix expression from left to right. A variable or constant is pushed to
the stack. When an operator is encountered, apply the operator with the top
two operands in the stack and replace the two operands with the result. The
following diagram shows how to evaluate 1 2 + 3 *.
'''
from Stack import Stack

def eval_postfix(s):
    a = Stack()
    l = ["+","-","*","/","^"]
    i = 0
    while i < len(s):
        if s[i] not in l:
            t = ''
            while s[i] not in l:
                t += s[i]
                i += 1
            a.push(t)
##            print(a)
        else:
            try:
                x2 = a.pop()
                x1 = a.pop()
                x = eval(x1+u+x2)
                a.push(str(x))
##                print(a)
            except:
##                print(a)
                print("Invalid Postfix notation")
                return
##    print(a)
    if a.getSize()==1:
        return a.pop()
    else:
        print("Invalid Postfix notation")

def main():
    s1 = "3-2*(7/2 -7)+8-4*(((9-8)/88)-5)*4"
    print(eval_postfix("8844/"))

if __name__ == "__main__":
    main()
        

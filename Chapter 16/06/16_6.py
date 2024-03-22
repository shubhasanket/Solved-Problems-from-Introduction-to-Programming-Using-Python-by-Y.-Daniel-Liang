"""(Execution time for GCD) Write a program that obtains the execution time
for finding the GCD of every two consecutive Fibonacci numbers from the
index 40 to index 45 using the algorithms in Listings 16.2 and 16.3.
Your program should print a table like this:
"""
import time
from tabulate import tabulate

# Find gcd for integers m and n
def gcd_16_3(m,n):
    if m%n == 0:
        return n
    else:
        return gcd_16_3(n, m%n)

def gcd_16_2(m,n):
    gcd = 1

    if m%n == 0:
        return n
    
    for k in range (int(n/2),0,-1):
        if m % k == 0 and n % k == 0:
            gcd = k
            break
        
    return gcd
            
    
def fib(n):
    d = {}
    d[0] = 0
    d[1] = 1
    d[2] = 1

    if n == 0:
        return d[0]
    elif n == 1:
        return d[1]
    elif n == 2:
        return d[2]

    for i in range (3, n+1):
        d[i] = d[i-1] + d[i-2]

    return d

def chrono(func,m,n):
    starttime = time.time()
    func(m,n)
    time.sleep(3)
    endtime = time.time()
    return endtime - starttime

##print(fib(45))

def main():
    n = 46
    d = fib(n)
    l2 = [] # the timings
    for i in range (n-6, n):
        l2.append([])
        l2[-1].append(chrono(gcd_16_2,i+1,i))
        l2[-1].append(chrono(gcd_16_3,i+1,i))
##        print(".........")

    index = [str(i) for i in range (n-6,n)]

    head = ["Algorithm"] + index
    print(head)
    data_for_table = [["16.2 GCD1"],["16.3 GCD2"]]
    data_for_table[0] += [x[0] for x in l2]
    data_for_table[1] += [x[1] for x in l2]
##    print(l2)
    print(data_for_table)
    print(tabulate(data_for_table, headers = head, tablefmt ="grid"))
   
main()   

   
            


    
    


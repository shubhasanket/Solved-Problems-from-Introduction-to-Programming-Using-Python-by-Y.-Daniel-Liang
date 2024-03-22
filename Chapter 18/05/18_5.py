"""18.5 (Use the Stack class) Write a program that displays the first
50 prime numbers in descending order. Use a stack to store prime
numbers
"""
from Stack import Stack

def main():
    n = 50
    primes = [True for i in range(n+1)] # prime number sieve
##    print("Done")
    #initialize primes[i] to true
##    for i in range(n+1):
##        primes.append(True)

    k = 2
    r = n/k
    while k <= n/k:
        if primes[k]:
            for i in range(k, int(n/k)+1):
                primes[k*i] = False # k*i is not prime

        k += 1

    count = 0 # Count of the number of prime numbers found so far
    # Print prime numbers
    a = Stack()
    for i in range(2, len(primes)):
        if primes[i]:
            a.push(i)

    for i in range (a.getSize()):
        print(a.pop())

if __name__ == "__main__":
    main()           

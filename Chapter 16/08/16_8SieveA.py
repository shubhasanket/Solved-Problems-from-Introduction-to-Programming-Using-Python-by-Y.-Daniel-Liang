"""16.8 (All prime numbers up to 10,000,000,000) Write a program
that finds all prime numbers up to 10,000,000,000 and store them
in a file. There are approximately 455,052,511 such prime numbers.
"""
import time
def SieveOfEratosthenes(n):
    ouf = open("Primes.txt", "w")
    primes = [True for i in range(n+1)] # prime number sieve
##    print("Done")
    #initialize primes[i] to true
##    for i in range(n+1):
##        primes.append(True)

    k = 2
    r = n/k
    while k <= n/k:
        if primes[k]:
            i = k
            temp = k*(k-1)
            while i <= int(n/k):
                temp += k
                primes[temp] = False
                i += 1
##            for i in range(k, int(n/k)+1):
##                primes[k*i] = False # k*i is not prime

        k += 1

    count = 0 # Count of the number of prime numbers found so far
    # Print prime numbers
    for i in range(2, len(primes)):
        if primes[i]:
            count += 1
            ouf.write(str(count)+". "+str(i)+"\n")

    ouf.write("\n" + str(count) + " prime(s) less than or equal to " + str(n))
    print("\n" + str(count) + " prime(s) less than or equal to " + str(n))
    ouf.close()



def main():
    n = 10000000000
##    n = 10000000
    n = 10000000
    
    t1 = time.time()
    SieveOfEratosthenes(n)
    t2 = time.time()
    print(t2-t1)
    print("Done")
main()

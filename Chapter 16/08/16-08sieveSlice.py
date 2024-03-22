#This program uses sieve to find primes in the first n numbers
#Then calculates all the primes in n * n using the primes found out
#earlier. It uses the same list again and again to find the next
#primes.
#This way works even if we do not have enough memory to do the
#entier sieve for 10 billion in the memory.

#Sieve         #of primes 
#100            25 (0.00028sec)
#10000         1228   (0.0067)
#1000000   -   78498     Million      0.368     
#10000000  -  664579     10 Million
#100000000 - 5761455     100 million  37.17sec
#1000000000- 455,052,511 10 billion
import time

def sieve(n):
    # Find out all the primes in the range 1 to n * n
    # If n = 1000 - then the function will find out all the primes
    # in the range 1 to 1,000,000.

    limit = n * n    
    primeList = []   #List of primes

    #Use the usual sieve to find out the primes in the first n numbers

    primes = []      #This is the sieve
    # Prime number sieve
    # Initialize primes[i] to true
    for i in range(n + 1):
        primes.append(True)
    k = 2
    while k <= n / k:
        if primes[k]:
            for i in range(k, n//k+ 1):
                primes[k * i] = False # k * i is not prime
        k += 1
        
    count = 0 # Count the number of prime numbers found so far
    #and store the prime numbers in primeList
    for i in range(2, len(primes)):
        if primes[i]:
            count += 1
            primeList.append(i)
            
        
    start = n + 1
    #Resusing the primes sieve array
    while start < n * n:  #limit:
        primes[0]=False
        primes[1]=False
        for i in range(2,len(primes)):
            primes[i] = True

        q = (start+n+1) ** 0.5   
        for k in primeList: 
            if k > q:
                break
            s = start // k
            if k * s < start:
                s = s + 1
            for i in range(k*s - start,len(primes),k):
                primes[i] = False

        #Now check the elements in primes which are True
        for i in range(len(primes)):
            if primes[i]:
                p = i + start
                count += 1

        start = start + n
       
    return count


def main():
    n = 10
    while n <= 100000:
        start = time.time()
        c = sieve(n)
        ending = time.time()
        print(c,"primes<=",n*n,"Time=",ending-start)
        n = n * 10
main()

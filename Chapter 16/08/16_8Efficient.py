"""16.8 (All prime numbers up to 10,000,000,000) Write a program
that finds all prime numbers up to 10,000,000,000 and store them
in a file. There are approximately 455,052,511 such prime numbers.
"""
import time

def main():
    t1 = time.time()
    n = 10000000
    
    lst = [] # A list to hold prime numbers
    count = 0 # Count the number of prime numbers
    number = 2 # A number to be tested for primeness
    sqrt = 1 # Check whether number <= sqrt

    ouf = open("Primes1.txt", "w")

    while number <= n:
        # Assume the number is prime
        isPrime = True # Is the number number prime?

        if sqrt**2 < number:
            sqrt += 1

        # Test whether number is prime
        k = 0
        while k < len(lst) and lst[k] <= sqrt:
            if number % lst[k] == 0: # If true, not prime
                isPrime = False # Set isPrime to false
                break # Exit the for loop
            k += 1

        if isPrime:
            count += 1
            lst.append(number)
            ouf.write(str(count)+". "+str(number)+"\n")

        number += 1

##    ouf.close()
##    ouf = open("Primes1.txt", "a")


    print("\n" + str(count) + " prime(s) less than or equal to " + str(n))
    ouf.close()
    print(time.time()-t1)
main()

    
                
        
    

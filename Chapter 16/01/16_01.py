'''16.1 (Maximum consecutive increasingly ordered substring) Write a
program that prompts the user to enter a string and displays the maximum
consecutive increasingly ordered substring.
'''
s = input("Enter a string: ") # this is the string
d = 0
d_max = 0
index = 0
##ord_previous = ord(s[0])

for i in range (1, len(s)):
    if ord(s[i]) > ord(s[i-1]):
        d += 1
##        print("d =", d)
    else:
##        print("i =", i)
        d = 0
    if d > d_max:
##        print("...")
        d_max = d
##        print("d_max =", d_max)
        index = i-d_max

##print(d_max,index)
print(s[index:index+d_max+1])

#The complexity of this algorithm is O(n)


    

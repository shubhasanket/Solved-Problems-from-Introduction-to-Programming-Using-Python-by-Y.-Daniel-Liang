"""16.5 (Same-number subsequence) Write an O(n) program that prompts
the user to enter a sequence of integers and finds longest subsequence
with the same number.
"""
l = [2,3,4,2,2,3,4,5,5,5,5,5,6,4,3,4,5,7,8,8,8,8,8,9,6,6,6,6,6,6,6,6,6,4,3]
l = [1,6,6,6,6,4,5,5,5,5,5,3]
start = l[0]
d = 1
s = 1
j = 0
for i in range (1, len(l)):
    if l[i] == start:
        d += 1
        if d > s:
            s = d
            j = i - d + 1
    else:
        start = l[i]
        d = 1

print("The longest same number sequence starts at index", j, "with", s,"values of", l[j])
        
         

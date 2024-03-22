'''(Maximum increasingly ordered subsequence) Write a program that
prompts the user to enter a string and displays the maximum increasingly
ordered subsequence of characters. Analyze the time complexity of your
program.
'''

s = input("Enter the string: ") # input string
l = [] # list to store the subsequence of characters
d = 0
index = 0

for i in s:
    if not len(l): # for the first iteration
        l.append(i)
        continue
    check = False
    for j in range (len(l)):
    # check if i can be added to any of the substrings in l
##        if ord(i) >= ord(l[j][-1]):
        if i >= l[j][-1]:
            l[j] += i
            check = True # if it i
            if len(l[j])>d:
                d = len(l[j])
                index = j

    if not check:# add if letter not added to any substring
        l.append(i)
    
print(l[index])
print(l)
# Welcabocdoefg

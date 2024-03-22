"""16.3 (Pattern matching) Write a program that prompts the user
to enter two strings and tests whether the second string is a
substring in the first string. Suppose the neighboring characters
in the string are distinct. (Don’t use the find method in the str
class.) Analyze the time complexity of your algorithm. Your
algorithm needs to be at least O(n) time.
"""
##s1, s2 = input("Enter the 2 strings: ").split()
s1 = "HeloKAJHdUGQEdygpwejpfoiwhetguivbhc bCHWEVjjewvkWVEGfwHBEFPython"
s2 = "vbhc "
check = False
for i in range (len(s1)):
    if s1[i] == s2[0] and (i+len(s2)-1)<len(s1):
        # if the first element of s2 == s[i] and
        # s1[i:i+len(s2)] raises no index error
        if s1[i:i+len(s2)] == s2:
            check = True

    if check == True:
        print("Matched at index:",i)
        break
            
##print("It is a substring") if check == True else print("It is not a substring") 
##print(check)  
##print(s2 in s1)
if check == False:
    print("No match found")


#Time complexity O(n)
# Did not take "Suppose the neighboring characters"
#"in the string are distinct" into consideration


'''(Occurrences of a specified character in a string) Write a recursive function that
finds the number of occurrences of a specified letter in a string using the following
function header.
def count(s, a):
For example, count("Welcome", 'e') returns 2. Write a test program that
prompts the user to enter a string and a character, and displays the number of
occurrences for the character in the string.
'''
def count(s, a):
    n_s = len(s)
    n_a = len(a)

    if n_a > n_s:
##        print(n_a, n_s)
        return 0
    
    return int(a.lower() == s[:n_a].lower()) + count(s[n_a:], a)

print(count("welcomeeeeeeeee", "eee"))

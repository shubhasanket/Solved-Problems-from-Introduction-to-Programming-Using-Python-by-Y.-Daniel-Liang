'''Reading a text file and writing back to another by keeping a
fixed line length
'''

import os.path
import random
import sys

MIN = 30

def main():
    while True:
        in_fname = input("Enter a file name:").strip()
        if os.path.isfile(in_fname):
            break

    while True:
        length = eval(input(("Enter the number of characters you want per line (minimum " + str(MIN) +"): ")))
        if (length < 0) or type(length) != int or length < MIN:
            continue
        else:
            break
        
    out_fname = "Done.txt"

    # Reading data from the file 
    infile = open(in_fname, "r")
    lst = infile.readlines()
    infile.close()
##    print(lst)

    s = '' # String which will contain the entire text
    for u in lst:
       s += u.strip() + ' '
##    s = s.strip()
##    print(s)

    lst_space = [] #List of the indexes of spaces in s
    for i in range (len(s)):
        if s[i].isspace():
            lst_space.append(i)
##    lst_space.append(len(s)-lst_space[-1])


    lst_divisions = [] #List of indexes where the split will be made
    j = length
    for i in range(len(lst_space)):
        if lst_space[i] > j:
            lst_divisions.append(lst_space[i-1])
##            print(lst_space[i]//length)
##            print(lst_space[i-1])
            j = lst_space[i-1] + length
##    print(lst_divisions)
    
    # lst_final will contain slices of the the string s.
    # lst_final will be later formatted
    lst_final = []
    lst_final.append(s[:lst_divisions[0]].strip())
    
    for i in range (len(lst_divisions)-1):
        lst_final.append(s[lst_divisions[i]+1:lst_divisions[i+1]].strip())
##        if len(lst_final[i+1]) > length:
##            print("PROBLEM")
##            sys.exit()

    lst_final.append(s[lst_divisions[-1]: ].strip())

    # Running the format_to_length method on every element of lst_final
    for i in range (len(lst_final)-1):
        lst_final[i] = format_to_length(lst_final[i], length)
        lst_final[i].lstrip()
        lst_final[i] += "\n"
    lst_final[-1].lstrip()
    lst_final[-1] += "\n"

    # Writing to the output file
    outfile = open(out_fname, "w")
    for u in lst_final:
##        print(u)
        outfile.write(u)
    outfile.close()

    print("Done")


def format_to_length(string, length):
    ls = len(string)
    count_spaces = string.count(" ")#number of spaces in the string

    #the definition of num_spaces illutrates the significance of total_cycle
    total_cycle = (length-ls)//count_spaces
    
    num_spaces = (total_cycle + 1)*' '
    s_new = string.replace(' ', num_spaces)

    spaces = [] #Contains the indexes of the spaces in the list
    spaces.append(s_new.index(num_spaces))
    j = spaces[-1]
    temp_s_new = s_new[j+1:] #Creating a temporary variable for s_new
##    print(temp_s_new)
    while j != len(s_new):
##        print("j = ",j)
        if temp_s_new.find(num_spaces) != -1:
            n = s_new.index(num_spaces, j+1)
            temp_s_new = s_new[n+1:]
            spaces.append(n)
            j = n
##            print(temp_s_new)
        else:
            j = len(s_new)     
            
    rem = length - len(s_new)
##    print("rem", rem)
    #randomly picking spaces in s_new to add the remaining spaces
    ran_picks = random.sample(spaces,rem)
    ran_picks.sort()

    for i in range (len(ran_picks)):
        temp = ran_picks.pop()
        s_new = s_new[:temp] + " " + s_new[temp:]

##    print(s_new)
    return s_new

##print("Done")

main()

'''
(Remove text) Write a program that removes all the occurrences of a specified
string from a text file. Your program should prompt the user to enter a filename
and a string to be removed.
'''

import os.path

while True:
    in_fname = input("Enter a file name:").strip()
    if os.path.isfile(in_fname):
        break

s_rem = input("Enter the string to be removed: ").strip()

##in_fname = "Text.txt"
##s_rem = "Science"
out_fname = "Done.txt"

infile = open(in_fname, "r")
s = infile.read()
infile.close()

s_new = s.replace(s_rem, '')
##print(s_new)
##print(repr(s_new))

outfile = open(out_fname, "w")
outfile.write(s_new)
outfile.close()

##n_lst = []
##
##for u in lst:
##    n_lst.append(u.split())
####print(n_lst)
##
##outfile = open(out_fname, "w")
##
##for v in n_lst:
##    while s_rem in v:
##        v.remove(s_rem)
##    outfile.write(' '.join(v)+ "\n")
##outfile.close()
        
##outfile = open(out_fname, "w")
##print()

##print(n_lst)
    
        

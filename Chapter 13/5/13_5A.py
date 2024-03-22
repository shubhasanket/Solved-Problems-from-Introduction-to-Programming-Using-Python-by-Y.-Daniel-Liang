'''(Replace text) Write a program that replaces text in a file. Your program should
prompt the user to enter a filename, an old string, and a new string.
'''

import os.path

while True:
    in_fname = input("Enter a file name:").strip()
    if os.path.isfile(in_fname):
        break

s_old = input("Enter the old string to be replaced: ").strip()
s_new = input("Enter the new srting to replace the old string: ").strip()

out_fname = "Done.txt"

infile = open(in_fname, "r")
s = infile.read()
infile.close()

s_upd = s.replace(s_old, s_new)
##print(s_upd)

outfile = open(out_fname, "w")
outfile.write(s_upd)
outfile.close()


    
##table = s.maketrans(s_old, s_new, "")
##print(table)
##
##s_new = s.translate(table)
##
##print(s_new)

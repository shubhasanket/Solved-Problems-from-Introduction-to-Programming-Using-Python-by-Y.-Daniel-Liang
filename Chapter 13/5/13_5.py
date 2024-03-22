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

table = s.maketrans(s_old, s_new, "")
print(table)

s_new = s.translate(table)

print(s_new)

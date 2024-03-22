s = "abcdefghijklmopqrstuvwxyz\n"
d = {}
for i in s:
##    if i.isalpha():
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

a = ord('a')
for i in range (26):
    if chr(a+i) in d:
        j = d[chr(a+i)]
    else:
        j = 0
    print(chr(a+i) + " appears " + str(j) + " times")

s = "14_4_readline.py"
inf = open(s, 'r')
a = inf.readline()
while a != '':
    print(a)
    a = inf.readline()
inf.close()

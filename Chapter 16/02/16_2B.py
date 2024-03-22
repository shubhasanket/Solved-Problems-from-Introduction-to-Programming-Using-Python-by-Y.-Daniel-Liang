from bisect import bisect_left

##a = [2,6,3,40,111,2,9,5,8,7,11,2,3,20]
##a = [10,12,11,15,13,0]
a = 'AWAelcabocdonmpefgnmrtzwe'
##a = 'AaAWelcaAbozprwtuvwzxy'
s = [a[0]]
l = [[a[0]]]# list to store substrings of each size till the largest size
print(a)
print(s,a[0])

for i in range(1,len(a)):
    d = a[i]
    #if d > last element of s - append d to s
    if d > s[-1]:
        s.append(d)
        # added the 
        l.append([]+l[-1])
        l[-1].append(d)

    else:
        #Find the position of smallest element in s which is >= to d
        #and replace it with d
        position = bisect_left(s,d)
        print(position, s[position])
        temp = position
        # adding this while loop
        while s[temp] == d and temp != len(s)-1:
            temp += 1
        s[temp] = d
        # this check is necessary for altering the elements in l
##        if temp == len(s)-1 and l[-1][-2] <= d:
##            l[-1][-1] = d
##        print(temp, s[temp])
        # adding the for loop
##        pos = bisect_left(l[temp],d)
##        while l[temp][pos] == d:
##            pos += 1
##        print(l[temp],pos)
        if l[temp][-2] < d:
            l[temp][-1] = d


    print(s,d)
    print(l,d)
print("S=",s)
print("l=",l)
print(len(s), len(l[-1]))

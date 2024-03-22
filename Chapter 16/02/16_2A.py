from bisect import bisect_left

##a = [2,6,3,40,111,2,9,5,8,7,11,2,3,20]
##a = [10,12,11,15,13,0]
##a = 'AWAelcabocdonmpefgnmrtzwe'
a = 'AAWAelcabo'
s = [a[0]]
l = [[a[0]]]# list to store substrings of each size till the largest size
print(a)
print(s,a[0])

for i in range(1,len(a)):
    d = a[i]
    #if d > last element of s - append d to s
    if d >= s[-1]:
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
        while s[temp] == d:
            temp += 1
        s[temp] = d
        print(temp, s[temp])
        # adding the for loop
        for i in range (temp, len(l)):
            pos = bisect_left(l[i],d)
            print(l[i],pos)
            # adding the while loop
            while l[i][pos] == d:
                pos += 1
            l[i][pos] = d


    print(s,d)
    print(l,d)
print("S=",s)
print("l=",l)

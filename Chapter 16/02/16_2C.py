from bisect import bisect_left

##a = [2,6,3,40,111,2,9,5,8,7,11,2,3,20]
##a = [10,12,11,15,13,0]
a = 'AWAelcabocdonmpefgnmrtzwe'
a = 'eQripAptaweEibZe'
a = 'ALsdoqiewwvIJWfjbIWFzwjkflieygeritdDQLebvKRfgvQgweqriutwpU'
##a = 'fyEqsTIUoraViPdsw'
##a = 'wliYKtrdsrxyckgHLyktyur'
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
##        print(position, s[position])
##        position
        # adding this while loop
        while s[position] == d and position != len(s)-1:
            position += 1
        s[position] = d
        
        if position > 0:
            if l[position][-2] <= d:
                l[position][-1] = d
        else:
            if l[position][0] > d:
                l[position][0] = d
##        if position == len(s)-1 and l[-1][-2] <= d:
##            l[position][-1] = d
        # this check is necessary for altering the elements in l
        for i in range (len(l)-2,-1,-1):
##            if i != position:
                if l[i][-1] <= d:
                    print(l[i])
                    r = [] + l[i]
    ##                print(r.append(1))
    ##                print(r)
                    r.append(d)
                    print(r)
                    l[i+1] = r
##        
##        print(temp, s[temp])
        # adding the for loop
##        pos = bisect_left(l[temp],d)
##        while l[temp][pos] == d:
##            pos += 1
##        print(l[temp],pos)
        


    print("s=",s,d)
    print("l=",l,d)
    print()
print("S=",s)
print("l=",l)
print(len(s), len(l[-1]))

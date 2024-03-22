from bisect import bisect_left,bisect_right

##a = [2,6,3,40,111,2,9,5,8,7,11,2,3,20]
##a = [10,12,11,15,13,0]
a = 'AWAelcabocdonmpefgnmrtzwe'
##a = 'eQripAptaweEibZe'
a = 'ALsdoqiewwvIJWfjbIWFzwjkflieygeritdDQLebvKRfgvQgweqrKJWielrtypWEhbEfmbmxwpwei'\
+'gfhklaurDQgygriirewuyqqwioplkjhgfdsazxcvbnmmiutHihwiuEDIWEfwefhoHWEOifupweyrwepWB'\
+'CDNWBWKEFlwyuecasxUWYEdiwileghieourtoeirvberwkjWieugfyvoqwyreruueoiponcbsdhvfWytw'\
+'IOEUWUOBuwiaeifuguirpowipeirwomahweEBWYODaabfraifgpweWEOOOYGUORFWEOIBWChWBEFYOWGEU'\
+'OIRPWJerouiyerBWEFbegfyuweuvfeqwrtycbsUedfpzU'
##a = 'eQripAptaweEibZeAXBYCZDaE'
a = "eQripAptaweEibZeABCEDFGHIJK"
##a = 'fyEqsTIUoraViPdsw'
##a = [2, 5, 3, 7, 11, 8, 10, 13, 6]
##a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
##a = 'wliYKtrdsrxyckgHLyktyur'
##tailtable = [0 for i in range (len(a)+1)]
def longest_substring(a,s = 'strong'):
    tailtable = [a[0]]
    l = [[a[0]]]# list to store substrings of each size till the largest size
    print(a)
    ##print(tailtable,a[0])
    if s == 'strong':
        for i in range(1,len(a)):
            d = a[i]
            #if d > last element of s - append d to s
            if d <= tailtable[0]:
                tailtable[0] = d
                l[0] = [d]

            elif d > tailtable[-1]:
                tailtable.append(d)
                r = [] + l[-1]
                r.append(d)
                l.append(r)

            else:
                #Find the position of smallest element in s which is >= to d
                #and replace it with d
                position = bisect_left(tailtable,d)
        ##        print(position, s[position])
        ##        position
                # adding this while loop
        ##        while tailtable[position] == d and position != len(tailtable)-1:
        ##            position += 1
                tailtable[position] = d
                r = []+l[position-1]
                r.append(d)
                l[position] = r
    elif s == 'weak':
        for i in range(1,len(a)):
            d = a[i]
            #if d > last element of s - append d to s
            if d < tailtable[0]:
                tailtable[0] = d
                l[0] = [d]

            elif d >= tailtable[-1]:
                tailtable.append(d)
                r = [] + l[-1]
                r.append(d)
                l.append(r)

            else:
                #Find the position of smallest element in s which is >= to d
                #and replace it with d
##                position = bisect_left(tailtable,d)
##                print(position, s[position])
                position = bisect_right(tailtable,d)
                # adding this while loop
##                while tailtable[position] == d and position != len(tailtable)-1:
##                    position += 1
                tailtable[position] = d
                r = []+l[position-1]
                r.append(d)
                l[position] = r
        
    ##    print(l)
    ##    print()
    ##    print(tailtable)
    ##    print()
##    print("S=",tailtable)
##    for u in l:
##        print(u)
    print('The largest substring is:', l[-1])
    print('Length of tailtable =',len(tailtable),'and length of the largest substring =', len(l[-1]))

longest_substring(a,s = 'weak')
longest_substring(a,s = 'strong')


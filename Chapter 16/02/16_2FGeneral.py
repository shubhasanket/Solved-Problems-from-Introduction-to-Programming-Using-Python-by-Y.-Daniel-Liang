#https://stackoverflow.com/questions/3992697/longest-increasing-subsequence

from bisect import bisect_left, bisect_right
from functools import cmp_to_key   #NEW for us

#N^2 algorithms just to check
def findLIS(s):  #increasing
  lengths = [1] * len(s)
  for i in range(1, len(s)):
    for j in range(i):
      if s[i] > s[j] and lengths[i] <= lengths[j]:
        lengths[i] += 1
  return max(lengths)

def findLISNon(s):  #non decreasing
  lengths = [1] * len(s)
  for i in range(1, len(s)):
    for j in range(i):
      if s[i] >= s[j] and lengths[i] <= lengths[j]:
        lengths[i] += 1
  return max(lengths)

"""
Return the longest increasing subsequence of `seq`.

Parameters
----------
seq : sequence object
  Can be any sequence, like `str`, `list`, `numpy.array`.
mode : {'strict', 'strictly', 'weak', 'weakly'}, optional
  If set to 'strict', the subsequence will contain unique elements.
  Using 'weak' an element can be repeated many times.
  Modes ending in -ly serve as a convenience to use with `order` parameter,
  because `longest_sequence(seq, 'weakly', 'increasing')` reads better.
  The default is 'strict'.
order : {'increasing', 'decreasing'}, optional
  By default return the longest increasing subsequence, but it is possible
  to return the longest decreasing sequence as well.
key : function, optional
  Specifies a function of one argument that is used to extract a comparison
  key from each list element (e.g., `str.lower`, `lambda x: x[0]`).
  The default value is `None` (compare the elements directly).
index : bool, optional
  If set to `True`, return the indices of the subsequence, otherwise return
  the elements. Default is `False`.

Returns
-------
elements : list, optional
  A `list` of elements of the longest subsequence.
  Returned by default and when `index` is set to `False`.
indices : list, optional
  A `list` of indices pointing to elements in the longest subsequence.
  Returned when `index` is set to `True`.
"""



def longest_subsequence(seq, mode='strictly', order='increasing',
                        key=None, index=False):

  bisect = bisect_left if mode.startswith('strict') else bisect_right

  # compute keys for comparison just once
  rank = seq if key is None else map(key, seq)
  if order == 'decreasing':
    rank = map(cmp_to_key(lambda x,y: 1 if x<y else 0 if x==y else -1), rank)
  rank = list(rank)

  if not rank: return []

  lastoflength = [0] # end position of subsequence with given length
  predecessor = [None] # penultimate element of l.i.s. ending at given position

  for i in range(1, len(seq)):
    # seq[i] can extend a subsequence that ends with a lesser (or equal) element
    j = bisect([rank[k] for k in lastoflength], rank[i])
    # update existing subsequence of length j or extend the longest
    try: lastoflength[j] = i
    except: lastoflength.append(i)
    # remember element before seq[i] in the subsequence
    predecessor.append(lastoflength[j-1] if j > 0 else None)

  # trace indices [p^n(i), ..., p(p(i)), p(i), i], where n=len(lastoflength)-1
  def trace(i):
    if i is not None:
      yield from trace(predecessor[i])
      yield i
  indices = trace(lastoflength[-1])

  return list(indices) if index else [seq[i] for i in indices]


def shubh(a,s = 'strong'):
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
                position = bisect_right(tailtable,d)
##              in case bisect right does not work, replace it with the following 4 lines
##                position = bisect_left(tailtable,d)
                # adding this while loop
##                while tailtable[position] == d and position != len(tailtable)-1:
##                    position += 1
                tailtable[position] = d
                r = []+l[position-1]
                r.append(d)
                l[position] = r
                
    return (len(l[-1]), l[-1])    
##    return l




##a = [2,6,3,40,111,2,9,5,8,7,11,2,3,20]
##a = [10,12,11,15,13,0]
a = 'AWAelcabocdonmpefgnmrtzwe'
a = 'eQripAptaweEibZe'
a = 'ALsdoqiewwvIJWfjbIWFzwjkflieygeritdDQLebvKRfgvQgweqrKJWielrtypWEhbEfmbmxwpwei'\
+'gfhklaurDQgygriirewuyqqwioplkjhgfdsazxcvbnmmiutHihwiuEDIWEfwefhoHWEOifupweyrwepWB'\
+'CDNWBWKEFlwyuecasxUWYEdiwileghieourtoeirvberwkjWieugfyvoqwyreruueoiponcbsdhvfWytw'\
+'IOEUWUOBuwiaeifuguirpowipeirwomahweEBWYODaabfraifgpweWEOOOYGUORFWEOIBWChWBEFYOWGEU'\
+'OIRPWJerouiyerBWEFbegfyuweuvfeqwrtycbsUedfpzU'
##a = 'eQripAptaweEibZeAXBYCZDaE'
##a = "eQripAptaweEibZeABCEDFGHIJK"
##a = 'fyEqsTIUoraViPdsw'
##a = [2, 5, 3, 7, 11, 8, 10, 13, 6]
##a = [0, 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15, 1,1,1,0,0,0,2,2,2,3,3,4,4,4,4,4,5,5,5,5,5,5,6,6]
##a = 'wliYKtrdsrxyckgHLyktyur'

print("Original String/List")
print(a)
print("*******")
print("LONGEST",longest_subsequence(a, mode='strictly', order='increasing',
                        key=None, index=False) )
print("SHUBH")
t = shubh(a,s = 'strong')
print(type(t))
print("Length=",t[0])
print("LONGEST",t[1])
print("*******")
print( 'findLIS',findLIS(a))
print( 'findLISNon',findLISNon(a))
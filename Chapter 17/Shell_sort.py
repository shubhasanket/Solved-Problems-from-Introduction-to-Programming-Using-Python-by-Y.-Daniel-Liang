'''Shell Sort
'''
def shellSort(lst):
    n = len(lst)
    gap = n//2

    while gap > 0:
        j = gap
        while j < n:
##            i = j-gap
            for i in range (j-gap,-1,-gap):
##            while i >= 0:
                if lst[i+gap] < lst[i]:
                    lst[i],lst[i+gap] = lst[i+gap],lst[i]
            j += 1
        gap = gap//2

lst = [2,5,4,3,6,9,7,2,3,1,66,5,33,2,0,9,8,77,6,5,797,34,23,634,4]
print(lst)
shellSort(lst)
print(lst)
                
        

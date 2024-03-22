'''17.1 (Improving quick sort) The quick sort algorithm presented in the
book selects the first element in the list as the pivot. Revise it by
selecting the median among the first, middle, and last elements in the
list.
'''

def quickSort(lst):
    quickSortHelper(lst, 0, len(lst)-1)

def quickSortHelper(lst, first, last):
    if last > first:
        pivotIndex = partition(lst, first, last)
        quickSortHelper(lst, first, pivotIndex-1)
        quickSortHelper(lst, pivotIndex+1, last)

def partition(lst, first, last):
    temp = [[lst[first],first],[lst[len(lst)//2],len(lst)//2],[lst[last],last]]
    temp.sort()
    pivot = temp[1][0] # selecting the median of temp
    lst[first],lst[temp[1][1]] = pivot, lst[first]
    low = first + 1
    high = last

    while high > low:

        while low <= high and lst[low]<= pivot:
            low += 1

        while low <= high and lst[high] > pivot:
            high -= 1

        if high > low:
            lst[high],lst[low] = lst[low],lst[high]

    while high > first and lst[high] >= pivot:
        high -= 1

    if pivot > lst[high]:
        lst[first] = lst[high]
        lst[high] = pivot
        return high
    else:
        return first

def main():
    lst = [2,3,2,5,6,1,-2,3,14,12,15,7,88,1,23,12,11,-2,-33,-5,12,2342]
    quickSort(lst)
    for v in lst:
        print(str(v) + " ", end = "")

main()
        

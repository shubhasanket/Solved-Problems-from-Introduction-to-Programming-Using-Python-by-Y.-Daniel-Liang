'''17.2 (Checking order) Write the following functions that check
whether a list is ordered in ascending order or descending order.
By default, the function checks ascending order. To check descending
order, pass descending to the ord argument in the function.
'''

def ordered(lst, order = "ascending"):
    des = True
    asc = True

    i = 0
    while i <len(lst)-1:
        if lst[i] > lst[i+1]:
            asc = False
        if lst[i] < lst[i+1]:
            des = False
        i += 1
        if not (des or asc):
            break

    ret = False
    if order == 'ascending' and asc:
        ret = True
    elif order == 'descending' and des:
        ret = True

    return ret

def main():

    l = [1,2,4,7,9,12,24,112,1112,2222,4567,89089]
    print(ordered(l,"ascending"))
    print(ordered(l,"descending"))
    l.reverse()
    print(ordered(l,"descending"))
    print(ordered(l,"ascending"))

if __name__ == "__main__":
    main()
##main()

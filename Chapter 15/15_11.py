def reverseDisplay(s):
    return reverseDisplayHelper(s, i='')

def reverseDisplayHelper(s,i):
    if s == '':
        return i
    else:
        return reverseDisplayHelper(s[1:], s[0]+i)

print(reverseDisplay("abcdefg"))

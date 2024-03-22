def sumDigits(n):
    return sumDigitsHelper(n,0)

def sumDigitsHelper(n, m):
    if n == 0:
        return m
    else:
        return sumDigitsHelper(n//10, m + n%10)

print(sumDigits(123456789))

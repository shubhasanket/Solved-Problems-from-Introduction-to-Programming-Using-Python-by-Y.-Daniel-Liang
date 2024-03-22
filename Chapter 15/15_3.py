def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

print(gcd(52721607,4629126429))

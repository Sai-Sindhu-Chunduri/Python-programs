def gcd(m,n):
    if m>n:
        return gcd(n,m)
    elif m==0:
        return n
    else:
        return gcd(n%m,m)
def lcm(m,n):
    if m>n:
        l=m
    else:
        l=n
    while True:
        if l%m==0 and l%n==0:
            break
        else:
            l=l+1
    return l
print("gcd=",gcd(3,6),"lcm=",lcm(4,8))

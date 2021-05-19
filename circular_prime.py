
n=137
dc=len(str(n))
i=0
x=10**(dc-1)
pc=0
if is_prime(n):
    while True:
        r=n%10
        n=n//10
        i+=1
        res=r*x+n
        n=res
        if is_prime(n):
            pc+=1
        print(n)
        if i==dc:
            break
    if pc==dc:
        print('circular prime')
    else:
        print('not circular prime')
else:
    print('not prime')

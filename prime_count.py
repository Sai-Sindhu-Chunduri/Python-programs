'''This program is to check the number of prime numbers and non prime numberss
   in given number.'''

n=2345
prime_count=0
non_prime_count=0
while n:
    r=n%10
    n=n//10
    factor_count=0
    for i in range(1,r+1):    #prime number logic
        if r%i==0:
            factor_count+=1
    if factor_count==2:
        prime_count+=1
    else:
        non_prime_count+=1
print(prime_count)
print(non_prime_count)

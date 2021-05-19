'''CANADA NUMBER is a number N such that the sum of squares of the digits
of N is equal to the sum of the non trivial divisors
of N,i.e.,(sum of divisors of N)1-N.
Eg:125,581,8549,16999
n=125
(1**2)+(2**2)+(5**2)=5+25=30 -->sqrsum_of_digits
1+5+25+125-1-125=30 -->non_trivial_divisors
'''

from math import sqrt
def sqrsum_of_digit(n):
    sum1=0
    while n:#12
        r=n%10#1%10-->1 
        n=n//10#1//10->0
        sum1=sum1+r**2#30
    return sum1

def non_trivial_divisors(n):
    result=0
    
    for i in range(1,int(sqrt(n))+1):#25
        if n%i==0:#25%5==0:T
            if i==n//i:#5==25//5 
                result+=i#
            else:
                result+=i+n//i#26
    return result-1-n

def is_canada(n):
    if sqrsum_of_digit(n)==non_trivial_divisors(n):
        return True
    return False
n=125
print(is_canada(n))
                

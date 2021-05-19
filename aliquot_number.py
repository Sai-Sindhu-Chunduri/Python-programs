'''Aliquot Number:An aliquot sequence is a sequence of positive integers in
   which each term is the sum of the proper divisors of the previous term.
   If the sequence reaches the number 1, it ends, since the sum of the proper
   divisors of 1 is 0.
   Eg:Input:  n = 10
      Output: 10 8 7 1 0
      Sum of proper divisors of 10 is  5 + 2 + 1 = 8.
      Sum of proper divisors of 8 is 4 + 2 + 1 = 7.
      Sum of proper divisors of 7 is 1
      Sum of proper divisors of 1 is 0
     Note that there is no proper divisor of 1.
'''

from math import sqrt
def proper_div_sum(n):
    if n==1:
        print(0,end=" ")
        return
    #To find proper divisor sum.
    sum1=0
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            if i==n//i:
                sum1+=i
            else:
                sum1+=i
                sum1+=n//i
    n=sum1-n
    print(n,end=" ")
    return proper_div_sum(n)
n=12
print(n,end=" ")
proper_div_sum(n)
    
                   

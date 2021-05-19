'''Given a number n, print all primes smaller than or equal to n. It is also
given that n is a small number.
For example, if n is 10, the output should be “2, 3, 5, 7”. If n is 20,
the output should be “2, 3, 5, 7, 11, 13, 17, 19”. '''

n=int(input())
nonprimes=[]
for i in range(2,n+1):
    if i not in nonprimes:
        print(i)
        for j in range(i*i,n+1,i):
            nonprimes.append(j)
print(nonprimes)

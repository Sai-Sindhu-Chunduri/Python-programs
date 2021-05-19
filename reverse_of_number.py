#This program is for reversing given number. 
n=12345
rev=0
#Logic for reversing a number.
while n:
    r=n%10             # 5     4    3     2     1
    n=n//10            # 1234  123  12    1     0
    rev=rev*10+r       # 5     54   543   5432  54321
    if n==0:
        break
print(rev)

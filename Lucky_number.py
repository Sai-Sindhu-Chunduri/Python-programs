'''Lucky number:If 'n' is given number,then each digit in 'n' should be
   divisible by 'n'.
   Eg:n=12
      1 and 2 are divisible by 12. 
'''

n=12
digit_count=0
temp=n
count=0
while n:
    r=n%10          # 2              1
    digit_count+=1  # 1              2
    n=n//10         # 1              0
    if temp%r==0:   # 12%2==0-->T    12%1==0-->T 
        count+=1    #1               2
if count==digit_count:   #2==2-->T
    print('Lucky number')#Lucky number 
else:
    print('Not Lucky number')

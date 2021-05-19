'''PALLINDROME NUMBER:A number 'n' is said to be palindrome number,if the digits
   in the number 'n' are reversed,the same number 'n' should be obtained.
   Eg:n=121
      121 is a pallindrome number since,even if we reverse the digits 121,
      we get 121.
'''

n=int(input())
rev=0
temp=n
#Lgic to reverse the digits of n.
while True:
    r=n%10
    n=n//10
    rev=rev*10+r
    if n==0:
        break
if temp==rev:
    print('Palindrome')
else:
    print('Not a Pallindrome')




       #OR

#X=str(n)
#if X==X[::-1]:
#    print('Pallindrome')
#else:
#    print('Not a pallindrome')

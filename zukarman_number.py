'''A ZUKERMAN NUMBER  is a number which is divisible by product of its digits.
   Eg:N=115
      1*1*5=5 and 115%5=0 '''

def is_Zukerman(n):
    product=1
    temp=n
    while n:
        r=n%10
        n=n//10
        product=product*r
    if temp%product==0:
        return True
    return False
print(is_Zukerman(115))

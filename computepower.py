#Write a program to compute a^n using recursion.
def computePower(a,n):
    if n==1:
        return a
    else:
        return a*computePower(a,n-1)
computePower(2,3)

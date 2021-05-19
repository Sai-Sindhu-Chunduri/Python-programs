#If n is even,then n=n/2
#if n is odd,then n=3*n+1
#Eg:n=3
#   10 5 16 8 4 2 1      ,when series reaches 1,stop.

'''def collatz_seq(n):
    while 1:
        if n%2==0:
            print(n//2,end=" ")
            n=n//2
        else:
            print(3*n+1,end=" ")
            n=3*n+1
        if n==1:
            break
collatz_seq(10)'''

#OR

def re_collatz_seq(n,i=1):
    if i==1:
        print(n,end=" ")
        i+=1
        return re_collatz_seq(n,i)
    if n==1:
        return
    if n%2==0:
        print(n//2,end=" ")
        n=n//2
        return re_collatz_seq(n,i)
    else:
        print(3*n+1,end=" ")
        n=3*n+1
        return re_collatz_seq(n,i)
re_collatz_seq(10)

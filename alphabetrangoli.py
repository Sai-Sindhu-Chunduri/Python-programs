import string
n=int(input())
l=[]
alph=string.ascii_lowercase
for i in range(n):
    l.append("-".join(alph[n-1:i:-1]+alph[i:n]).center(4*n-3,'-'))
for i in range(len(l)-1,-1,-1):
    print(l[i])
for j in range(len(l)):
    print(l[j])

'''Nested list max value'''
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    l[i]=list(set(l[i]))
    l[i]=max(l[i])
print(l)   

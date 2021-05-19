n=int(input())
lis=list(map(int,input().split()))
t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    sum1=sum(lis[l:r+1])
    print(sum1)

'''
OUTPUT:
5
2 5 3 1 6
3
0 4
17
1 3
9
2 4
10
'''

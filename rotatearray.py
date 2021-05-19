'''t=1   #int(input())
#n,k=map(int,input().split())
n=5
k=2
arr=[1,2,3,4,5]    #list(map(int,input().split()))
for i in range(t):
    for i in range(k):
        element=arr.pop(n-1)
        arr.insert(0,element)
for i in arr:
    print(i,end=" ")'''



'''
OUTPUT:
1
5 2 
1 2 3 4 5

4 5 1 2 3
'''

n=2
l=[1,2,3,4,5]
l=(l[-n:]+l[:-n])
print(l[-n:])
print(l[:-n])
print(l)

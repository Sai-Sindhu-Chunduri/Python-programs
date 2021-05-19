n=int(input())
s=[]
for i in range(n):
    s+=map(int,input().split(","))
s1=list(set(sorted(s)))
print("set({})".format(s1))
print(s1[-2])

'''
Sample Input:
3
1,2,1
3,2,4
1,2,1
Sample Output:
set([1, 2, 3, 4])
3
'''



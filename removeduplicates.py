'''l=list(map(int,input().split()))
print(list(set(l)))'''


l=list(map(int,input()))
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

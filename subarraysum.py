l=[11,2,1,3,4,12,10,6]
key=8
cur_sum=l[0]
i=0
for j in range(1,len(l)):
    while(cur_sum>key and i<j-1):
        cur_sum=cur_sum-l[i]
        i+=1
    if cur_sum==key:
        print(i,j-1)
        break
    if j<len(l):
        cur_sum+=l[j]
else:
    print('Not found')

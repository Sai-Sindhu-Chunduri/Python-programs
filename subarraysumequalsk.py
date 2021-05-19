#Subarray Sum Equals K
'''
nums=[4,-2,-1,1,-2,3,-3]
k=2
n=len(nums)
for i in range(n):
    x=0
    for j in range(i,n):
        x=sum(nums[i:j+1])
        if(x==k):
            c+=1
print(c)
'''

#Using prefix sum algorithm method.

nums=[4,-2,-1,1,-2,3,-3]
k=2
n=len(nums)
prefix=[0 for i in range(n)]
prefix[0]=nums[0]
for i in range(1,n):
    prefix[i]=prefix[i-1]+nums[i]
d={0:1}
count=0
for i in range(n):
    if prefix[i]-k in d.keys():
        count+=d[prefix[i]-k]
    if prefix[i] not in d.keys():
        d[prefix[i]]=1
    else:
        d[prefix[i]]+=1
print(count)

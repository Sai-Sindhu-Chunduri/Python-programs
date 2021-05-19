#Problem : Returns the count of same number in array.

nums=[1,2,3,1,1,3]
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]==nums[j]):
            count+=1
print(count)

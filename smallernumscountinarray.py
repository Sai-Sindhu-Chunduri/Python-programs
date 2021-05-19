'''Given the array nums,for each nums[i] find out how many numbersin the array
   are smaller than it.That is,for each nums[i] you have to count the number
   of valid j's such that j != i and nums[j]<nums[i].
   Return the anser in an array.
   Example:
   Input: nums=[8,1,2,2,3]
   Output: [4,0,1,1,3]
   Explanation:
   For nums[0]=8 there exists four smaller numbers than it (1,2,2,3)
   For nums[1]=1 doesnot exist any smaller number than it.
   For nums[2]=2 there exist one smaller number than it (1)
   For nums[3]=2 there exist one smaller number than it(1)
   For nums[4]=3 there exists three smaller numbers than it (1,2,2)'''

nums=[8,1,2,2,3]
l=[]
for i in range(len(nums)):
    count=0
    for j in range(len(nums)):
        if nums[i]>nums[j]:
            count+=1
    l.append(count)
print(l)




#OR  -->  This method takes less time complexity.
'''nums=[8,1,2,2,3]
arr=sorted(nums)
d={}
count=0
for i in range(len(nums)):
    if arr[i] not in d:
        d[arr[i]]=count
        count+=1
    else:
        count+=1
for i in range(len(nums)):
    nums[i]=d[nums[i]]
print(nums)'''



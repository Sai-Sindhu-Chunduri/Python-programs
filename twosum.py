'''Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.You may assume that each input
would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

'''nums=[2,7,11,15]
target=9
i=0
j=len(nums)-1
for i in range(j):
    j=len(nums)-1
    while(i<j):
        if nums[i]+nums[j]==target:
            print([i,j])
            break
        else:
            j-=1'''

nums = [2,7,11,15]
target = 9
i=0
for i in range(len(nums)-1):
    n=target-nums[i]
    if n in nums[i+1:]:
        j=nums.index(n,i)
        print(i,j)
    
        

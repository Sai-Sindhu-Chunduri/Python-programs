'''Given an array of integers nums and an integer target,returns indices of the
   two numbers such that they add up to target.You may assume that each input
   would have exactly one solution,and you may not use the same element twice.
   You can returnn the answer in any order.
   Example:
   Input:
   nums=[2,7,11,15],target=9
   Output:
   [0,1]'''

nums=[3,3]
target=6
s=0
for i in range(len(nums)):
    sum1=0
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
            s=1
    if s==1:
        break

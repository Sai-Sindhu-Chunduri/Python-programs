'''Given an array of n positive integers and a positive integer s,find the
   minimal length of a contiguous subarray of which the sum>=s.If there isn't
   one,return 0 instead.
   Example:
   Input: s=7,nums=[2,3,1,2,4,3]
   Output:2
   Explanation: the subarray[4,3] has the minimal length under the problem
'''
nums=[2,3,1,2,4,3]
s=7
i=0
cur_sum=0
z=[]
for j in range(0,len(nums)):
    cur_sum+=nums[j]
    while (cur_sum>=s):
        z.append(len(nums[i:j+1]))
        cur_sum-=nums[i]
        i+=1
print(min(z))

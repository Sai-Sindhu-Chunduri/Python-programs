
'''
Given an array of n positive integers and a positive integer s, find the
minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
one, return 0 instead.
Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem
constraint.
'''

arr=list(map(int,input("Enter the array elements").split()))
s=int(input("Enter positive integer to check"))
n=len(arr)
i=0
current_sum=0
min=999
for j in range(n):
    current_sum+=arr[j]
    while(current_sum>=s):
        if j-i<=min:
            min=j-i
            break
        i+=1
print(min)
        

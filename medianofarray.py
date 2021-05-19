'''Given two sorted arrays num1 and num2 of size m and n respectively,return
   the median of the two sorted arrays.
   Follow up:The overall run time complexity should be 0(log(m+n)).
   Example:
   Input1: nums1=[1,3],nums2=[2]
   Output1:2.00000
   Explanation: merged array=[1,2,3] and median is 2.

   Input2:num1=[1,2],nums2=[3,4]
   Output:2.50000
   Explanation: merged array=[1,2,3,4] and median is (2+3)/2
   '''
nums1=[1,2]
nums2=[3]
nums3=nums1+nums2
y=len(nums3)
if y%2==0:
    mid=y//2
    median=(nums3[mid-1]+nums3[mid])
    

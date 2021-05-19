'''Given a non-empty array of digits representing a non-negative integer,
   increment one to the integer.The digits are stored such that the most
   significant digit is at the head of the list,and each element in the
   array contains a single digit.You may assume the integer does not contain
   any leading zero,except the number 0 itself.
   Example:
   Sample Input:
   [1,2,3]
   Sample Output:
   [1,2,4]
DLLs
   '''
n=[4,3,2,1]
x=0
for i in n:
    x=x*10+i
x=x+1
l=list(map(int,str(x)))

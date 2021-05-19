'''
Program to ramove the given element from given array and print the length of
the array after removing the given element.
'''

def removeelements(nums,val):
    nums[:]=list(value for value in nums if value!=val)
    print(len(nums))
n=int(input())
nums=list(map(int,input().split()))
val=int(input())
removeelements(nums,val)


'''
SAMPLE INPUT:
4
1 2 3 4
3
SAMPLE OUTPUT:
3
'''



#OR
'''val=int(input()) #3
nums = list()
number = input() #4
for i in range(int(number)):
    n = int(input()) 
    nums.append(n)  #3 2 2 3
print(nums)
count = 0
for i in range(len(nums)):
    if nums[i] != val :
        nums[count] = nums[i]
        count +=1
print(count)'''
           
    






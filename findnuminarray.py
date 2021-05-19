'''Program to check whether a given number is present in given array or not. '''

array=[1,24,7,3,6,8,9,2]
key=9
#if 9 in array:
#    print('Yes')
#else:
#    print('No')
for i in range(len(array)):
    if array[i]==key:
        print('yes')
        break
else:
    print('No') 

#Another method plan
'''array=[1,4,7,3,6,8,5,9,2]
          i             j
    key=9
    sort the array-->[1,2,3,4,5,6,7,8,9]
    lower_bound-->i
    upper_bound-->j
    mid=(i+j)//2

    if -->array[mid]==key

    elif-->array[mid]<key
            i=mid+1
'''
#Progam for Method2
'''array=[1,4,7,3,6,8,5,9,2]
key=9
array.sort()
i=0
j=len(array)-1
while i<j:
    m=(i+j)//2
    if array[m]==key:
        print('yes')
        break
    elif array[m]<key:
        i=m+1
    else:
        j=m-1'''
    

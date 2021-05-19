#Program to print the largest sum of sub arrays from the given array.

'''
l=[-2,-3,4,-1,-2,1,5,-3]
y=0
for i in range(len(l)):
    for j in range(i,len(l)):
        x=sum(l[i:j+1])
        if x>y:
            y=x
print(y)
'''

#OR

l=[-2,-3,4,-1,-2,1,5,-3]
max_end_here=0
max_so_far=0
for i in range(len(l)):
    max_end_here+=l[i]
    if max_end_here<0:
        max_end_here=0
    if max_so_far<max_end_here:
        max_so_far=max_end_here
print(max_so_far)



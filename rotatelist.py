def rotate(lst,x):
    copy = list(lst)
    for i in range(len(lst)):
        if x<0:
            lst[i+x] = copy[i]
        else:
            lst[i] = copy[i-x]
num=[45,19,23,34,9]
rotate(num,2)
print(num)

'''
output:
[45, 19, 23, 34, 9]
'''

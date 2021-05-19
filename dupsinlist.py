def dup(l):
    s=set(l)
    for i in s:
        if l.count(i)>1:
            print(i)

dup([5,6,5,6,7,8,10,20])
dup([2,3,4,4,5,6,6,7])

'''
5
6
4
6
'''

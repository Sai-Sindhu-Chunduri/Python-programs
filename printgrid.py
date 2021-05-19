'''Write a python program that takes number of rows and columns as input,
   creates a list of lists of that shape that includes the 'row,column' of that
   location.For example,after following code is executed:(4,3)
   ([['0,0','0,1','0,2'],['1,0','1,1','1,2'],['2,0','2,1','2,3'],
    ['3,0','3,1','3,2']])
    Note these are strings.
   '''

m=int(input())
n=int(input())
l=[]
for x in range(m):
    l1=[]
    for y in range(n):
        s=str(x)+","+str(y)
        l1.append(s)
    l.append(l1)
print(l)   

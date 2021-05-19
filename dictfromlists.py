n=int(input())
l=[input() for i in range(n)]
l1=[input() for i in range(n)]
l2=[input().split() for i in range(n)]
d={}
for i in range(n):
    d[l[i]]={l1[0]:int(l2[i][0]),l1[1]:l2[i][1],l1[2]:int(l2[i][2]),}
print(d)
for k in d.keys():               #Adding new key-value pairs.
    d[k]['designation']=input()
print(d)

'''
INPUT:
3
jagadeesh
rakesh
harish
empid
dept
sal
771 it 35000
123 cse 33000
245 it 28000
OUTPUT:
{'jagadeesh': {'empid': 771, 'dept': 'it', 'sal': 35000}, 'rakesh': {'empid': 123, 'dept': 'cse', 'sal': 33000}, 'harish': {'empid': 245, 'dept': 'it', 'sal': 28000}}
Sr.Assistant Professor
Assistant Proffesor
New Joinee
{'jagadeesh': {'empid': 771, 'dept': 'it', 'sal': 35000, 'designation': 'Sr.Assistant Professor'}, 'rakesh': {'empid': 123, 'dept': 'cse', 'sal': 33000, 'designation': 'Assistant Proffesor'}, 'harish': {'empid': 245, 'dept': 'it', 'sal': 28000, 'designation': 'New Joinee'}}
>>> 

'''

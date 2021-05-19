'''Create a nested dictionary with the following input:
   Assignment_1 85 100 0.25
   Test_1 95 100 0.25
   Exam_1 95 100 0.25
   The final output should be
   {'assignment_1':{'grade':95,'total':100,'weight':0.25}
   'test_1':{'grade':95,'total':100,'weight':0.25}
   'exam_1':{'grade':95,'total':100,'weight':0.25}
'''

n=int(input())
l=[list(input().split()) for i in range(n)]
print(l)
d={}
for i in l:
    d[i[0]]={'grade':int(i[1]),'total':int(i[2]),'weight':float(i[3]),}
print(d)
for k,v in d.items():
    for i in v.keys():
        print(d[k][i])
    

n=7
m=21
l=[]
for i in range(n//2):
    l.append(('.|.'*(2*i+1)).center(m,'-'))
l.append('WELCOME'.center(m,'-'))
for i in range(len(l)-1):
    print(l[i])
for j in range(len(l)-1,-1,-1):
    print(l[j])



#OR

'''N, M = map(int,input().split(' ')) 
for i in range(1,N,2): 
    print(('.|.'*i).center(M,'-'))
print("WELCOME".center(M,'-'))
for i in range(N-2,-1,-2): 
    print(('.|.'*i).center(M,'-'))'''


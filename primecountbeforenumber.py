s=10001
seive=[1]*s
prefix=[0 for i in range(len(seive))] 
def Gen_seive():                          #Generating seive
    seive=[1 for i in range(s)]
    seive[0]=0
    seive[1]=0
    for i in range(2,int(s**0.5)+1):
        if seive[i]==1:
            for j in range(i*i,s,i):
                seive[j]=0
        prefix[i]=(prefix[i-1]+seive[i])
    '''temp=seive[:N+1]
    c=temp.count(1)
    print(c)'''
    '''n=len(seive)                          #prefix logic
    prefix=[0 for i in range(len(seive))] 
    prefix[0]=seive[0]
    for i in range(1,len(seive)):
        prefix[i]=(prefix[i-1]+seive[i])'''
Gen_seive()
#T=int(input())
#for i in range(T):
N=int(input())
print(prefix[N-1])

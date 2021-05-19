n=4
steps=[0]*(n+1)
steps[1]=1
steps[2]=2
for i in range(3,n+1):
    steps[i]=steps[i-1]+steps[i-2]
print(steps[n])

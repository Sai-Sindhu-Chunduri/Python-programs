list=[10,20,30,40,50,60,70,80,90,100]
sum=0
for i in range(0,len(list),2):
    sum+=abs(list[i]-list[i+1])
print(sum)

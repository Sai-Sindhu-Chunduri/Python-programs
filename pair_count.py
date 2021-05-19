l=[10,20,20,10,20,40,50,50,10,10,20,20]
x=list(set(l))                              #[40,10,50,20,30]
pair_count=0
for i in range(len(x)):
    pair_count+=l.count(x[i])//2
print(pair_count)

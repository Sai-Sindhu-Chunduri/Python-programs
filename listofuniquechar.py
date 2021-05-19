def unique(s):
    for i in range(len(s)+1):
        if i==len(s):
            print(-1)
        else:
            if s.count(s[i])==1:
                print(i+1)
                break
s=input()
s1=s.lower()
unique(s1)

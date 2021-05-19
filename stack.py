inputs=list(map(int,input().split()))
maxs=5
current=[]
pointer=0
while pointer<len(inputs):
    if inputs[pointer]==1:
        pointer+=1
        if len(current)!=maxs:
            current.append(inputs[pointer])
        else:
          print("Overflow")
        pointer+=1
    elif inputs[pointer]==2:
        if len(current)!=0:
            current.pop()
        else:
            print("Underflow")
        pointer+=1
    elif inputs[pointer]==3:
        for i in range(len(current)-1,-1,-1):
            print(current[i])
        pointer+=1
    else:
        print(pointer)

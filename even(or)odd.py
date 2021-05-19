#TO check whether each number is even or odd. 
n=2345
while n:
    r=n%10            # 5     4    3   2
    n=n//10           # 234   23   2   0
    if r%2==0:
        print('Even')
    else:
        print('Odd')
        

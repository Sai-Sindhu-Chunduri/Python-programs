'''CHARACTER SEQUENCE:
   print the folowing:
            A
            B C
            D E F
            G H I J
            K L M N O
'''

value=65
n=int(input())
for i in range(n):
    for j in range(0,i+1):
        ch=chr(value)
        print(ch,end=" ")
        value=value+1
    print()


#OR
'''
value='A'
for i in range(n):
    for j in range(0,i+1):
        print(value,end=" ")
        value=chr(ord(value)+1)
    print()
'''    

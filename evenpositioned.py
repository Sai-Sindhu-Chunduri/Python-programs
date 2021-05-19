#Program to print all even positioned characters in a string.
s=input()
for i in range(len(s)):
    if i%2==0:
        print(s[i],end=" ")

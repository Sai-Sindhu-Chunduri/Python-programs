'''Print the characters of a list according to the given range.'''
l=['a','b','c','d','e','f','g','h','i','j','k','l']  #OR l=list(input().split())
n=int(input())
for i in range(n):
    print(l[i:len(l):n])

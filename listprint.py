#Write a program to print the elements in an array using recursion.
def listPrint(l):
    if len(l)==0:
        return "No Element"
    else:
        print(l[0])
        listPrint(l[1:])
l=[]
n=int(input("Enter the number of elements in the list:\n"))
print("Enter the elements of the list:\n")
for i in range(n):
    l.append(int(input()))
listPrint(l)

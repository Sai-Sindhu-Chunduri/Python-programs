'''Program to print reverse of a string.
   Eg:
   Input:Aditya Engineering College
   Output:egelloC gnireenignE aytidA
'''

def reverse(str):
    s = ""
    for i in str:
        s = i + s
    return s
mystr = input("Enter a string: ")
print("Reversed String: ", reverse(mystr))


#OR
'''mystr=input("Enter a string: ")
str = mystr[::-1]
print(str)'''


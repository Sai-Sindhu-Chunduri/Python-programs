import math
a=input("Enter the first coordinate:")
x=a.split(",")
b=input("Enter the second coordinate:")
y=b.split(",")
result=math.sqrt(((int(x[0])-int(y[0]))**2)+((int(x[1])-int(y[1]))**2))
print("Distance between two points is:",result)


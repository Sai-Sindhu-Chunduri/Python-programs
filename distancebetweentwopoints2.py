import math as m
x1=int(input("Enter first point of x coordinate"))
x2=int(input("Enter second point of x coordinate"))
y1=int(input("Enter first point of y coordinate"))
y2=int(input("Enter second point of y coordinate"))
d=m.sqrt(m.pow((x2-x1),2)+m.pow((y2-y1),2))
print(d)


'''
Enter first point of x coordinate5
Enter second point of x coordinate13
Enter first point of y coordinate17
Enter second point of y coordinate18
8.06225774829855


Enter first point of x coordinate12.5
Traceback (most recent call last):
File "C:/python programs/distancebetweentwopoints2.py", line 2, in <module>
x1=int(input("Enter first point of x coordinate"))
ValueError: invalid literal for int() with base 10: '12.5'
'''

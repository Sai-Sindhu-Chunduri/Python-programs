age=int(input("Enter age"))
if age>=18:
    print("Eligible to cast a vote")
else:
    print("There are",18-age,"years left to be eligible")


'''
Enter age14
There are 4 years left to be eligible

Enter age15.2
Traceback (most recent call last):
  File "C:\python programs\vote.py", line 1, in <module>
    age=int(input("Enter age"))
ValueError: invalid literal for int() with base 10: '15.2'
'''

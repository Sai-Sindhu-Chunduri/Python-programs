l=Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> '''Take variable number of arguments and find the sum of the arguments using
   lambda'''

(lambda *args:sum(args))(1,2,3)
SyntaxError: multiple statements found while compiling a single statement
>>> '''Take variable number of arguments and find the sum of the arguments using
   lambda'''
'Take variable number of arguments and find the sum of the arguments using\n   lambda'
>>> (lambda *args:sum(args))(1,2,3)
6
>>> '''Take a variable number of keyword arguments as input and finish the sum of the values of the arguments using lambda'''
'Take a variable number of keyword arguments as input and finish the sum of the values of the arguments using lambda'
>>> (lambda *kwargs:sum(args.values()))(a=10,b=20,c=30)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    (lambda *kwargs:sum(args.values()))(a=10,b=20,c=30)
TypeError: <lambda>() got an unexpected keyword argument 'a'
>>> (lambda **kwargs:sum(args.values()))(a=10,b=20,c=30)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    (lambda **kwargs:sum(args.values()))(a=10,b=20,c=30)
  File "<pyshell#5>", line 1, in <lambda>
    (lambda **kwargs:sum(args.values()))(a=10,b=20,c=30)
NameError: name 'args' is not defined
>>> (lambda **kwargs:sum(kwargs.values()))(a=10,b=20,c=30)
60
>>> 

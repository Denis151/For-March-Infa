Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def func(*s):
 return sum(s[1] + s[1])
 
a = 1,3,5,7,9
b = 6,8,10

print(func(a,b))

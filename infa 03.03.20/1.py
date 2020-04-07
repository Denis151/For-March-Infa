Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> r = [4, 5.3, 6.6, 7.9, 9.2]
h = [4, 5.5, 7, 8.5, 10]



x = int(input())
y = int(input())

def func(h,r):
 return ((h/3*3.14) *(r*r))
print(func(r[x],h[y]))

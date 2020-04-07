Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = int(input())
b = int(input())
def funck(a,b): 
  return a*b*2-2*a

def funck_a(a,b):
  return a/b

if a > b:
 print(funck(4, 5))

else:
 print(funck_a(4, 5))

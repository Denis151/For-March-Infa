Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math

r = int(input())
a = int(input())

class KZI_V:
  v = 4/3*3.14*(r**3)
ob1 = KZI_V

b = int(input())
c = int(input())
d = int(input())

class KZI_S:
  p = (d+b+c)/2
  s = math.sqrt(p*(p-d)*(p-b)*(p-c))
ob2 = KZI_S

print(ob1.v)
print(ob2.s)

Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random

a = [1,3,4,5,6]
b1 = random.randint(1, 6)
b2 = random.randint(1, 6)
b3 = random.randint(1, 6)
b4 = random.randint(1, 6)
b5 = random.randint(1, 6)


def func(b1,b2,b3,b4,b5):
  return b1 + b2 + b3 + b4 + b5
print(func(1,2,3,4,5))

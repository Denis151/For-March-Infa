import random

a = [1,3,4,5,6]
b1 = random.randint(1, 6)
b2 = random.randint(1, 6)
b3 = random.randint(1, 6)
b4 = random.randint(1, 6)
b5 = random.randint(1, 6)


def func(b1,b2,b3,b4,b5):
  return b1 + b2 + b3 + b4 + b5
print(func(1,2,3,4,5))

import random

a = [1,3,4,5,6]
b1 = random.randint(1, 6)
b2 = random.randint(1, 6)
b3 = random.randint(1, 6)


def func(b1,b2,b3):
  return (b1**2) + (b2**2) + (b3**2)
print(func(b1,b2,b3))

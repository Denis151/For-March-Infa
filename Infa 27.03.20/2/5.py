Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = int(input())
if n == 1:
    n = "Linux"
else:
    n = "Windows"

class KZI_21:
  def __init__(self, a1="Оперционая", a2="система", a3=n):
   self.p1 = a1
   self.p2 = a2
   self.p3 = a3

ob1 = KZI_21()

print(ob1.p1, ob1.p2, ob1.p3)

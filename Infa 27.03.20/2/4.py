Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class KZI_21:
  def __init__(self, a1="Днистер", a2="Десна"):
   self.p1 = a1
   self.p2 = a2
ob1 = KZI_21("Днипро","Ворскла")
ob2 = KZI_21("Днипро")
ob3 = KZI_21("                ")
print(ob1.p1, ob1.p2)
print(ob2.p1)
print(ob3.p1)

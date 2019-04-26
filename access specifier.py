#difference between private and public and procted
class ashish:
   def __init__(self,money,name,age):
      self.__money =23455 #private access specifier
      self._age=age #procted access specifier
      self.name =name
   def getmoney(self):
       return self.__money
ashu =ashish(1223,'verma',21)
print(ashu.name)
print(ashu._age)
print(ashu.__money)
print(ashu.getmoney())

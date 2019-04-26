#Upload the error free program on LMS.
class employee:
 def __init__(self, name, sal):
 self.__name=name # private attribute
 self.__salary=sal # private attribute
>>>e1=employee("Bill",10000)
>>>e1.__salary
AttributeError: 'employee' object has no attribute '__salary'

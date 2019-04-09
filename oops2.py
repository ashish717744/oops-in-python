#declaring the class and and its function
class Ashish:
    umrao =5 # class variable
    def __init__ (self,car,age,name):
        self.car =car 
        self.age =age
        self.name =name
    def sing(self):
       print('hy i m arjit')
    def close(self):
       print('hy i m singer')

bitto =Ashish('maruti',34,'bitoto')
bitto.umrao =4
print(bitto.car)
print(bitto.age)
print(bitto.name)
print(bitto.sing())
print(bitto.umrao)
print(bitto.close())

 #class inheritance
class college:
    def __init__(self,name,location,position,fees): #what name you want to give u can give it here
       self.name=name
       self.location =location
       self.position =position
       self.fees =1223444
    def ranking(self):
       rank =int(input('enter the rank of the college'))
       return rank
    def review(self):
       review =str(input('enter the review of college'))
class college1(college): #we are using the properties of the different class in other class.
    #this class can access all the properties of that class and the object also can access all feature
    def __init__(self,name):
         self.name=name
    def run(self):
        return True
Nmit =college1('nitte')
print(Nmit.name)
Reva =college('nitte','bangalore',12,11234)# data got saved and it did not went to others 
print(Reva.location)
print(Reva.fees)
print(Nmit.ranking())
 

class room:
    def __init__(self,person):
        self.person =person
        
    def take(self):
        self.car =int(input('enter the no'))
        return self.car
    def print(self):
        return self.car
y =room('tdg')
print(y.take())
print(y.print())
print(y.person)

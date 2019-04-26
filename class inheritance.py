class userinput:
    def __init__(self):
        pass
    def money(self):
        self.currentmoney=int(input('enter the currentmoney no'))
        self.withdrawmoney=int(input('enter the withdrawmoney no'))
        return self.currentmoney,self.withdrawmoney
class employee(userinput):

    def __init__(self,name,accountno):
        print('childclass')
        self.name =name
        self.accountno =accountno

    def withdraw(self):
        if self.withdrawmoney >= self.currentmoney:
            return print('wrong no enter')
        elif self.withdrawmoney<=self.currentmoney:
            return print('money had been deducated from current balance')
        else:
            return print('cant take money')

obj1=employee('malik','12334455')
print(obj1.name,obj1.accountno)
obj1.money()
print(obj1.withdraw())

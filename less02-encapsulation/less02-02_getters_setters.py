class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


a = BankAccount('Franko', 1000)
print(a.balance)

a.balance = 'hello'
print(a.balance)


class BankAccountNew:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_blance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('only number!')

        self.__balance = value

    def del_balance(self):
        print('delete balance')
        del self.balance

    balance = property(fget=get_blance, fset=set_balance)

a = BankAccountNew('Franko', 1000)
print(a.get_blance())
a.set_balance(5555)
print(a.get_blance())

b = BankAccountNew('Vasya', 1000)

# balance = property(fget=get_blance, fset=set_balance, fdel=del_balance)
print(a.balance)
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
print(a.balance)
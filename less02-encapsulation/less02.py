# инкапсуляция
class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name  # спереди 2ное подчеркивание - защищенный аттрибут
        self.__balance = balance
        self.__passport = passport

    # def print_data(self):
    #     print(self.name, self.balance, self.passport)

    def print_protected_data(self):
        print(self.__name, self.__balance, self.__passport)


account1 = BankAccount('Mark', 10000, 'KK060403')
account1.print_protected_data()
# print(account1.__balance)
print(dir(account1))
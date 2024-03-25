# перегрузка
class Base:
    def __init__(self, a):
        self.__a = a

    def print_a(self, square=False, multiplier=None):
        if square and not multiplier:
            print(self.__a ** 2)
        elif not square and multiplier:
            print(self.__a * multiplier)
        elif square and multiplier:
            print((self.__a ** 2) * multiplier)
        else:
            print(self.__a)


base = Base(4)
base.print_a(square=True, multiplier=2)

# переопределение
class Multiplier:
    def __init__(self, a):
        self._a = a

    def print_a(self, x):
        print(self._a * x)

class Exponent(Multiplier):
    def print_a(self, x):
        print(self._a ** x)


e = Exponent(4)
e.print_a(2)

mult = Multiplier(2)
mult.print_a(3)
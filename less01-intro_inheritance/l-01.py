class Human:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name

    def get_name_and_age(self):
        return self.name, self.age



human_1 = Human(age=25, name='Mark', gender='male')
print(f'{human_1.age=}, {human_1.name=}, {human_1.gender=}')

print(human_1.get_name())
print(human_1.get_name_and_age())

class Human:
    def __init__(self, age):
        self.age = age

    def sey_hello(self):
        print('Hello, I am {}'.format(self.age))

class HumanExtended(Human):
    def __init__(self, age, name):
        super().__init__(age)  # вызов метода родительского класса
        self.name = name

    def sey_hello(self):
        print("Hello, I am {} and I'm {}".format(self.name, self.age))


human = Human(50)
human.sey_hello()

human2 = HumanExtended(age=30, name='David')
human2.sey_hello()


class Doctor:
    def can_cure(self):
        print("Я врач, я лечу")

    def can_build(self):
        print("я доктор, но я тоже немного строю")


class Architect:
    def can_build(self):
        print("я архитектор, я строю")


class Person(Doctor, Architect):  # использование одиаковых методов разных родителей - по порядку указания наследования (в скобках)
    # def can_build(self):  # переопределение метода в дочернем классе
    #     print("я тоже умею строить")
    pass




s = Person()
print(s.can_cure())
print(s.can_build())
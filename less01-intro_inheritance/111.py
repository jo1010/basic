# class Fish:
#
#
#
#     def swim(self):
#
#
#
#         print('Риба плаває')
#
#
#
#     def be_awesome(self):
#
#
#
#         print('Риба гарна')
#
#
#
# my_fish=Fish()
#
#
#
# my_fish.be_awesome()

class Dog:



    def walk(self):



        return "*walking*"



    def speak(self):



        return "woof!"



class Doberman(Dog):



    def talk(self):



        return super().speak()



lina = Doberman()



print(lina.talk())

# acitivity_1
class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am cat , My name is {self.name} , I am {self.age} years old")

    def make_sound(self):
        print("Meow")


class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name} , I am {self.age} years old")

    def make_sound(self):
        print("bark")


cat1 = cat("dodo", 2, 5)
dog1 = dog("tyson", 9)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()

    # acitivty_2


class computer:
    def __init__(self):
        self.__maxprice = 100

    def sell(self):
        print("The selling price is {}".format(self.__maxprice))

    def setmaxprice(self, price):
        self.__maxprice = price


c = computer()
c.sell()

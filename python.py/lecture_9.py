class person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class employee(person):
    def __init__(self, name, age, empid):
        self.empid = empid
        super().__init__(name, age)


a = employee("riya", 25, 1001)
a.display()


# Activity_2
class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = student("Mike", "tyson", 2025)
x.printname()
print(x.graduationyear)


# activity_3
class parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


blue = parrot("blue", 10)
woo = parrot("woo", 15)
print("blue is a {}", format(blue.__class__.species))
print("woo is a {}", format(woo.__class__.species))

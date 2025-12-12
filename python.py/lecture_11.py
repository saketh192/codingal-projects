# Activity_1
class vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage


class bus(vehicle):
    pass


school_bus = bus("School volvo", 180, 12)

print(
    "Vehicle name:",
    school_bus.name,
    "\nspeed:",
    school_bus.maxspeed,
    "\nmileage:",
    school_bus.mileage,
)


# activity_2
class person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


class employee(person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, idnumber)


a = employee("rahul", 8811, 22222, "intern")
a.display()

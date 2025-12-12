class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print(f"Hello, I am {self.name}.")
        print(f"I am a {self.model} robot.")
        print(f"My main purpose is {self.purpose}.")

# Creating an object of Robot class
robot1 = Robot("Optimus", "AI-Model X", "helping humans with daily tasks")

# Calling the introduce method
robot1.introduce()

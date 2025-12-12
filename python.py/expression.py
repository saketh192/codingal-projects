class Human:
    def __init__(self, name):
        self.name = name
        self.emotion = None

    def set_emotion(self, emotion):
        self.emotion = emotion

    def express(self):
        if self.emotion is None:
            print(f"{self.name} is not showing any expression yet.")
        else:
            print(f"{self.name} is feeling {self.emotion}.")


# Creating object
person = Human("Alex")

# Setting emotions
person.set_emotion("happy")
person.express()

person.set_emotion("sad")
person.express()

person.set_emotion("angry")
person.express()

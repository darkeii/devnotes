# Inheritence = Allows a class to inherit attributes and methods from another class
#                Helps with code reusablity and extensiblity
#                class Child(parent)

class animals:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class dog(animals):                         # now class "dog" also has all methods of class "animals"
    def speak(self):                        # along with its own methods.
        print("Woof woof")

class cat(animals):
    def speak(self):
        print("Meoww !")

class mouse(animals):
    def speak(self):
        print("Squeek")

dog = dog("scooby")
cat = cat("garfield")
mouse = mouse("stuart")

print(dog.name)
print(dog.is_alive)
dog.eat()
cat.eat()

print("------------------------------")

dog.speak()
cat.speak()
mouse.speak()


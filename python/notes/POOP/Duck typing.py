# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#                  Object must have minimum necessary attributes/methods
#                   "If it looks like a duck and quacks like duck, it must be a duck."
#
#

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    alive = False                   # we also gave the car "alive" attribute, still its not an animal but it will act as animal .... because i t has all minimum required attributes/methods which we defined an animal has in "Animal" class

    def speak(self):
        print("Honking !")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
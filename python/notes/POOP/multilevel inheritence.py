#multiple inheritence = inherit from more than one parent class
                        # C(A,B)
#
# multilevel inheritence = inherit from a parent which inherits from another parent
#                         C(B) <- B(A) <- A

class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} animal is eating")

    def sleep(self):
        print(f"{self.name} animal is sleeping")

class Prey(Animals):
    def flee(self):
        print(f"{self.name} animal is fleeing")

class Predator(Animals):
    def hunting(self):
        print(f"{self.name} animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bunny")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.hunting()
hawk.eat()
rabbit.sleep()

# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

# examples of multilevel inheritance
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# example of multiple inheritance
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


rabbit.eat()
rabbit.flee()
hawk.hunt()
hawk.eat()

fish.hunt()
fish.flee()
fish.sleep()
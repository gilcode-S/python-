# multi level inheritance

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'This {self.name} is eating')

    def sleep(self):
        print(f'This {self.name} is sleeping')


# this 2 is the parent class
class Prey(Animal):
    def flee(self):
        print(f'This {self.name}is fleeing')


class Predator(Animal):
    def hunt(self):
        print(f'This {self.name} is hunting')


# inheritance class child
class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bunny")
hawk = Hawk("eye")
fish = Fish("nemo")

fish.hunt()
fish.eat()

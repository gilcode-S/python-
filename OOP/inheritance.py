
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("woof")


class Cat(Animal):
    def speak(self):
        print("meow")


class Mouse(Animal):
    def speak(self):
        print("speek")


dog = Dog("black")
cat = Cat("garfield")
mouse = Mouse("Mickey")


print(dog.name)
print(dog.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()

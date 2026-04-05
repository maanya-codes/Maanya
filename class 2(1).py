from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        print(self.name + " bark")
    def walk(self):
        print(self.name + " is walking")

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        print(self.name + " meow")
    def walk(self):
        print(self.name + " is walking")
    

dog = Dog("scooby doo")
cat = Cat("billy")

dog.walk()
dog.sound()
cat.sound()
cat.walk()


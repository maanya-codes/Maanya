from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
    
    def details(self):
        print("Car brand is " + self.brand + " Car color is "+ self.color )

class BMW(Car):
    def __init__(self, brand, color, model):
        self.model = model
        super().__init__(brand, color)
    def start(self):
        print("Engine started")
    def stop(self):
        print("Engine stopped")
    def details(self):
        print(f"The BMW {self.model} is in {self.color} color" )

bmw1 = BMW("BMW", "black", "m5")
bmw1.details()
    

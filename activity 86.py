class Bird:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    def display(self):
        print("Name: " + self.name)
        print("color: " + self.colour)
    def sing(self):
        print(self.name + " is singing: LALALALALA")
       
class Parrot(Bird):
    def __init__(self, name, colour):
        super().__init__(name, colour)
        
    
        
parrot = Parrot("Parrot", "Black")

parrot.display()
parrot.sing()

class Vehicle:
    def __init__(self, name, max, mileage):
        self.max_speed = max
        self.mileage = mileage
        self.name = name
        print("Name: "+ name )
        print("Mileage: "+ str(mileage) )
        print("Max spd: "+str( max) )
       
class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 100, 100)

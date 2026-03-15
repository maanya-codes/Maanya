class Parrot:
    type = "Bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Name: ", name)
        print("Age: ", age)

macaw = Parrot("Bob", 67)
cockatoo = Parrot("Larry", 76)
print("Name {} and age {}".format(macaw.name, macaw.age))
print("Name {} and age {}".format(cockatoo.name, cockatoo.age))
print("Types of animals of these parrots: {}".format(Parrot.type))



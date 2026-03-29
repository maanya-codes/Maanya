class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print("Name: " + self.name)
        print("ID: " + self.id)
       
class Employee(Person):
    def __init__(self, name, id, post, salary):
        self.post = post
        self.salary = salary
        Person.__init__(self, name, id)
    def display(self):
        print("Name: " + self.name)
        print("ID: " + self.id)
        print("Salary: " + self.salary)
        print("Post: " + self.post)
    
        
person = Person("Maanya", "T1132005D")

employee = Employee("Maanya", "T1132005D", "Immunologist", "$1000000")

person.display()
employee.display()

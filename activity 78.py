class Student:
    def __init__(self, name, grade):
        self.grade = grade
        self.name = name
        print(self.name, ", your grade is ", grade)


chan = Student("chan","A")

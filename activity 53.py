
try:
    age = int(input("Enter your age: "))
except ValueError as ex:
    print(ex)
    age = int(input("Enter your age: "))
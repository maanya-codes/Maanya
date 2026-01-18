def cube(number):
    return number**3

def divby3(number):
    if number % 3 == 0:
        print(number, "is divisible by 3 and cube is", end= " ")
        return cube(number)
    else:
        return False

num = int(input("Enter a number:"))       

print(divby3(num))
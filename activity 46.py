def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def times(a, b):
    return a*b
def div(a, b):
    return a/b
def fdiv(a, b):
    return a//b
print("WELCOME TO MAANYA'S AMAZING CALCULATOR")
while True:
    print("Type A for addition")
    print("Type S for subtraction")
    print("Type M for multiplication")
    print("Type D for division")
    print("Type F for floor division")
    print("\nType E to quit program")
    cmd = input("Your choice:")
    if cmd == "E":
        print("Exiting Calculator...........")
        break
    elif cmd != "A"  and cmd != "S" and cmd != "M" and cmd != "D" and cmd != "F":
        print("Invalid input. Try again!")
        continue
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    
    if cmd == "A":
        print(f"{a} + {b} = {add(a, b)}")
    elif cmd == "S":
        print(f"{a} - {b} = {sub(a, b)}")
    elif cmd == "M":
        print(f"{a} x {b} = {times(a, b)}")
    elif cmd == "D":
        print(f"{a} / {b} = {div(a, b)}")
    elif cmd == "F":
        print(f"{a} // {b} = {fdiv(a, b)}")
    else:
        print("Invalid input. Enter")
    
    
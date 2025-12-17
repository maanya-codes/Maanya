import random
x = random.randint(1, 100)
y = int(input("Guess a number from 1 - 100:"))
while x != y:
    print("Oh you are wrong.")
    if x > y:
        print("Mystery number is greater than your answer.")
    if x < y:
        print("Mystery number is smaller than your answer.")
    y = int(input("Guess another number from 1 - 100:"))

print("Congrats you are correct!.")

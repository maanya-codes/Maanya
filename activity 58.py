import math
num = float(input("Enter a number:"))
print(f"Floor of {num} is: {math.floor(num)} ")
print(f"Ceiling of {num} is: {math.ceil(num)} ")
num2 = int(input("Enter a number:"))
print(f"Copysign of {num2} for {num} is: {math.copysign(num, num2)} ")
print(f"FAB of {num} is: {math.fabs(num)}\nABS for {num2} is: {abs(num2)} ")
print(f"Greatest common divisor of both {int(num)} & {int(num2)} is : {math.gcd(int(num), num2)} ")

num = int(input("Enter number to check:"))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print("It is an Armstrong number")
else:
    print("Not an armstrong number")
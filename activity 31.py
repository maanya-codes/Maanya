limit = int(input("Till which natural numbers to add: "))
sum = 0
i = 1
while i <= limit:
    sum += i
    i += 1

print("Sum of", limit, "natural numbers is", sum)
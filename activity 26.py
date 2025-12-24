units = int(input("Enter number of units of electricity consumed: "))

if units <= 50:
    cost = 2.6 * units 

elif units <= 100:
    cost = 130 +(3.25 * (units - 50) + 35)

elif units <= 200:
    cost = 130 + 162.5 + (5.26 * (units - 100)+ 45)

else:
    cost = 130 + 162.5 + 526 + (8.45 * (units - 200) + 75)

print("Your total bill is", cost, "rupees.")
 
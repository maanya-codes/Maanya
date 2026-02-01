days = int(input("Enter number of nights  of the trip: "))
flights = int(input("How many flights did you board: "))

print("Hotel per day: $200\nVehicle rent per day: $50\nPrice per flight: $400")


total = 200*days + flights*400 + 50*days

print("Your total is: $", total)


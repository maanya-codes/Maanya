def hotel_cost():
    print(" ============================================= ")
    print("|       Cost per night at hotel is $100       |")
    print(" ============================================= ")
    nights = int(input("How many nights will you be staying?: "))
    price = nights*100
    print("Cost is: " , price)
    return price

def car_rent():
    print(" ============================================= ")
    print("|  Porsche Rent: $1000    Toyota Rent: $500    |")
    print(" ============================================= ")
    nights = int(input("Porsche (Enter 1) or Toyota (Enter 2): "))
    if nights == 1:
        price = 1000
    elif nights == 2:
        price = 500
    print("Cost is: " , price)
    return price

def plane_cost():
    print(" ============================================= ")
    print("|   To Singapore|To Australia|To UK|To India   |")
    print(" ============================================= ")
    nights = int(input("SG (Enter 1) or AUSTRALIA (Enter 2) or UK (Enter 3) or INDIA (Enter 4): "))
    if nights == 1:
        price = 500
    elif nights == 2:
        price = 400
    elif nights == 3:
        price = 300
    elif nights == 4:
        price = 200
    print("Cost is: " , price)
    return price




print(" * + * + * + * + * + * + * + * + * + * + * + * + * + ")
print("\n               Book your Vacation!                   \n")
print(" * + * + * + * + * + * + * + * + * + * + * + * + * + ")
hotel =  hotel_cost() 
car =  car_rent()
plane = plane_cost()

total = hotel + car + plane

print("Your total is :" , total)

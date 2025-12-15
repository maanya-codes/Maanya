cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))
if (sp - cp) > 0:
    print("It is a profit of", sp - cp)
elif (sp - cp) < 0:
    print("It is a loss of", cp - sp)
else:
    print("You don't get a profit nor a loss.")
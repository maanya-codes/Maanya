name = input("Enter name:") 
age = int(input("Enter age:"))
is_cool = input("Enter True or False:")
print(f"Hello {name}!")
print(f"You are {age} years old.")
if is_cool == "True":
    value = True
else:
    value = False
if value == True:
    print("Wow you are so cool!!")
elif value == False:
    print("You ain't cool :(")

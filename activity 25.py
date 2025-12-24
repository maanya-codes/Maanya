mcause = input("Do you have a medical cause (Y / N): ")
attendance = int(input("Enter your attendance: "))
if mcause == "Y":
    print("You are allowed to take the exam")
else:
    if attendance > 75:
        print("You are allowed to take the exam")
    else:
        print("You are not allowed due to poor attendance")

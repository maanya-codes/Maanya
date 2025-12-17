# under < 18.4, <24.9 healthy
h = float(input("Enter height in m:"))
w = float(input("Enter weight in kg:"))
bmi = w / (h**2)
if bmi < 18.4:
    print("You are underweight.")
elif bmi >= 18.4 and bmi < 24.9:
    print("You are at a healthy weight")
else: 
    print("You are obese")
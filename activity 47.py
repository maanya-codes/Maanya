def total_calc(bill_amt, tip_perc):
    total = bill_amt + bill_amt * (tip_perc / 100)
    total = round(total)
    print("Your total is: $", total)

bill_amt = float(input("Enter the bill amount:"))
tip_perc = int(input("Enter the tip percentage: "))

total_calc(bill_amt, tip_perc)


    
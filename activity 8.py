total = int(input("Please enter amount to withdraw:"))
#notes: 100, 50, 10, 1
notes_100 = total//100
notes_50 = (total%100)//50
notes_10 = ((total%100)%50)//10
notes_1 = (((total%100)%50)%10)//1
print("Number of 100$ notes:", notes_100)
print("Number of 50$ notes:", notes_50)
print("Number of 10$ notes:", notes_10)
print("Number of 1$ notes:", notes_1)
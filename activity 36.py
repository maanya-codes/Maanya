num = int(input("Enter a number: "))
t = num
numLen = len(str(num))

if numLen >= 4:
    numLen = int(numLen/2)
    chk = 0
    while num > 0:
        rem = num%10
        if chk == numLen:
            midOne = rem
        elif chk == numLen -1:
            midTwo = rem
        num = int(num/10)
        chk += 1
    product = midOne * midTwo

    print("The product of mid digits of", t, "is", product)
else:
    print("This number is lesser than 4 and invalid")

def factorial(x):
    '''
    This is a recursive function to find the factorial of parameter x
    '''
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x-1)


x = int(input("Enter x to find factorials from 0 till x:"))
print(factorial.__doc__)
for i in range(0, x+1):
    print("The factorial of", i, "is:", factorial(i) )
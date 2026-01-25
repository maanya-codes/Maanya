try:
    num1, num2 = eval(input("Enter 2 numbers sep by a comma: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Numbers cannot be divided by 0")
except SyntaxError:
    print("Enter 2 numbers seperated by a comma")
except:
    print("Unknown error occurred.")
else:
    print("Wow no error!" )
finally:
    print("Run no matter what")
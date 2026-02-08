import ast
uinput = input("Enter a tuple: ")
tuplex = ast.literal_eval(uinput)
def isPalindrome(t):
    if t == t[::-1]:
        print(t, " is a palindrome")
    else:
        print(t, " is not palindrome")
try:
    if isinstance(tuplex, tuple):
        isPalindrome(tuplex)
except ValueError, SyntaxError:
    print("This is not tuple")


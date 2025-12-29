string = input("Enter a string to be reversed:")
rev = ""
for i in string:
    rev = i + rev

print("reversed string ->", rev)
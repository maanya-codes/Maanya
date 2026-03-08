names = ["chan", "minho", "changbin"]
scores = [100, 89, 0]

zip_list = list(zip(names, scores))

zip_reverse = list(zip(names, scores[::-1]))

zip_dict = dict(zip(names, scores))

for x, y in zip_list:
    print(x, y, end=", ")
print("")
for x, y in zip_reverse:
    print(x, y, end=", ")
print("")
for x in zip_dict:
    print(x,end=", ")
print("")

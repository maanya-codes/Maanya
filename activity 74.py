list1 = [1, 2, 3]
list2 = [4, 5, 6]

add = list(map(lambda x, y: x + y , list1, list2))
def square(a):
    return a**2
print(add)
sq = list(map(square, list1))

print(sq)

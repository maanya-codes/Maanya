x = ["racecar", "mom", "pencil", "oo", "r"]
def matchword(x):
    result = []
    for i in x:
        if len(i) >= 2 and i[0] == i[-1]:
            result.append(i)
    return result

print("Words in \n", x, "\nthat have >= 2 Characters and first and last chr is same: \n", matchword(x))




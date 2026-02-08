t1 = (1, 0, 0, 0, 1, 1, 0)
sunny, rainy = 0, 0
for i in t1:
    if i == 1:
        rainy += 1
    else:
        sunny += 1
if sunny > rainy:
    print("Sunny")
else:
    print("Rainy")

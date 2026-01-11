import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(500, 500)
length = int(input("Enter length of each side: "))
sides = int(input("Enter number of sides: "))
angle = 360/sides
t = turtle.Turtle()
for i in range(sides):
    t.forward(length)
    t.left(angle)
turtle.done()


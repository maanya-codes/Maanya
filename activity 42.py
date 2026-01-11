import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(500, 500)
length = 0
t = turtle.Turtle()
while True:
    for i in range(4):
        t.forward(length+1)
        t.left(90)
        length -= 5
    length += 1
    

t.done()


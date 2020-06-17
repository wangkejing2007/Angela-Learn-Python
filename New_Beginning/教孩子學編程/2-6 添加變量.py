import turtle
t = turtle.Pen()
t.width(2)
t.speed(0)
turtle.bgcolor("black")
colors = ["red","blue","yellow","green","orange","cyan"]
sides = 3
for x in range(400):
    t.color(colors[x % sides])
    t.forward(2 * x)
    t.left(360 / sides + 1)
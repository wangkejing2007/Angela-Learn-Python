import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red","blue","yellow","green","orange","cyan"]
sides = 4
for x in range(300):
    t.color(colors[x % sides])
    t.width(x/20)
    t.forward(3 * x)
    t.left(360 / sides + 2)
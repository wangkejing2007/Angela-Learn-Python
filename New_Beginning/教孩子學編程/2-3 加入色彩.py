import turtle
t = turtle.Pen()
t.width(3)
t.color("#ff00ff")
t.speed(0)
for x in range(100):
    t.forward(4 * x)
    t.left(91)
turtle.done()
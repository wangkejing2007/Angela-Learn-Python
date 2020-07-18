import turtle
t = turtle.Pen()
t.width(1)
t.color("blue")
t.speed(0)
for x in range(100):
    t.circle(x)
    t.left(60)
turtle.done()
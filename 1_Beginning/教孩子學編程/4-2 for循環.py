import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
for i in range(30):
    t.color("red")
    t.circle(100)
    t.color("orange")
    t.circle(30)
    t.left(360/30)
turtle.done()
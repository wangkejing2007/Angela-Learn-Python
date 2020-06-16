import turtle
t = turtle.Pen()
t.width(2)
turtle.bgcolor("black")
colors = ["red","blue","green","orange"]
t.speed(0)
for x in range(100):
    t.color(colors[x % 4])
    t.forward(4 * x)
    t.left(89)
turtle.done()
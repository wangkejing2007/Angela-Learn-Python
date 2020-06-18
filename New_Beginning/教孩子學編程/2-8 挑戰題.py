import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red","blue","yellow","green","orange","cyan"]

sides=eval(input("Enter a number of sides between 2 and 6: "))

for x in range(100):
    t.color(colors[x % sides])
    t.width(x/20)
    t.circle(2 * x)
    t.left(360 / sides + 2)
t.clear()
for x in range(100):
    t.color(colors[x % sides])
    t.width(x/20)
    t.forward(4 * x)
    t.left(360 / sides + 92)

turtle.done()
import turtle
t = turtle.Pen()
t.width(2)
turtle.bgcolor("black") #改變背景顏色
colors = ["red","blue","green","orange"]
t.speed(0)
for x in range(400):
    t.color(colors[x % 4])
    t.forward(2 * x)
    t.left(89)
turtle.done()
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
sides = int(input("請輸入要畫幾邊形 (>=3)？"))
colors = ["red","blue","yellow","green","orange","cyan"]
for x in range(300):
    t.color(colors[x % sides % len(colors)])
    t.forward(x / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
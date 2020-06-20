import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
sides = int(input("請輸入要畫幾個圓形？"))
colors = ["red","blue","yellow","green","orange","cyan"]

for x in range(50):
    t.color(colors[x % sides % len(colors)])
    t.width(x * sides / 100)
    t.circle(x)
    t.left(360 / sides + 1)

adj=input("請輸入形容詞：")
noun=input("請輸入名詞：")
verb=input("請輸入動詞：")
print("很久以前，有個",adj,noun,verb,"這位老師")
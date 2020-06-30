import turtle
t = turtle.Pen()
t.speed(1)
turtle.bgcolor("black")

colors=('red','blue','green','orange')
ur_name=turtle.textinput("please enter ur name","請輸入你的名字")

for x in range(100):
    t.pencolor(colors[x%4])
    t.penup()
    t.forward(x*6)
    t.pendown()
    t.write(ur_name, font=("Arial", int(2+x/3),"bold"))
    t.left(92)

turtle.done()
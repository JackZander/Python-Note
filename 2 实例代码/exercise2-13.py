#exercise2-13.py
#用turtle库绘制9个同心圆
import turtle
turtle.setup(650, 450, 200, 200)
x = 10
y = 10
for i in range(9):
    turtle.up()
    turtle.goto(0,y)
    turtle.down()
    turtle.circle(x)
    x += 10
    y -= 10

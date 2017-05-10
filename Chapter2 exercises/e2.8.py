import turtle
x = 5
y = 90
turtle.speed(10)
for i in range(50):
    turtle.fd(x)
    turtle.seth(y)
    x += 5
    y += 90

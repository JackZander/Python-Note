# 绘制五角星
# I:输入数值
# P:计算数值
# O:输出数值

from turtle import *
fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos()) < 1:
        break
end_fill()

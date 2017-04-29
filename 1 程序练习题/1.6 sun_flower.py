# 绘制太阳花
# I:输入数值
# P:计算数值
# O:输出数值

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

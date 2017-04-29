# 九九乘法表
# I:输入数值
# P:计算数值
# O:输出数值

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(j,i,i*j),end='')
    print('')

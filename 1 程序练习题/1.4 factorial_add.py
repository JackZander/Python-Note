# 计算1+2!+3!+...+10!
# I:输入数值
# P:计算数值
# O:输出数值

sum, tmp = 0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print("运算结果是：{}".format(sum))

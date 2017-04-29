# 整数序列求和
# I:输入一个正整数N
# P:计算1到N相加的结果
# O:输出结果

n = input("请输入整数N：")
sum = 0
for i in range(int(n)):
    sum += i + 1
print("1到N求和结果：",sum)

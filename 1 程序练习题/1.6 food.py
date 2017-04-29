# 健康食谱
# I:输入数值
# P:计算数值
# O:输出数值

diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x == y):
            print("{}{}".format(diet[x],diet[y]))

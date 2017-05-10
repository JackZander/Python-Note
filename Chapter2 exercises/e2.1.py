#e2.1py
'''
TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
'''
T = input("请输入温度值符号：")
if T[-1] in ['C','c']:
    c = eval(input("请输入摄氏温度值："))
    f = 1.8*c + 32
    F = int(f)
    print("华氏温度为F:",F)
elif T[-1] in ['F','f']:
    f = eval(input("请输入华氏温度值："))
    c = (f - 32)/1.8
    C = int(c)
    print("摄氏温度为C:",C)
else:
    print("输入格式错误")
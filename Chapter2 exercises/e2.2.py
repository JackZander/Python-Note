#e2.2
m = input("请输入货币符号，人民币用R，r表示，美元用D，d表示：")
if m[-1] in ['R','r']:
    D = 6*eval(m[0:-1])
    print("转换后的货币是{:.2f}美元".format(D))
elif m[-1] in ['D','d']:
    R = (eval(m[0:-1]))/6
    print("转换后的货币是{:.2f}人民币".format(R))
else:
    print("输入格式错误")

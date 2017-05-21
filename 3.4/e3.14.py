#一年365天，出水平1.0，工作一天水平增加N（0.001~0.010)，不工作水平不下降，工作六天
dayup = 1.0
dayfactor = float(input("请输入小数（0.001~0.01）:") )
if 0.01>=dayfactor>=0.001:
    for i in range(365):
        if i % 7 in [1,2,3,4,5,6]:
            dayup = dayup * (1 + dayfactor)
        else:
            pass
else:
    print("输入错误")
print("向上6天的力量：{:.2f}".format(dayup))
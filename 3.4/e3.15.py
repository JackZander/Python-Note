#一年360天，初始水平1.0，以每个月30天计算，每个月初连续10天，工作一天水平增加N（0.001~0.010)，不工作水平不下降
dayup = 1.0
dayfactor = float(input("请输入小数（0.001~0.01）:") )
if 0.01>=dayfactor>=0.001:
    dayup = 12.0 *((1 + dayfactor)**10)
else:
    print("输入错误")
print("向上10天的力量：{:.2f}".format(dayup))
# 一年365天，以第1天的能力值为基数，记为1.0，好好学习能力值比前一天提高dayfactor，否则下降dayfactor，每天努力和放任，一年后能力相差多少
import math
dayfactor = 0.01
dayup = math.pow((1.0+dayfactor), 365)  # 提高0.001
daydown = math.pow((1.0 - dayfactor), 365)  # 放任0.001
print("向上：{:.2f}，向下：{:.2f}。".format(dayup, daydown))

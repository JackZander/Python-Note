'''
猴子吃桃问题。猴子第一天摘下若干个桃子，当即吃了一半，好不过瘾，又多吃了一个.
第二天早上又吃了剩下的桃子的一半，又多吃了一个。以后每天都吃了前一天剩下的一半
零一个，到第5天早上想再吃的时候，就剩下一个桃子.  求第一天共摘多少个桃子。
'''
# I:输入数值
# P:计算数值
# O:输出数值

n = 1
for i in range(5,0,-1):
    n = (n+1)<<1
print(n)

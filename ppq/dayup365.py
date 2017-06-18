import random


def dayup(base=1.0, n=1.0):
    print('n=' + str(n), end=',')
    ns = n / 1000
    for i in range(364):
        if i % 7 in [0, 1, 2, 3]:
            base *= (1 + ns)
    print('能力值:' + str(base), end=',')
    return base


def daydayup(base=1.0, n=1.0):
    ns = n / 1000
    for i in range(364):
        base *= (1 + ns)
    return base


loop = eval(input("请输入n的个数:"))
for i in range(loop):
    n = random.random() * 10
    result1 = dayup(1.0, n)
    result2 = daydayup(1.0, n)
    print("差别为:" + str(result2 - result1))

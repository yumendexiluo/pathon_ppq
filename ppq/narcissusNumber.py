# 水仙花数
def isNarcissus(num):
    # 分别计算百位十位个位数字
    bw = int(num / 100)
    sw = int((num % 100) / 10)
    gw = num % 10
    # 求和 **3代表求立方
    sum = bw ** 3 + sw ** 3 + gw ** 3
    if sum == num:
        return True
    return False


for i in range(100, 1000):
    if isNarcissus(i):
        print(i, end=',')

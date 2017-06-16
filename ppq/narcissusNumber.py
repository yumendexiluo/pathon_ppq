# 水仙花数
def isNarcissus(num):
    # 分别计算百位十位个位数字
    bw = int(num / 100)
    sw = int((num % 100) / 10)
    gw = num % 10
    # 求和
    sum = (bw * bw * bw) + (sw * sw * sw) + (gw * gw * gw)
    if sum == num:
        return True
    return False


for i in range(100, 1000):
    if isNarcissus(i):
        print(i, end=',')

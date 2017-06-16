# 水仙花数
def isNarcissus(num):
    bw = int(num / 100)
    sw = int((num % 100) / 10)
    gw = num % 10
    sum = (bw * bw * bw) + (sw * sw * sw) + (gw * gw * gw)
    if sum == num:
        return True
    return False


for i in range(100, 1000):
    if isNarcissus(i):
        print(i, end=',')

# 兔子繁衍
def time(oneMonthRabbit, twoMonRabbit, adultRabbit):
    # 第一个月的兔子都长成了第二个月兔
    # 每只成年兔生一只第一个月兔
    # 每只第二个月兔都长成了成年兔并生一只第一个月兔
    return [adultRabbit+twoMonRabbit, oneMonthRabbit, adultRabbit+twoMonRabbit]


s = input("请输第n个月:")
if s.isdigit():
    oneMonthRabbit = 2
    twoMonRabbit = 0
    adultRabbit = 0
    print("第1个月兔子数为2")
    for i in range(2, int(s)+1):
        array = time(oneMonthRabbit, twoMonRabbit, adultRabbit)
        oneMonthRabbit = array[0]
        twoMonRabbit = array[1]
        adultRabbit = array[2]
        sum = oneMonthRabbit + twoMonRabbit + adultRabbit
        print("第" + str(i) + "个月兔子数为" + str(sum))
else:
    print("输入错误")

# 奇偶求和
def sum():
    s = input("请输入正整数:")
    su = 0.0
    if s.isdigit():
        num = int(s)
        if num % 2 == 0:
            for i in range(2, num + 2, 2):
                su += 1.0 / i
            print(su)
        else:
            for i in range(1, num + 2, 2):
                su += 1.0 / i
            print(su)
    else:
        print("输入错误请重新输入")
        sum()


sum()

# 素数判断
def isPrime(n=0):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def listPrime(maxNum=0):
    for i in range(maxNum):
        if isPrime(i):
            print(i, end=',')


s = input("请输入正整数:")
if s.isdigit():
    num = int(s)
    listPrime(num)
else:
    print("输入错误")

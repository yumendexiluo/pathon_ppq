# 输入判断
def checkInput(str=None):
    if str == 'a':
        return 'alpha'
    elif str == 'b':
        return 'bravo'
    elif str == 'c':
        return 'charlie'
    else:
        raise ValueError


s = input("Enter a,b,or c:")
result = ''
try:
    result = checkInput(s)
except ValueError:
    print('输入错误')
else:
    print(result)

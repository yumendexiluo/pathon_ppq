def max_lenth(str='abcdassasdefg'):
    pmax = ""
    for i in range(len(str)):
        b = 1
        for j in range(i, len(str[i:])):
            if str[j] in str[i:j]:
                b = 0
                break
        if len(str[i:j + b]) > len(pmax):
            pmax = str[i:j + b]
    print(pmax)


if __name__ == '__main__':
    s = input("请输入字符串:")
    # max_lenth(str=s)
    for t in range(3, 5):
        print(s[t])

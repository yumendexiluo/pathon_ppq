# 凯撒加密解密
def encode(plaincode=None):
    encodeStr = ''
    for p in plaincode:
        if ord("a") <= ord(p) <= ord("z"):
            print(chr(ord("a") + (ord(p) - ord("a") + 3) % 26), end='')
            encodeStr += chr(ord("a") + (ord(p) - ord("a") + 3) % 26)
        else:
            print(p, end='')
            encodeStr += p
    return encodeStr


def decode(encodeStr=None):
    for p in encodeStr:
        if ord("a") <= ord(p) <= ord("z"):
            print(chr(ord("a") + (ord(p) - ord("a") - 3) % 26), end='')
        else:
            print(p, end='')


if __name__ == '__main__':
    s = input("请输入字符串:")
    encodeStr = encode(s)
    print()
    decode(encodeStr)

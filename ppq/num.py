# 0123四个数字组成不重复三位数
array = list()
for i in range(3, 0, -1):
    for j in range(3, -1, -1):
        if j != i:
            for k in range(3, -1, -1):
                if k != i and k != j:
                    array.append(i * 100 + j * 10 + k)
print(len(array))
for l in array:
    print(l, end=' ')

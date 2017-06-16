for i in range(21):
    for j in range(21):
        if i % 5 == 0 and j % 5 == 0:
            print('+', end='')
        elif i % 5 == 0:
            print('—', end='')
        elif j % 5 == 0:
            print('|', end='')
        else:
            print('  ', end='')
        if j == 20:
            print()

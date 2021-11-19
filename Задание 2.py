import random


def numbers(a,b):
    line = []
    shirina = 0
    while shirina != a:
        for dlina in range(b):
            line.append(str(random.randint(-100, 101)))
            line.append(' ')
        line.append('\n')
        shirina += 1
    file = open('numbers.txt', 'w')
    file.writelines(line)
    file.close()


numbers(int(input("Ширина ")), int(input("Длина ")))
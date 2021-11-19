file = open('numbers.txt', 'r')
line = file.read()
file.close()
i = line.split()
sum = 0
for x in i:
    sum += int(x)
print(sum)


# 12 33 100
# 20 30 40
# -99 80 0
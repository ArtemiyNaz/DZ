file = open('input.txt', 'r', encoding = "utf-8")
file1 = open('output.txt', 'w', encoding = "utf-8")
otv = []
for x in range(15):
    srav = []
    t = file.readline()
    words = " ".join(t)
    for i in words:
            if i.isalpha():
                srav.append(i.lower())
                ''.join(srav)
    if srav == srav[::-1]:
        otv.append(words)
file.close()


for b in range(len(otv)):
    file1.write(otv[b])
    file1.write('\n')
file1.close

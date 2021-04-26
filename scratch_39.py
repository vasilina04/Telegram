c = [68, 56, 56, 60]
data = open('Тогу направления.txt', 'rt', encoding='utf8').read().strip('')
n = [[a for a in d.split(';')]for d in data.split('\n')]
chans = []
s1 = c[0] + c[1]
s2 = c[0] + c[1] + c[2]
if c[2] > c[3]:
    s1 += c[2]
else:
    s1 += c[3]
if c[0] < 40 or c[1] < 39 or c[2] < 44 or c[3] < 33:
    a = 'Недостаточно баллов для подачи документов'
    if c[0] < 40:
        b = 'Не хватает баллов по русскому языку'
    if c[1] < 39:
        b = 'Не хватает баллов по математике'
    if c[2] < 44:
        b = 'Не хватает баллов по информатике'
    if c[3] < 39:
        b = 'Не хватает баллов по физике'
    chans.append(a)
    chans.append(b)
else:
    for i in range(len(n)):
        if i == 1 or i == 2 or i == 3:
            if (s2 >= int(n[i][1])) and (s2 <= int(n[i][2])):
                a = n[i][0] + ' - шанс поступить есть, но ниже среднего'
                chans.append(a)
            elif (s2 >= int(n[i][2])) and (s2 <= int(n[i][3])):
                a = n[i][0] + ' - шанс поступить средний'
                chans.append(a)
            elif s2 >= int(n[i][3]):
                a = n[i][0] + ' - шанс поступить высокий'
                chans.append(a)
        else:
            if (s1 >= int(n[i][1])) and (s1 <= int(n[i][2])):
                a = n[i][0] + ' - шанс поступить есть, но ниже среднего'
                chans.append(a)
            elif (s1 >= int(n[i][2])) and (s1 <= int(n[i][3])):
                a = n[i][0] + ' - шанс поступить средний'
                chans.append(a)
            elif s1 >= int(n[i][3]):
                a = n[i][0] + ' - шанс поступить высокий'
                chans.append(a)

MyFile = open('ТОГУ шанс.txt', 'w')
for u in chans:
     MyFile.write(u)
     MyFile.write('\n')
MyFile.close()
print(chans)
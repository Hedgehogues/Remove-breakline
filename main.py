fd = open('data')

answ = ''
for line in fd.readlines():
    answ += line[:-1] + ' '

fd.close()

fd = open('data', 'w')
fd.write(answ)

# coding:utf-8
a = range(1,10000)
for i in a:
    c = 0
    for j in range(1,i+1):
        if j<i:
            if i%j == 0:
                c = c+j
            else :
                continue
        else:
            break
    if c == i :
        print("%s为完全数" %i)
    elif c !=i:
        continue


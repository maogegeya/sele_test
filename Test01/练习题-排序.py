# coding:utf-8
List1 = [3, 2, 1, 9, 10, 78, 6]
i = 0
for i in range(7):
    if i<7:
        for k in range(i,7):
            if List1[i]>List1[k]:
                j = List1[i]
                List1[i] = List1[k]
                List1[k] = j
            else:
                continue
    else:
        break
print(List1)

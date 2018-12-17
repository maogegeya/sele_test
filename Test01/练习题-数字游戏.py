# coding:utf-8
import random
print("------猜数字------")
k = 1
i = 99
c = random.randint(1,99)
print(c)
active = True
while active:
    a = int(input("请输入一个整数%s到%s:" %(k,i)))
    if a>=k and a<c:
        k = a
    else:
        if a>c and a<=i:
            i = a
        else:
            if a ==c:
                print("真聪明，猜对了！")
                break
            else:
                k>a or i<a
                print("您输入的整数范围不符合要求！请重新输入")


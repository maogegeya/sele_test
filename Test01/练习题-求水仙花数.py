a = range(100,1000)
result = []
for i in a:
    b = int(i/100)
    s = int((i%100)/10)
    g = i%10
    if i == b**3+s**3+g**3:
        result.append(i)
    else:
        continue
print(result)

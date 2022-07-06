d = [2]
b = 0
for a in range(3, 120000, 2):
    for i in d:
        if a % i == 0:
            break
    else:
        d.append(a)
print(d[10000])

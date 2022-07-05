x = []
for i in range(100, 1000):
    for n in range(100, 1000):
        b = str(n*i)
        if len(b) == 6 and b[0] == b[5] and b[1] == b[4] and b[2] == b[3]:
            x.append(b)
            x.sort()
print(x[-1])

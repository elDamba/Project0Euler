a = 13195
for i in range(a-1, 1, -1):
    b = False
    if a % i == 0:
        for k in range(i - 1, 1, -1):
            if i % k == 0:
                b = True
        if b == True:
            print(i, end=" ")

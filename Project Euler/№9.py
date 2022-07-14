(a, b, c) = (0, 0, 0)
for a in range(100, 332):
    for b in range(a + 1, 500):
        for c in range(a + 2, 500):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                print(a * b * c)

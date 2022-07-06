(a, b, c, d) = (0, 0, 0, 0)
for i in range(1, 101):
    a = i**2
    b += a
    c += i
    d = c**2
print(d-b)

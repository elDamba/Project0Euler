a = [1, 2]
while a[-2] < 4000000:
    a.append(a[-2] + a[-1])
b = [i for i in a if i < 4000000 if i % 2 == 0]
print(sum(b))

n = 2000000
a = [i for i in range(n + 1)]
a[1] = 0
i = 2
while i <= n / 2:
    if a[i] != 0:
        b = i ** 2
        while b <= n:
            a[b] = 0
            b += i
    i += 1
b = [i for i in a if i != 0]
print(sum(b))

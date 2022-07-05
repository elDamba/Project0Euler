for i in range(1, 10000000000):
    if i % 20 == 0 and i % 19 == 0 \
            and i % 17 == 0 and i % 16 == 0 \
            and i % 13 == 0 and i % 12 == 0 \
            and i % 9 == 0 and i % 11 == 0 \
            and i % 5 == 0 and i % 7 == 0:
        print(i)
        break

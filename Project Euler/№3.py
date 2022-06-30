a = 600851475143
b = 2
while 1:
    if a % b == 0:
        a /= b
        if a == 1:
            print(b)
            break
    b += 1
    

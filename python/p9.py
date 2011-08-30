
a = 1
b = 2
while True:
    while 1000 - a - b > b:
        c = (1000 - a - b)
        if a ** 2 + b ** 2 == c **2:
            print a * b * c
            exit(0)
        b += 1
    a += 1
    b = a + 1

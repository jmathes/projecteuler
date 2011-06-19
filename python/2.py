f1 = 1
f2 = 2
answer = 0

while f2 <= 4000000:
    if f2 % 2 == 0:
        answer += f2
    f2 = f2 + f1
    f1 = f2 - f1

print answer
big_number = 2 ** 1000 #lol yeah python!
sum = 0
while big_number > 0:
    sum += big_number % 10
    big_number /= 10
print sum
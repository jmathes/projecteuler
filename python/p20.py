product = 1

for i in xrange(1, 101):
    product *= i
    
sum = 0
while product > 0:
    sum += product % 10
    product /= 10
    
print sum
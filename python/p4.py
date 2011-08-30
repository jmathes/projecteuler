num = 999

def palindromize(num):
    return (num * 1000) + (num % 10 * 100) + (num / 10 % 10 * 10) + (num / 100)

while num > 99:
    answer = palindromize(num) 
    divisor = 999
    while divisor > 99:
        if answer % divisor == 0 and answer / divisor < 999:
            print answer
            exit(0)
        divisor -= 1
    num -= 1

print "There is no answer (!?)"

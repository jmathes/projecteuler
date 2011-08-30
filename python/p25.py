"""
"""
from cache import lru_cache

@lru_cache()
def fib(n):
    if n < 2:
        return 1
    low = 1
    high = 1
    i = 3
    while i <= n+1:
        high = low + high
        low = high - low
        i += 1
    return high

high_end = 10000
low_end = 1

def digit_count(n):
    i = 0
    while n > 0:
        i += 1
        n /= 10
    return i



goal = 1000
done = False
iterations = 0
while not done:
    current_guess = (high_end - low_end) / 2 + low_end
    print "current_guess", current_guess
    dc = digit_count(fib(current_guess))
    print "dc", dc
    dc1 = digit_count(fib(current_guess-1))
    print "dc1", dc1
    if dc == goal:
        if dc1 < goal:
            done = True
        else:
            
            high_end = current_guess
    elif dc1 > goal:
        high_end = current_guess
    else:
        low_end = current_guess
    iterations += 1
    if iterations > 100:
        print "Giving up"
        done = True
        
print fib(current_guess)
print fib(current_guess-1)
print current_guess + 1
    
    
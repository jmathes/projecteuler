"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import primes
import math
from cache import lru_cache

myprimes = primes.expand_primes_list(limit=78500)
truncatables = []

def is_truncatable(test):
    return test > 10 and is_left_truncatable(test) and is_right_truncatable(test)

@lru_cache()
def is_left_truncatable(test):
    if test in [2, 3, 5, 7]:
        return True
    return primes.is_prime(test) and is_left_truncatable(test / 10)

@lru_cache()
def is_right_truncatable(test):
    if test in [2, 3, 5, 7]:
        return True
    return primes.is_prime(test) and is_right_truncatable(test % (10 ** int(math.floor(math.log(test, 10)))))


test = 11
last_biggest = 0
while len(truncatables) < 11:
    r = range(1, int(math.floor(math.log(test, 10))) + 1)
    r.reverse()
#    if(len(r)) > last_biggest:
#        print "new milestone: ", test
#        last_biggest = len(r)
    for j in r:
        if not is_left_truncatable(test / (10 **j)):
#            print "For %s, %s isn't left truncatable, so skipping to %s (+1 if that makes it odd)" % (test, test / (10 **j), (test / (10 ** j) + 1) * (10**j))
            test = (test / (10 ** j) + 1) * (10**j)
            if test % 2 == 0:
                test += 1
            break
    if is_truncatable(test):
#        print test
        truncatables.append(test)
    test += 2
        

sum = 0
for t in truncatables:
    sum += t
print sum


"""
Whoops! It would have been faster to add 2, 3, 5, and 7 to the left end of a known left-truncatable 
number over and over until there were no more possible left-truncatable numbers, then tested them all
for right-truncatableness.
Oh well! At least I now have a file with all the primes < 10,000,000
"""
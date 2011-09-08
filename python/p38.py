"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n  1?
"""

import primes
import math
import digits
from cache import lru_cache

best = 918273645
best_n = 9

def test_guess(guess, best):
#    print "Trying ", guess
    multiplier = 0
    list = []
    while True:
        multiplier += 1
        list += digits.get_all(guess * multiplier)
#        print "  list after multiplying by %s" % multiplier, list
        if 0 in list:
#            print "    No zeroes allowed!"
            break
        if digits.collapse(list) < best / (10 ** (9 - len(list))):
#            print "    %s < %s, giving up on %s" % (digits.collapse(list), best / (10 ** (9 - len(list))), guess)
            break
        if len(set(list)) < len(list):
#            print "    list contains duplications, giving up"
            break
        if len(list) == 9:
#            print "***** found a contender! %s results in %s" % (guess, digits.collapse(list))
            return digits.collapse(list)
    return -1


for guess in xrange(9182, 9877):
    temp_best = test_guess(guess, best)
    if temp_best > best:
        best = temp_best

print best
"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

import digits
from math import log

i = 1
while True:
    if int(log(6*i, 10)) == int(log(i, 10)):
        c = set(digits.get_all(i))
        nope = False
        for n in xrange(2, 7):
            if c != set(digits.get_all(i*n)):
                nope = True
                break
        if not nope:
            print i
            exit(0)
    i += 1

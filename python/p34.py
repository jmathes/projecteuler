"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""

import digits
from math import factorial
from pprint import pprint, pformat

ans = 0
for i in xrange(1, 2000000):
    if sum([factorial(n) for n in digits.get_all(i)]) == i:
        ans += i
        print i
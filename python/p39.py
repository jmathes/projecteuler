"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

import math
from pprint import pprint

solutions = {}

for a in xrange(2, 501):
    b = -1
    while True:
        b += 1
        c = math.sqrt(a*a + b*b)
        if a + b + c > 1000:
            break
        if int(c) == c:
            c = int(c)
            if a+b+c not in solutions.keys():
                solutions[a+b+c] = 0
            solutions[a+b+c] += 1

m = max(solutions.values())
[pprint(key) for key, value in solutions.iteritems() if value == m]

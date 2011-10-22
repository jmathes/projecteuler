"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import primes
import digits
from itertools import permutations
from pprint import pprint, pformat

def is_arithmatic_sequence(s):
    if len(s) == 1:
        return True
    s.sort()
    d = s[1] - s[0]
    for i in xrange(len(s)-1):
        if s[i+1] - s[i] != d:
            return False
    return True

four_digit_primes = primes.primes[168:1229] # calcualted offline to save iteration time
excluded_primes = [d for d in digits.get_permutations(1487) if d in four_digit_primes]

for prime in four_digit_primes:
    if prime in excluded_primes:
        continue
    perms = [p for p in digits.get_permutations(prime) if p in four_digit_primes]
    if len(perms) < 3:
        continue
    triples = [list(t) for t in permutations(perms, 3)]
#    pprint(triples)
    for triple in triples:
        if is_arithmatic_sequence(triple):
            print "%s"*3 % tuple(triple)
            exit(0)

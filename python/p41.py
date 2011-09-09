"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import primes
import digits
from itertools import permutations

for i in xrange(9, 0, -1):
    for p in permutations(xrange(i, 0, -1)):
        potential = digits.collapse(p)
        if primes.is_prime_greedy(potential):
            print potential
            exit(0)


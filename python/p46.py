"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import primes
from pprint import pprint, pformat
non_answers = [9, 15, 21, 25, 27, 33]

def insert(nonanswer):
    global non_answers
    if nonanswer == nonanswer/2*2:
        return
    if primes.is_prime(nonanswer):
        return
    non_answers.append(nonanswer)

def is_unreachable_odd_composite(n):
    global non_answers
    if n == n/2*2:
        raise Exception("%s is even, asshole" % n)
    if n in non_answers:
        return False
    if primes.is_prime(n):
        return False
    p = 0
    while primes.primes[p] < n:
        i = 1
        while primes.primes[p] + 2*i**2 <= n:
            nonanswer = primes.primes[p] + 2*i**2
            i += 1
            if nonanswer in non_answers:
                continue
            insert(nonanswer)
            if nonanswer == n:
                return is_unreachable_odd_composite(n)
        p += 1
    
    return True

guess = 3
while not is_unreachable_odd_composite(guess):
    guess += 2
print guess
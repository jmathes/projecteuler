"""
By replacing the 1st digit of *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes
among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003,
being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part
of an eight prime value family.
"""

import primes
import digits

i=0
for prime in primes.primes:
    if prime > 143710:
        print prime
        print i
        exit(0)
    i += 1

def get_guess_iterator():
    guess = [1, 4, 3, 7, 1, 9] #everything before this has been tried in earlier iterations
    while True:
        if sum([1 for g in guess if g == 10]) > 0:
            print guess
            yield guess
        i = len(guess)-1
        guess[i] += 1
        while guess[i] > 10:
            guess[i] = 0
            i -= 1
            if i < 0:
                guess = [0] + guess
                i = 0
            guess[i] += 1
        while guess[-1] not in [1,3,7,9,10]:
            guess[-1] += 1
            
gi = get_guess_iterator()

def get_family(guess):
    candidates = [digits.collapse([(d if d < 10 else nd) for d in guess]) for nd in xrange(10)]
    return [candidate for candidate in candidates if primes.is_prime(candidate)]

family = get_family(gi.next())
while len(family) != 8:
    for guess in family:
        print " ", guess
    family = get_family(gi.next())

print family[0]

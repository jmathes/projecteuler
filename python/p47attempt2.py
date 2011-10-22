"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?
"""

import primes
distfacts = 4

def four_factor_iterator():
    i = 2
    while True:
        factors = primes.dictfactor(i)
        if len(factors) == 4:
            yield i
        i += 1


ffi = four_factor_iterator()
last_f = -100
length = 1
for f in ffi:
    if f == last_f+1:
        length += 1
        print "%s,"%last_f,
    elif length > 1:
        print last_f
        if length == 4:
            exit(0)
        length = 1
#        print "nodeadd: %s baseadd: %s sort: %s other: %s total: %s" % (int(tnn), int(tnb), int(ts), int(to), int(tnn + tnb + ts + to))
    last_f = f
    

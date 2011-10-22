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
import time
from copy import deepcopy
from pprint import pprint, pformat
distfacts = 4

def evaluate(l):
    return reduce((lambda a, b: a*b[1]), l, 1)

def increase(i):
    i[1] *= primes.primes[i[0]]
    return i[1] == primes.primes[i[0]] ** 2

tnn = 0
to = 0
tnb = 0
ts = 0
def four_factor_iterator():
    global tnn
    global tnb
    global ts
    global to
    option = [[i, primes.primes[i]] for i in xrange(distfacts)]
    next_options = [(evaluate(option), option)]
    while True:
        to -= time.time()
        opt = next_options[0][1]
        to += time.time()
        yield next_options[0][0]
        to -= time.time()
        next_options = next_options[1:]
        is_base = True
        to += time.time()
        tnn -= time.time()
        for i in xrange(distfacts):
            option = deepcopy(opt)
            is_base &= increase(option[i])
            option = (evaluate(option), option)
            if option not in next_options:
                next_options.append(option)
        tnn += time.time()
        tnb -= time.time()
        if is_base:
            for i in xrange(distfacts):
                if i == distfacts-1 or opt[i][0]+1 < opt[i+1][0]:
                    option = deepcopy(opt)
                    option[i][0] += 1
                    option[i][1] = primes.primes[option[i][0]]
                    option = (evaluate(option), option)
                    if option not in next_options:
                        next_options.append(option)
        tnb += time.time()
        ts -= time.time()
        next_options.sort()
        ts += time.time()


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
    

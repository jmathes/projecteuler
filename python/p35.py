"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

import digits
import primes
from itertools import permutations


pbm = filter(lambda p : 0 not in digits.get_all(p), primes.get_primes(1000000))
pbm = filter(lambda p : 2 not in digits.get_all(p), pbm)
pbm = filter(lambda p : 4 not in digits.get_all(p), pbm)
pbm = filter(lambda p : 5 not in digits.get_all(p), pbm)
pbm = filter(lambda p : 6 not in digits.get_all(p), pbm)
pbm = filter(lambda p : 8 not in digits.get_all(p), pbm)

cpms = set([2, 5])
ncpms = set([])

def rotations(l):
    l2 = l * 1
    for i in xrange(len(l2)):
        l2 = l2[1:] + [l2[0]]
        yield l2

for prime in pbm:
    if prime not in cpms and prime not in ncpms:
        perms = []
        circular = True
        for ppml in rotations(digits.get_all(prime)):
            ppm = digits.collapse(ppml)
            if not ppm in pbm:
                circular = False
                break
            perms.append(ppm)
        if circular:
#            print perms
            cpms |= set(perms)
        else:
            ncpms |= set(perms)
        
#print cpms
print len(cpms)
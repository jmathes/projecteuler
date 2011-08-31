"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

import digits
from pprint import pprint, pformat

def check(n, d):
    nl = digits.get_all(n)
    dl = digits.get_all(d)
    for i in xrange(2):
        for j in xrange(2):
            if nl[1-i] == dl[1-j] and 1.0 * n / nl[i] == 1.0 * d / dl[j]:
                print "%s/%s -> %s/%s" % (n, d, nl[i], dl[j])
                return True

result = [1, 1]

for d in xrange(11, 100):
    if d % 10 == 0:
        continue
    for n in xrange(11, d):
        if n % 10 == 0:
            continue
        if check(n, d):
            result[0] *= n
            result[1] *= d

#print result

i = 2
while i < result[1]:
    if result[0] % i == 0 and result[1] % i == 0:
        result[0] /= i
        result[1] /= i
#        print "dividing by %s: %s" % (i, result)
    else:
        i += 1
print result[1]
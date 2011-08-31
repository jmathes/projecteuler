"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

"""

import primes
import digits
from itertools import permutations, chain, combinations
import functools
import operator
from pprint import pprint, pformat

def divisions(iterable):
    "divisions([1,2,3]) --> ((), (1,2,3)) ((1,), (2,3)) ((2,), (1,3)) ((3,), (1,2))   "
    s = set(zip(iterable, xrange(len(iterable))))
    total = 2 ** (len(s) - 1)
    source = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    result = []
    for i in xrange(total):
        ns = set(source.next())
        result.append((ns, s - ns))
    return [[[tagged_factor[0] for tagged_factor in tagged_factor_list]
             for tagged_factor_list in tagged_factor_list_pair]
             for tagged_factor_list_pair in result]

def lister(length):
    l = range(1, length+1)
    yield l * 1
    while True:
        i = length-1
        l[i] += 1
        while l[i] > 10 - length + i:
            i -= 1
            if i < 0:
                raise StopIteration
            l[i] += 1
        for i in xrange(1, length):
            if l[i] > 10 - length + i:
                l[i] = l[i-1] + 1
        yield l * 1

answers = set([])

unique_ascending_lists = lister(4)
for unique_ascending_list in unique_ascending_lists:
    unique_lists = permutations(unique_ascending_list)
    for unique_list in unique_lists:
        number = digits.collapse(unique_list)
        ps = set(unique_list)
#        print "number: %s" % number
        factors = primes.factor(number)
#        print "factors: %s" % factors
        factorpairs = divisions(factors)
#        print unique_list
        for pair in factorpairs:
#            print "  %s" % (pair,)
            multiplicand = functools.reduce(operator.mul, pair[0], 1)
            m1s = set(digits.get_all(multiplicand))
            multiplier = functools.reduce(operator.mul, pair[1], 1)
            m2s = set(digits.get_all(multiplier))
            if len(m1s) + len(m2s) == 5 and m1s | m2s | ps == set([1,2,3,4,5,6,7,8,9]):
                answers.add((multiplicand, multiplier, number))

pprint(answers)
print sum(set(eq[2] for eq in answers))


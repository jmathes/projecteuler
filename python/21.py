import primes
from cache import lru_cache
amicabilabuddies = {}


@lru_cache()
def get_amicabilibuddy(n):
    factors = primes.all_factors(n)
    sum = 0
    for factor in factors[:-1]:
        sum += factor
    return sum

amicables = []

for i in xrange(1, 10000):
    buddy = get_amicabilibuddy(i)
    if get_amicabilibuddy(buddy) == i and buddy != i:
        print "pair: %s, %s" % (i, buddy)
        amicables.append(i)


sum = 0
for i in amicables:
    sum += i

print sum 
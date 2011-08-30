import primes
allfactors = {}
for i in xrange(1, 21):
    factors = primes.dictfactor(i)
    for factor, count in factors.items():
        if factor not in allfactors.keys():
            allfactors[factor] = 0
        allfactors[factor] = max(allfactors[factor], count)
answer = 1
for factor, count in allfactors.items():
    answer *= factor ** count
print answer
            
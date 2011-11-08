fileprimesfile = open('primes.txt', 'rw')
fileprimes = fileprimesfile.readlines()
primes = [int(prime) for prime in fileprimes]

def factor(n):
    pi = primes_iterator()
    d = pi.next()
    factors = []
    while d <= n:
        if n % d == 0:
            n /= d
            factors.append(d)
        else:
            d = pi.next()
    return factors

def dictfactor(n):
    pi = primes_iterator()
    d = pi.next()
    factors = {}
    while d <= n:
        if n % d == 0:
            if d not in factors.keys():
                factors[d] = 0
            factors[d] += 1
            n /= d
        else:
            d = pi.next()
    return factors

def all_factors(n):
    dictfactors = dictfactor(n)
    factors_so_far = [1]
    for factor, count in dictfactors.items():
        new_factors_list = []
        for i in xrange(count + 1):
            more_factors = factors_so_far * 1
            for factorloc in xrange(len(more_factors)):
                more_factors[factorloc] *= (factor ** i)
            new_factors_list += more_factors
        factors_so_far = new_factors_list
    factors_so_far.sort()
    return factors_so_far

def expand_primes_list(limit=1000, limit_type = 'length'):
    global primes
    fileprimesfile = open('primes.txt', 'rw')
    fileprimes = fileprimesfile.readlines()
    fileprimes = [int(prime) for prime in fileprimes]
    if len(fileprimes) > len(primes):
        primes = fileprimes
    
    if primes == []:
        primes = [2]
    test = max(3, primes[len(primes) - 1])
    
    def past_limit(primes, limit, limit_type):
        if limit_type == 'length':
            return len(primes) > limit
        if limit_type == 'max':
            return primes[len(primes) - 1] > limit
        return True
    
    while not past_limit(primes, limit, limit_type):
        is_prime = True
        for prime in primes:
            if test % prime == 0:
                is_prime = False
                break
        if is_prime:
            print "added %s", test
            primes.append(test)
        test += 2
    pfile = open("primes.txt", "w")
    pfile.writelines([str(prime) + '\n' for prime in primes])
    return primes

def sieve(max):
    sieve_primes = range(2, max)
    i = 0
    nonprime_indices = set()
    while i*i <= max:
        prime = sieve_primes[i]
        m = 1
        while i + (prime * m) < len(sieve_primes):
            nonprime_indices.add(i + prime * m)
            m += 1
        i += 1
    newprimes = []
    last_prime_index = 0
    for index in nonprime_indices:
        newprimes += sieve_primes[last_prime_index:index]
        last_prime_index = index + 1
    newprimes += sieve_primes[last_prime_index:]
    sieve_primes = newprimes
    global primes
    if len(sieve_primes) > len(primes):
        primes = sieve_primes
        pfile = open("primes.txt", "w")
        pfile.writelines([str(prime) + '\n' for prime in primes])
    return primes

def othersieve(max):
    primes = sundaram3(max)
    print len(primes)
    print primes[-1]
    pfile = open("primes.txt", "w")
    pfile.writelines([str(prime) + '\n' for prime in primes])

def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)


def is_prime(test):
    max_prime = primes[len(primes) - 1]
    if test > max_prime:
        print "Crap, I don't have primes as high as %s. Expanding the list. This takes a while" % test
        expand_primes_list(limit_type="max", limit=test)
    return test in primes

def is_prime_greedy(test):
    max_prime = primes[len(primes) - 1]
    if test > max_prime:
        for prime in primes:
            if test / (1.0 * prime) == int(test / (1.0 * prime)):
                return False
            if prime * prime > test:
                return True
        raise Exception("I dunno. Expand the primes list.")
    return test in primes

def primes_iterator():
    for prime in primes:
        yield prime
    raise Exception ("Primes iterator doesn't support finding new primes")

def get_primes(less_than, greater_than=1):
    max_prime = primes[len(primes) - 1]
    if less_than > max_prime:
        print "Crap, I don't have primes as high as %s. Expanding the list. This takes a while" % less_than
        expand_primes_list(limit_type="max", limit=test)
    return [prime for prime in primes if (prime < less_than and prime > greater_than)]
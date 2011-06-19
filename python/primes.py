
def factor(n):
    d = 2
    factors = []
    while d <= n:
        if n % d == 0:
            n /= d
            factors.append(d)
        else:
            d += 1
    return factors

def dictfactor(n):
    d = 2
    factors = {}
    while d <= n:
        if n % d == 0:
            if d not in factors.keys():
                factors[d] = 0
            factors[d] += 1
            n /= d
        else:
            d += 1
    return factors

def expand_primes_list(primes, limit, limit_type = 'length'):
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
            primes.append(test)
        test += 2
    return primes

def sieve(max):
    primes = range(2, max)
    i = 0
    nonprime_indices = set()
    while i*i <= max:
        prime = primes[i]
        m = 1
        while i + (prime * m) < len(primes):
            nonprime_indices.add(i + prime * m)
            m += 1
        i += 1
    newprimes = []
    last_prime_index = 0
    for index in nonprime_indices:
        newprimes += primes[last_prime_index:index]
        last_prime_index = index + 1
    newprimes += primes[last_prime_index:]
    primes = newprimes
    return primes

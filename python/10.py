import primes
primelist = primes.sieve(2000000)
answer = 0
for prime in primelist:
    answer += prime
print answer
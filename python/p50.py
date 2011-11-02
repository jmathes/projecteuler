"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import primes

longest_sequence = 1
answer = 2

i = 0
for i in xrange(len(primes.primes)):
    ci = i
    sum = 0
    while sum < 1000000:
        sum += primes.primes[ci]
        if ci-i > longest_sequence and primes.is_prime(sum):
            longest_sequence = ci-1+1
            answer = sum
        ci += 1
    
    i += 1
print answer
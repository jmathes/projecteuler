"""
find a*b

such that n^2 + an + b yields the most primes in a row for integer n>=0
and |a| < 1000, |b| < 1000

"""
import primes


def primelength(a, b):
    i = 0
    while primes.is_prime(i*(i + a) + b):
        i += 1
    return i

#print primelength(1, 41) # should be 40
#print primelength(-79, 1601) # should be 80

best_pair = (-29, 251)
longest_length = 55

possible_b = primes.get_primes(1000, greater_than=best_pair[1] - 1)
print possible_b

for b in possible_b:
    print "Trying ", b
    for a in xrange(-1 * b + 2, 1000, 2):
        length = primelength(a, b)
        if length > longest_length:
            longest_length = length
            best_pair = (a, b)
            print "longest_length: ", longest_length
            print "best_pair: ", best_pair

print "longest_length: ", longest_length
print "best_pair: ", best_pair
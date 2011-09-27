"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import digits
import primes


def divides(d, n):
    return n*1./d == n/d

def unique_digits(n):
    dgs = digits.get_all(n)
    return len(set(dgs)) == len(dgs)

first_six_primes = primes.primes[:6]
first_six_primes.reverse()

multiples_of_17 = [n for n in xrange(99, 1000) if divides(17, n) and unique_digits(n)]

alldigits = set(xrange(10))


def sum_interestings(number_so_far, primes):
    numbers_unused = alldigits - set(number_so_far)
    if len(numbers_unused) == 1:
        if 0 in numbers_unused:
            return 0
        return digits.collapse(list(numbers_unused) + number_so_far)
    test = number_so_far * 1
    sum = 0
    for number in numbers_unused:
        test = [number] + number_so_far
        if divides(primes[0], digits.collapse(test[:3])):
            sum += sum_interestings(test, primes[1:])
    return sum

sum = 0
for multiple in multiples_of_17:
    number_so_far = digits.get_all(multiple)
    sum += sum_interestings(number_so_far, first_six_primes)
    
print sum
        

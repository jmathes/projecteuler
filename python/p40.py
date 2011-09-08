"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1  d10  d100  d1000  d10000  d100000  d1000000
"""

import digits

def get_digits_in_power(power):
    return 9 * power * 10**(power-1)

def digit_at(place):
    index_into_power = place
    power = 1
    while index_into_power > get_digits_in_power(power):
        index_into_power -= get_digits_in_power(power)
        power += 1
    index_into_power -= 1
    number_in_power = index_into_power / power
    digit_in_number = index_into_power % power
    number = (10 ** (power-1)) + number_in_power
    digit = digits.get_all(number)[digit_in_number]
    return digit
    
answer = 1
for power in xrange(7):
    answer *= digit_at(10 ** power)
    
print answer
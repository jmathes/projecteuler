"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

import digits
ans = 0

for i in xrange(1, 1000000):
    dl = digits.get_all(i)
    dlr = (dl * 1)
    dlr.reverse()
    bl = digits.get_all(i, 2)
    blr = (bl * 1)
    blr.reverse()
    if dl == dlr and bl == blr:
        print i
        ans += i

print ans
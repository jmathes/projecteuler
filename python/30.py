"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

from pprint import pprint, pformat
import digits
import time

def sum_of_powers(ds, p):
    return sum(d ** p for d in ds)

checked = []

dgs = [0, 0, 0, 0, 0, 0, 1] #first thing we do is add 1, but we shouold skip 1 per prob definition, so start at 2
l = len(dgs)
done = False

ans = 0

while not done:
    i = l-1
    dgs[i] += 1
    while dgs[i] > 9:
        dgs[i] = 0
        i -= 1
        if i < 0:
            done = True
            break
        dgs[i] += 1
    for i in xrange(1, l):
        if(dgs[i] < dgs[i-1]):
            dgs[i] = dgs[i-1]
    spd = digits.get_all(sum_of_powers(dgs, 5))
    n = digits.collapse(spd)
    spd.sort()
    if digits.collapse(dgs) == digits.collapse(spd):
        ans += n
        print n

print ans

assert sum_of_powers(digits.get_all(1634), 4) == 1634
assert sum_of_powers(digits.get_all(8208), 4) == 8208
assert sum_of_powers(digits.get_all(9474), 4) == 9474




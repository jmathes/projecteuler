"""
Pentagonal numbers are generated by the formula, Pn=n(3n1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70  22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference is pentagonal and D = |Pk  Pj| is minimised; what is the value of D?
"""

from cache import lru_cache

def gpi():
    i = 1
    while True:
        yield (i*(3*i-1))/2
        i += 1

npgpi = gpi()
pentlist = [npgpi.next()]
def next_pent(pent):
    assert is_pent(pent)
    pentlist.append(npgpi.next())
    return pentlist[pentlist.index(pent)+1]

def is_pent(candidate):
    while candidate not in pentlist:
        if pentlist[len(pentlist)-1] > candidate:
            return False
        pentlist.append(npgpi.next())
    return True

assert is_pent(1)
assert is_pent(5)
assert is_pent(12)
assert is_pent(22)
assert is_pent(35)
assert not is_pent(33)
assert not is_pent(7)

scout = gpi()
candidate = scout.next()
smaller = 0
larger = 1
print "candidate: ", candidate
while True:
    while pentlist[larger] + pentlist[smaller] < candidate:
        larger += 1
        while larger >= len(pentlist):
            pentlist.append(npgpi.next())
    if pentlist[larger] + pentlist[smaller] == candidate:
        print "pents %s and %s sum to %s" % (pentlist[smaller], pentlist[larger], candidate)
        if is_pent(pentlist[larger] - pentlist[smaller]):
            print " ... and diff to %s! success" % (pentlist[larger] - pentlist[smaller])
            exit(0)
        else:
            smaller += 1
            larger = smaller + 1
            while larger >= len(pentlist):
                pentlist.append(npgpi.next())
    elif larger - smaller == 1:
        print "candidate: ", candidate
        candidate = scout.next()
        smaller = 0
        larger = 1
    else:
        smaller += 1
        larger = smaller + 1
        while larger >= len(pentlist):
            pentlist.append(npgpi.next())

"""
Maybe not the best answer:

pents 1560090 and 7042750 sum to 8602840
 ... and diff to 5482660! success
"""
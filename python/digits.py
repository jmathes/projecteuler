from itertools import permutations

def get_all(n, base=10):
    result = []
    while n > 0:
        result.append(n % base)
        n /= base
    result.reverse()
    return result

assert [1,2,3,4,5] == get_all(12345)

def collapse(l):
    if len(l) == 0:
        return []
    return int("".join([str(d) for d in l]))

assert 12345 == collapse([1,2,3,4,5])

def get_permutations(n):
    if n == 0:
        return [0]
    digits = get_all(n, 10)
    perms = permutations(digits)
    return set([collapse(perm) for perm in perms if perm[0] > 0])

assert set([123, 132, 213, 231, 312, 321]) == get_permutations(123)
assert set([102, 120, 201, 210]) == get_permutations(102)
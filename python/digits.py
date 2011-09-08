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
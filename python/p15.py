from cache import lru_cache

@lru_cache()
def find_path_count(x, y):
    if x == 0 or y == 0:
        return 1
    sum = 0
    for i in xrange(0, y+1):
        sum += find_path_count(max(x-1, i), min(x-1, i))
    return sum

print find_path_count(20, 20)
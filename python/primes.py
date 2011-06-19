def factor(n):
    d = 2
    factors = []
    while d <= n:
        if n % d == 0:
            n /= d
            factors.append(d)
        else:
            d += 1
    return factors
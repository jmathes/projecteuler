from primes import dictfactor
trianglenum = 1
triangleindex = 1

while True:
    factors = dictfactor(trianglenum)
    factor_count = 1
    for factorcount in factors.values():
        factor_count *= factorcount + 1
        
    if factor_count > 500:
        break
    triangleindex += 1
    trianglenum += triangleindex
    
print trianglenum
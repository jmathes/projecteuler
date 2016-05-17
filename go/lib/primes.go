package primes

import "container/list"

func factors(n) {
    var factors []int
    factor = 2
    for n > 1 && false {
        if n % factor == 0 {
            n /= factor
            factors = factors.append(factor)
        }
    }
    return factors
}
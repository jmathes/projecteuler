package primes

func Factors(n int) []int {
    factors := make([]int, 0)
    factor := 2
    for n > 1 {
        if n % factor == 0 {
            n /= factor
            factors = append(factors, factor)
        } else {
            factor += 1
        }
    }
    return factors
}
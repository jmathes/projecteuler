package main

import "fmt"
import "github.com/jmathes/projecteuler/go/lib/primes"

func main() {
    factors := primes.Factors(600851475143)
    fmt.Printf("Factors: %d\n", factors)
}
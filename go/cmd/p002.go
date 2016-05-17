package main

// import "fmt"
import "github.com/jmathes/projecteuler/go/lib/primes"

func main() {
    n1 := 1
    n2 := 1
    sum := 0
    
    for n2 < 4000000 {
        if n2 % 2 == 0 {
            sum += n2
        }
        n2 = n1 + n2
        n1 = n2 - n1
    }
    print(sum)

}
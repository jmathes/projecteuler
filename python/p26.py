"""
find the number d<1000 such that 1/d has the longest recurring cycle in its decimal fraction part
"""


def long_divide_digit(num, denom):
    i = 0
    while denom * i <= num:
        i += 1
    i -= 1
    return (i, num - denom * i)
    print i
    

def get_digit_length(num, denom):
    print "%s / %s: " % (num, denom), 
    answer = "0."
    visited_nodes = []
    length = 0
    while True:
        num *= 10
        length += 1
        (divisor, num) = long_divide_digit(num, denom)
        if (divisor, num) in visited_nodes:
            break
        answer += str(divisor)
        visited_nodes.append((divisor, num))
    print answer
    return length - 1

longest_length = 0
number_with_longest_length = None
for n in xrange(1, 1000):
    length = get_digit_length(1, n)
    if length > longest_length:
        longest_length = length
        number_with_longest_length = n

print number_with_longest_length
print longest_length
get_digit_length(1, number_with_longest_length)
"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

answers = {}

def ways(n, maxdigit):
    global answers
    if n <= 1 or maxdigit == 1:
        return 1
    if (n, maxdigit) in answers.keys():
        return answers[(n, maxdigit)]
    sum = 0
    i = 0
    while i * maxdigit <= n:
        sum += ways(n-(i * maxdigit), maxdigit-1)
        i += 1
    answers[(n, maxdigit)] = sum
    return sum

def ways_with_at_least_two(n, i):
    return ways(n, i) - 1

for i in xrange(100):
    a = ways_with_at_least_two(100, i+1)

print ways_with_at_least_two(100, 100)
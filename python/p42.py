"""
The nth term of the sequence of triangle numbers is given by, tn = .5n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

from cache import lru_cache
from math import sqrt

@lru_cache()
def is_triangle_number(n):
    x = sqrt(n*2.0 + .25) - 0.5
    return x == int(x)
    
for n in [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]:
    assert is_triangle_number(n)
for n in [2, 4, 8, 14, 17, 27, 35, 40, 49, 56]:
    assert not is_triangle_number(n)
    
def word_value(word):
    return sum([ord(letter) - 64 for letter in word])

assert word_value("A") == 1
assert word_value("Z") == 26
assert word_value("SKY") == 55

def is_triangle_word(word):
    return is_triangle_number(word_value(word))

assert is_triangle_word("SKY")
assert is_triangle_word("A")
assert is_triangle_word("AAA")
assert is_triangle_word("C")
assert is_triangle_word("F")
assert is_triangle_word("A"*36)

wordfile = open('words.txt', 'r')
wordline = wordfile.readline()
words = wordline[1:-1].split('","')

print sum([1 for word in words if is_triangle_word(word)])
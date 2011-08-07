"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""

spiral = [[1]]

last_num_added = 1
from pprint import pprint

def add_column_right(spiral):
    global last_num_added
    for row in spiral:
        last_num_added += 1
        row.append(last_num_added)
    return spiral

def add_row_bottom(spiral):
    global last_num_added
    howmany = len(spiral[0])
    spiral.append(range(last_num_added + howmany, last_num_added, -1))
    last_num_added += howmany
    return spiral
    return spiral

def add_column_left(spiral):
    global last_num_added
    newrange = range(last_num_added + len(spiral), last_num_added, -1)
    for i in xrange(len(newrange)):
        spiral[i] = [newrange[i]] + spiral[i]
    last_num_added = spiral[0][0]
    return spiral

def add_row_top(spiral):
    global last_num_added
    spiral = [range(last_num_added + 1, last_num_added + len(spiral[0]) + 1)] + spiral
    last_num_added = spiral[0][len(spiral[0])-1]
    return spiral

operation_list = [add_column_right, add_row_bottom, add_column_left, add_row_top]

i = 0
squaresize = 1001
while len(spiral) < squaresize or len(spiral[0]) < squaresize:
    spiral = operation_list[i%4](spiral)
    i += 1
    

sum = 0
for i in xrange(squaresize):
    sum += spiral[i][i]
    sum += spiral[squaresize - i - 1][i]
    if i == squaresize - i - 1:
        sum -= spiral[i][i]

print sum
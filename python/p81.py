"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.


131    673    234    103    18
201    96    342    965    150
630    803    746    422    111
537    699    497    121    956
805    732    524    37    331

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""

from pprint import pprint, pformat

matrixfile = open('matrix.txt', 'r')
matrixlines = matrixfile.readlines()
matrix = [[int(s) for s in line.split(",")] for line in matrixlines]

for y in xrange(len(matrix)):
    for x in xrange(len(matrix[y])):
        print "%s, %s" % (y, x)
        if x == 0 and y == 0:
            pass
        elif y == 0:
            matrix[y][x] += matrix[y][x-1]
        elif x == 0:
            matrix[y][x] += matrix[y-1][x]
        else:
            matrix[y][x] += min(matrix[y-1][x], matrix[y][x-1])

print matrix[y][x]



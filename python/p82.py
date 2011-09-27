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

#matrix = [
#[131,    673,    234,    103,    18],
#[201,    96,    342,    965,    150],
#[630,    803,    746,    422,    111],
#[537,    699,    497,    121,    956],
#[805,    732,    524,    37,    331]]

matrix = [[[n, 10**100, 10**100, 10**100] for n in row] for row in matrix]

for y in xrange(len(matrix)):
    matrix[y][0][1] = matrix[y][0][0]
    matrix[y][0][2] = matrix[y][0][0]
    matrix[y][0][3] = matrix[y][0][0]

for x in xrange(1, len(matrix[0])):
    for y in xrange(0, len(matrix)):
        matrix[y][x][1] = matrix[y][x][0] + min(matrix[y][x-1][1:])
    for y in xrange(1, len(matrix)):
        matrix[y][x][2] = matrix[y][x][0] + min(matrix[y-1][x][1:])
    for y in xrange(len(matrix)-2, -1, -1):
        matrix[y][x][3] = matrix[y][x][0] + min(matrix[y+1][x][1:])
            
#pprint(matrix)
print min([min(entry[1:]) for entry in [row[len(row)-1] for row in matrix]])



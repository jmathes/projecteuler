"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.


131    673    234    103    18
201    96    342    965    150
630    803    746    422    111
537    699    497    121    956
805    732    524    37    331

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by moving left, right, up, and down."""

from pprint import pprint, pformat

matrixfile = open('matrix.txt', 'r')
matrixlines = matrixfile.readlines()
matrix = [[int(s) for s in line.split(",")] for line in matrixlines]

matrix = [
[131,    673,    234,    103,    18],
[201,    96,    342,    965,    150],
[630,    803,    746,    422,    111],
[537,    699,    497,    121,    956],
[805,    732,    524,    37,    331]]

smallest = min(min(row) for row in matrix)
print smallest
size = len(matrix)

def h(square):
    return max([size - square.y, size - square.x]) * smallest

class Square():
    def __init__(self, y, x, n):
        self.y = y
        self.x = x
        self.v = v
        self.distance = 10**100
        
    def neighbors(self):
        neighbors = []
        for y in xrange(min(self.y-1, 0), max(self.y+1, size-1)):
            for x in xrange(min(self.x-1, 0), max(self.x+1, size-1)):
                if y != self.y and x != self.x:
                    neighbors.append(smatrix[y][x])
        return neighbors

smatrix = []

for y in xrange(size):
    smatrix.append([])
    for x in xrange(size):
        smatrix[y][x] = Square(y, x, matrix[y][x])

visited_squares = []
queued_squares = [smatrix[0][0]]

while True:
    queued_squares.sort(cmp=lambda x,y: cmp())

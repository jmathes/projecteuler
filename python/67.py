trianglefile = open('triangle.txt', 'r')
triangle = trianglefile.readlines()
triangle = [[int(num) for num in row.split()] for row in triangle]


maxpath_triangle = triangle * 1

for y in xrange(0, len(triangle)):
    for x in xrange(0, len(triangle[y])):
        if x == 0 and y == 0:
            pass
        elif x == y:
            maxpath_triangle[y][x] += maxpath_triangle[y-1][x-1]
        elif x == 0:
            maxpath_triangle[y][x] += maxpath_triangle[y-1][x]
        else:
            maxpath_triangle[y][x] += max(maxpath_triangle[y-1][x], maxpath_triangle[y-1][x-1])

print max(maxpath_triangle[len(maxpath_triangle) -1 ])
        

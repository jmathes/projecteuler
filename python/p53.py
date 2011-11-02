"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =    
n!/(r!(n-r)!)
,where r  n, n! = n(n1)...321, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?
"""
from pprint import pprint, pformat
cutoff = 1000000

class partial_pascal_row():
    def __repr__(self):
        return ('%s{'+self.row.__repr__()[1:-1]+'}') % (self.r-1)
    
    def __init__(self, row, r):
        self.row = row*1
        self.r = r
        
    def __getitem__(self, i):
        if i<0:
            return 0
        if i == len(self.row):
            if self.r/2*2==self.r:
                return self.row[-1]
            return self.row[-2]
        return self.row[i]
    
    def append(self, val):
        self.row.append(val)
    
    def __iter__(self):
        return self.row


ppt = [partial_pascal_row([1], 0)]
r = 0

answer = 0

while True:
    r += 1
    ppt.append(partial_pascal_row([], r))
    for i in xrange((r+1)/2):
        ppt[r].append(ppt[r-1][i-1] + ppt[r-1][i])
        if ppt[r][i] >= cutoff:
            answer += r - 2*i
            break
    if (r-1)>=100:
        break

#pprint(ppt)
print answer
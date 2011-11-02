"""
The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

CRAP = 0
PAIR = 1
TWO_PAIR = 2
SET = 3
STRAIGHT = 4
FLUSH = 5
BOAT = 6
QUADS = 7
STRAIGHT_FLUSH = 8

from pprint import pprint, pformat
pokerfile = open('poker.txt', 'r')
pokerlines = pokerfile.readlines()
hands = []


def evaluate(hand):
    suit = hand[0][-1]
    flush = True
    ranks = {}
    type = CRAP
    order = []
    for card in hand:
        if card[-1] != suit:
            flush = False
        rank = int(card[:-1])
        if rank not in ranks.keys():
            ranks[rank] = 0
        ranks[rank] += 1
        if ranks[rank] == 2:
            if type == PAIR:
                type = TWO_PAIR
                order = order + [rank]
                order.sort()
                order.reverse()
            elif type == SET:
                type = BOAT
                order = order + [rank]
            else:
                type = PAIR
                order = [rank]
        if ranks[rank] == 3:
            if type == TWO_PAIR:
                type = BOAT
                if order[0] != rank:
                    order.reverse()
            else:
                type = SET
        if ranks[rank] == 4:
            type = QUADS
            order = [rank]

    uranks = ranks.keys()
    uranks.sort()
    handrank = uranks*1
    handrank.reverse()

    if type != CRAP:
        return [type] + order + handrank
    if uranks == [2,3,4,5,14]:
        uranks = [1,2,3,4,5]
    if [r - uranks[0] for r in uranks] == xrange(5):
        if flush:
            return [STRAIGHT_FLUSH, uranks[4]]
        return [STRAIGHT, uranks[4]]
    if flush:
        return [FLUSH] + handrank
    return [CRAP] + handrank


won_hands = 0

for rawline in pokerlines:
    line = rawline.replace("T", "10")
    line = line.replace("J", "11")
    line = line.replace("Q", "12")
    line = line.replace("K", "13")
    line = line.replace("A", "14")
    cards = line[:-2].split(" ")
    hand1 = cards[:5]
    hand2 = cards[5:]
    print "="*100
    print rawline
    print " ",evaluate(hand1)
    print " ",evaluate(hand2)
    if evaluate(hand1) > evaluate(hand2):
        print "winner winner chicken dinner"
        won_hands += 1


print won_hands
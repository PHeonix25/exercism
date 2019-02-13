from collections import Counter

YACHT =  lambda dice: 50 if len(set(dice)) == 1 else 0
SUM_X =  lambda dice, x: sum(y for y in dice if y == x)
ONES =   lambda dice: SUM_X(dice, 1)
TWOS =   lambda dice: SUM_X(dice, 2)
THREES = lambda dice: SUM_X(dice, 3)
FOURS =  lambda dice: SUM_X(dice, 4)
FIVES =  lambda dice: SUM_X(dice, 5)
SIXES =  lambda dice: SUM_X(dice, 6)
CHOICE = lambda dice: sum(x for x in dice)

FULL_HOUSE = lambda dice: sum(dice) \
    if sorted(Counter(dice).values()) == [2,3] else 0
FOUR_OF_A_KIND = lambda dice: max(i*4 for i in \
    [x[0] for x in Counter(dice).most_common(1) if x[1] >= 4] or [0])

STRAIGHT = lambda dice, start, stop: \
    bool(sorted(dice) == list(range(start, stop)))
LITTLE_STRAIGHT = lambda dice: 30 if STRAIGHT(dice, 1, 6) else 0
BIG_STRAIGHT = lambda dice: 30 if STRAIGHT(dice, 2, 7) else 0

def score(dice, category):
    return category(dice)

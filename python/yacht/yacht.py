from collections import Counter

YACHT =  lambda dice: 50 if len(set(dice)) == 1 else 0
ONES =   lambda dice: sum(x for x in dice if x == 1)
TWOS =   lambda dice: sum(x for x in dice if x == 2)
THREES = lambda dice: sum(x for x in dice if x == 3)
FOURS =  lambda dice: sum(x for x in dice if x == 4)
FIVES =  lambda dice: sum(x for x in dice if x == 5)
SIXES =  lambda dice: sum(x for x in dice if x == 6)
CHOICE = lambda dice: sum(x for x in dice)

FULL_HOUSE = lambda dice: sum(dice) \
    if sorted(Counter(dice).values()) == [2,3] else 0
FOUR_OF_A_KIND = lambda dice: max(i*4 for i in \
    [x[0] for x in Counter(dice).most_common(1) if x[1] >= 4] or [0])
LITTLE_STRAIGHT = lambda dice: 30 if sorted(dice) == list(range(1, 6)) else 0
BIG_STRAIGHT = lambda dice: 30 if sorted(dice) == list(range(2, 7)) else 0

def score(dice, category):
    return category(dice)

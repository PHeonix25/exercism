from collections import Counter

# Score categories
# Change the values as you see fit
YACHT =  ('YACHT',  lambda dice: 50 if len(set(dice)) == 1 else 0)
ONES =   ('ONES',   lambda dice: sum(x for x in dice if x == 1))
TWOS =   ('TWOS',   lambda dice: sum(x for x in dice if x == 2))
THREES = ('THREES', lambda dice: sum(x for x in dice if x == 3))
FOURS =  ('FOURS',  lambda dice: sum(x for x in dice if x == 4))
FIVES =  ('FIVES',  lambda dice: sum(x for x in dice if x == 5))
SIXES =  ('SIXES',  lambda dice: sum(x for x in dice if x == 6))
FULL_HOUSE = ('FULL HOUSE', \
    (lambda dice: sum(dice) if sorted(Counter(dice).values()) == [2,3] else 0))
FOUR_OF_A_KIND = ('FOUR OF A KIND', \
    lambda dice: max(i*4 for i in \
        [x[0] for x in Counter(dice).most_common(1) if x[1] >= 4] or [0]))
LITTLE_STRAIGHT = ('LITTLE STRAIGHT', \
    lambda dice: 30 if sorted(dice) == list(range(1, 6)) else 0)
BIG_STRAIGHT = ('BIG STRAIGHT', \
    lambda dice: 30 if sorted(dice) == list(range(2, 7)) else 0)
CHOICE = ('CHOICE', lambda dice: sum(x for x in dice))

def score(dice, category):
    func = category[1]
    print(f"Dice: {dice}, Category: {category}")
    if func is None:
        print(f"Requested category '{category[0]}' is not implemented yet.")
    else:
        print(f'Found category, providing {dice}; result is {func(dice)}')
        return func(dice)

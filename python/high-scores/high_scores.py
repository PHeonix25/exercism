class HighScores():
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def personal_best(self):
        return max(self.scores)

    def report(self):
        last = self.latest()
        best = self.personal_best()
        diff = best - last
        return f"Your latest score was {last}. " + \
            ("That's your personal best!", f"That's {diff} short of your personal best!")[diff > 0]

class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
    
    def latest(self):
        return self.scores[-1]

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def personal_best(self):
        return sorted(self.scores, reverse=True)[0]

    def report(self):
        last = self.latest()
        best = self.personal_best()
        diff = best - last
        return "Your latest score was {}. ".format(last) + \
            ("That's your personal best!", "That's {} short of your personal best!".format(diff))[diff > 0]
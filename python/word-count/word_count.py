import re, itertools

def word_count(phrase=''):
    phrase = sorted([word.strip('\'') for word in re.split("[^a-z0-9']+", phrase.lower().strip())])
    return { key : sum(1 for x in group) for (key, group) in itertools.groupby(phrase) if key }
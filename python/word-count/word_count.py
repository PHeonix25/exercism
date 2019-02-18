import re, itertools

def word_count(phrase=''):
    lower = phrase.lower().strip()
    srted = sorted([word.strip('\'') 
        for word in re.split("[^a-z0-9']+", lower)])

    return { key : sum(1 for x in group) 
        for (key, group) in itertools.groupby(srted) 
        if key }
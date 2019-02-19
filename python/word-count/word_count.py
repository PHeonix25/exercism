import re, itertools
from collections import Counter

def word_count_without_counter(phrase=''):
    """
    Counts "words" (as defined by [a-zA-Z0-9']) after stripping them,
    by sorting them and passing them to 'groupby', and using the word
    as the key value itself, and summing the number of values in the group.

    Solution was not required to be case-sensitive, so everything
    is converted to lower-case first in order to make parsing easier.
    """
    lower = phrase.lower().strip()
    srted = sorted(word.strip('\'') 
        for word in re.split("[^a-z0-9']+", lower))

    return { key : sum(1 for x in group) 
        for (key, group) in itertools.groupby(srted) 
        if key } # TIP: this 'if key' removes blank keys

def word_count_with_counter(phrase=''):
    """
    Counts words (as defined by [a-zA-Z0-9']) by using 
    collections.Counter(), chunking the words using a 
    list comprehension over the result of a regex eval.
    """
    return Counter(word.strip('\'') 
        for word in re.split("[^a-z0-9']+", phrase.lower().strip()) 
        if word)

def word_count(phrase=''):
    return word_count_with_counter(phrase)
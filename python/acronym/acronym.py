import re

def abbreviate(words=''):
    """Abbreviates a given sentence to its acronym (_ignoring quotation marks_)"""
    return ''.join(word[0].upper() for word in re.split(r"[^a-zA-Z']+", words) if word)

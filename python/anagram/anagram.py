def find_anagrams(word='', candidates=[]):
    word = word.lower()
    # I dislike how many times we call lower() below, 
    # but some comparisons are case-sensitive when others aren't
    return [c for c in candidates
        if word != c.lower()
        and sorted(word) == sorted(c.lower())]

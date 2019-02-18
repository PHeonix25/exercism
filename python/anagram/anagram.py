def find_anagrams(word='', candidates=[]):
    word = word.lower()
    return [orig for (orig, lower) 
        in [(c, c.lower()) for c in candidates]
        if word != lower and sorted(word) == sorted(lower)]

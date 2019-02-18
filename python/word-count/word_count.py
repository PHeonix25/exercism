import re

def word_count(phrase):
    wordcount = {}
    clean_phrase = [word.strip('\'') for word in re.split("[^a-z0-9']+", phrase.lower().strip(), flags=re.IGNORECASE)]
    for word in clean_phrase:
        if word: 
            wordcount[word] = wordcount.get(word, 0) + 1
    return wordcount
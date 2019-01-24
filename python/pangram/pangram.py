from string import ascii_lowercase

def is_pangram__first_try(sentence):
    chars = list()
    for character in sentence.lower():
        if character.isalpha():
            if not chars.__contains__(character):
                chars.append(character)

    return chars.__len__() == 26

def is_pangram(sentence):
    return set(ascii_lowercase).issubset(sentence.lower())

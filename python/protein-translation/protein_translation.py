import itertools

__codons__ = dict({
    "AUG":"Methionine",
    "UUU":"Phenylalanine",
    "UUC":"Phenylalanine",
    "UUA":"Leucine",
    "UUG":"Leucine",
    "UCU":"Serine",
    "UCC":"Serine",
    "UCA":"Serine",
    "UCG":"Serine",
    "UAU":"Tyrosine",
    "UAC":"Tyrosine",
    "UGU":"Cysteine",
    "UGC":"Cysteine",
    "UGG":"Tryptophan"
})

def get_groups(strand):
    """Returns chunks of 3 from the strand for easier comparison"""
    args = [iter(strand)] * 3
    return itertools.zip_longest(*args)

def proteins(strand):
    """Returns a list of the proteins contained in the strand"""
    result = list()
    for breakdown in get_groups(strand):
        val = __codons__.get(''.join(breakdown))
        if val is None:
            return result
        result.append(val)

    return result

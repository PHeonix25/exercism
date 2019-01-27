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
    """Returns a list of the proteins that are in the strand using a functional approach"""
    return list(__codons__.get(s) for s in itertools.takewhile( \
        lambda x: __codons__.get(x) is not None, \
        (''.join(chunk) for chunk in get_groups(strand))) \
    )

def proteins_procedural(strand):
    """Returns a list of the proteins that are in the strand using a very procedural approach"""
    result = list()
    for breakdown in get_groups(strand):
        val = __codons__.get(''.join(breakdown))
        if val is None:
            return result
        result.append(val)

    return result

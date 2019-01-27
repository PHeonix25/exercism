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

def proteins(strand=''):
    return proteins_functional(strand)

def proteins_functional(strand=''):
    """Returns a list of the proteins that are in the strand, using a functional approach"""
    return list(__codons__.get(protein) for protein in \
        itertools.takewhile( \
            lambda x: __codons__.get(x) is not None, \
            (''.join(chunk) for chunk in \
                itertools.zip_longest(*([iter(strand)] * 3)))))
                # This last line probaby deserves some explanation:
                #   We're taking a reference to the same iterator, and
                #   providing it three times to the same function so it'll:
                #   step, step, step, return, step, step, step, return, etc.

def proteins_procedural(strand=''):
    """Returns a list of the proteins that are in the strand using a very procedural approach"""
    result = list()
    i = 3
    while i <= len(strand):
        protein = __codons__.get(strand[i-3:i])
        if protein is None:
            return result
        result.append(protein)
        i += 3
    return result

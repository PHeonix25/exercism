def dna_to_rna(dna):
    return {
        'G':'C',
        'C':'G',
        'T':'A',
        'A':'U'
    }.get(dna, '')

def to_rna(dna_strand=''):
    """Converts a DNA strand, to a matching RNA strand"""

    return ''.join(dna_to_rna(char) for char in dna_strand)

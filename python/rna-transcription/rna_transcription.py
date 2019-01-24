# Hold the mapping in a static instance,
# rather than per-instantiation.
__dna_mapping__ = {
        'G':'C',
        'C':'G',
        'T':'A',
        'A':'U'
    }

def dna_to_rna(dna):
    return __dna_mapping__.get(dna, '')

def to_rna(dna_strand=''):
    """Converts a DNA strand to a matching RNA strand"""

    return ''.join(dna_to_rna(char) for char in dna_strand)
